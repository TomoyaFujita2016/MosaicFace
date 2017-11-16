import cv2
import sys
import os
import argparse

def addDirStr(path):
    return "./" + path + "/"

def removeNotImage(files):
    output = []
    exs = [".jpg", ".png", ".bmp", "jpeg"]
    for fileName in files:
        for ex in exs:
            if ex in fileName:
                output.append(fileName)
                break
            if ex is exs[-1]:
                print(fileName + " is NOT in " + str(exs))
    return output

cascadePath = "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml"

SHOW_SIZE = 500
MOSIC_PARAM = 20
FACE_RATIO = 0.045
DISPLAY_TIME = 500

loadDir = "OriginalImages"
saveDir = "MosaicImages"
noFaceDir = "NoFaceImages"

# parser
parser = argparse.ArgumentParser()
parser.add_argument("--d", help="Remove files in " + saveDir + ", " + noFaceDir,
                           action="store_true")
parser.add_argument("--ad", help="Remove files in " + loadDir + ", "+ saveDir + ", " + noFaceDir,
                            action="store_true")
parser.add_argument("--show", help="Show each mosaic images.",
                            action="store_true")
parser.add_argument("-fr", help="The minimum face ratio in each images. DEFAULT="+str(FACE_RATIO))
parser.add_argument("-t", help="Display time[ms] of mosaic images. DEFAULT="+str(DISPLAY_TIME))
parser.add_argument("-mp", help="Mosaic parameter. When the parameter is small, it becomes coarse. DEFAULT="+str(MOSIC_PARAM))

parser_args = parser.parse_args()

if not os.path.exists(loadDir):
    os.mkdir(loadDir)
if not os.path.exists(saveDir):
    os.mkdir(saveDir)
if not os.path.exists(noFaceDir):
    os.mkdir(noFaceDir)

loadDir = addDirStr(loadDir)
saveDir = addDirStr(saveDir)
noFaceDir = addDirStr(noFaceDir)

if parser_args.d:
    os.system("rm " + saveDir + "*")
    os.system("rm " + noFaceDir + "*")
    print("Removed files in " + saveDir + ", " + noFaceDir)
    exit()
if parser_args.ad:
    os.system("rm " + saveDir + "*")
    os.system("rm " + noFaceDir + "*")
    os.system("rm " + loadDir + "*")
    print("Removed files in "+ loadDir + ", " + saveDir + ", " + noFaceDir)
    exit()

if parser_args.t:
    DISPLAY_TIME = int(parser_args.t)
if parser_args.fr:
    FACE_RATIO = float(parse_args.fr)
if parser_args.mp:
    MOSIC_PARAM = int(parser_args.mp)

imageNames = os.listdir(loadDir)
imageNames = removeNotImage(imageNames)

for imagePath in imageNames:
    print("== " + imagePath  + " ==")
    image = cv2.imread(loadDir + imagePath)
    result = cv2.imread(loadDir + imagePath)
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier(cascadePath)
    faceRect = cascade.detectMultiScale(imageGray, scaleFactor=1.1, minNeighbors=1, minSize=(1,1))
    
    if len(faceRect) <= 0:
        print("No face.")
        os.system("cp "+loadDir+imagePath + " " + noFaceDir+"noFace_"+imagePath)
    else:
        # confirm face
        imageSize = image.shape[0] * image.shape[1]
        filteredFaceRects = []
        for faceR in faceRect:
            faceSize = faceR[2]*faceR[3]
            if FACE_RATIO  < (faceSize / imageSize):
                filteredFaceRects.append(faceR)

        if len(filteredFaceRects) > 0:
            print("Get face")
            for (x, y, w, h) in filteredFaceRects:
                cutImg = image[y:y+h, x:x+w]
                cutFace = cutImg.shape[:2][::-1]
                cutImg = cv2.resize(cutImg, (MOSIC_PARAM, MOSIC_PARAM))
                cutImg = cv2.resize(cutImg, cutFace, interpolation=cv2.INTER_NEAREST)
                result[y:y+h, x:x+w] = cutImg
                cv2.imwrite(saveDir+"mosic_"+imagePath, result)
            if parser_args.show:
                height = int(SHOW_SIZE)
                width = int(result.shape[1] * SHOW_SIZE / result.shape[0])
                cv2.imshow("MosaicImage", cv2.resize(result, (width, height)))
                cv2.waitKey(DISPLAY_TIME)
        else:
            print("No appropriate face size.")
            os.system("cp "+loadDir+imagePath + " " + noFaceDir+"noFace_"+imagePath)


