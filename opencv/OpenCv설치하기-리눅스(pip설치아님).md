# 리눅스에서 직접 build 하기 

https://docs.opencv.org/master/d7/d9f/tutorial_linux_install.html


## Install minimal prerequisites (Ubuntu 18.04 as reference)
```
sudo apt update && sudo apt install -y cmake g++ wget unzip
```
## Download and unpack sources
```
wget -O opencv.zip https://github.com/opencv/opencv/archive/master.zip
unzip opencv.zip
```
## Create build directory
```
mkdir -p opencv-master/build && cd opencv-master/build
```
## Configure
```
cmake  ..
```
## Build
```
cmake --build .
```


참고 투토리얼 :   
http://wiki.ros.org/cv_bridge/Tutorials/UsingCvBridgeToConvertBetweenROSImagesAndOpenCVImages