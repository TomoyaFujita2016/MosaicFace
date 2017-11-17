# MosaicFace
|Before|After|
|---|---|
|![](https://github.com/TomoyaFujita2016/MosaicFace/blob/master/OriginalImages/lena.jpg)|![](https://github.com/TomoyaFujita2016/MosaicFace/blob/master/MosaicImages/mosic_lena.jpg)|

## Usage
  #### 1. ``` git clone https://github.com/TomoyaFujita2016/MosaicFace.git ```
  #### 2. ``` cd MosaicFace ```
  #### 3. ``` python3 generateMosaicFace.py ``` (In order to make dirs.)
  #### 3. ``` cp "ImageFileDir"/* OriginalImages/ ``` 
  #### 4. ``` python3 generateMosaicFace.py ```

## Requirements
  #### 1. python 3
  #### 2. OpenCV3
  #### 3. Some Face Images
  
## Options
  #### Please confirm options by ``` python3 generateMosaicFace.py -h ```
  ```
usage: generateMosaicFace.py [-h] [--d] [--ad] [--show] [--save] [--video]
                             [-fr FR] [-t T] [-mp MP]
optional arguments:
  -h, --help  show this help message and exit
  --d         Remove files in MosaicImages, NoFaceImages
  --ad        Remove files in OriginalImages, MosaicImages, NoFaceImages
  --show      Show each mosaic images.
  --save      Saving images when you use --video.
  --video     Use Camera.
  -fr FR      The minimum face ratio in each images. DEFAULT=0.045
  -t T        Display time[ms] of mosaic images. DEFAULT=500
  -mp MP      Mosaic parameter. When the parameter is small, it becomes
              coarse. DEFAULT=20
  ```
