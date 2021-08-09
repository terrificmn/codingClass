# AI tensorflow object detection 프로젝트
사진 또는 동영상을 업로드를 해서 물체 디텍팅을 해주는 웹 서비스 입니다.  


첫 메인페이지의 모습입니다.    
<img src=0>
<br/>

그리고 기능 중의 하나인 Object detection을 선택했을 때 나오는 화면 스크린 샷
<img src=1>
<br/>


<br/>

# 주요기능
AI 모델별로 이미지/동영상을 업로드해서 이미지 디텍팅을 해 볼 수 있으나,   
현재는 **작동이 중지**되어 있습니다.  
이유는 배포한 AWS 의 free tier의 물리적 한계 때문입니다.

1. Tensorflow를 이용한 이미지 Object detection
    - 이미지의 Object Detection 과정을 확인 할 수 있습니다.

2. Tensorflow를 이용한 동영상 Object detection
    - 영상의 Object Detection 과정을 확인 할 수 있습니다.

3. Yolo 모델을 이용한 이미지/동영상 Object Detection 
    - 웹 페이지 스크린 샷
    
    <img src=2>
    <br/>
    
4. SSD 를 이용한 이미지/동영상 Object Detection
    - 웹 페이지 스크린 샷
    
    <img src=3>
    <br/>

5. OpenCV - Semantic Segmentation
    - 웹 페이지 스크린 샷
    
    <img src=4>
    <br/>


<br/>

## 사용 언어
python

<br/>

## 필요한 라이브러리 (requirements)
streamlit, cython, tensorflow==2.2.0, numpy, pandas, pycocotools  
joblib, opencv-python-headless, keras, imutils  

<br/>

## AI 모델
1. 이미지 detection: Tensorflow faster_rcnn_inception_resnet_v2_640x640

2. 동영상 detection: Tensorflow centernet_resnet50_v2_512x512

3. yolo: yolo3

4. SSD: ssd_mobilenet_v2_fpnlite_640x640


<br/>

## 프레임워크
streamlit       
파이썬 코드를 깔끔하게 웹에서 표현할 수 있는 프레임워크 입니다.

<br/>

## 개발환경
docker   
로컬에서 개발을 하다가 배포할 때 서버에서 동일한 환경을 만들어 주기 위해서  
도커 컨테이너로 개발환경을 구축했습니다.  
어느 리눅스 배포판 운영체제에서도 쉽게 작동이 될 수 있습니다.  

리눅스 배포판 운영체제를 사용했습니다. 대체로 CentOS 8기반에서 개발을 하였고  
docker를 이용해서 Ubuntu 18.04 서버에서 작동합니다.  

<br/>

## 서버 
AWS - EC2 t2.micro Free Tier  
아마존의 무료서버를 사용하고 있습니다. 무료인 1 CPU의 한계로 인해서 실제로 이미지 분석을 하는것에는   
무리가 있기 때문에 작업한 내용을 캡쳐하여 동영상으로 올리거나 미리 작업된 사진으로 대체하였습니다.  
다만, 아무리 서버의 한계로 웹 서비스를 만든다고 해도 실제로 작동하는 것이 중요하다고 생각했기 때문에   
사진/동영상의 업로드 및 분석 등의 모든 기능이 작동할 수 있게 개발하였고 현재는 분석 기능만 중단된 상태입니다.  

<br/>

## 깃 허브
소스코드를 볼 수 있습니다.

[깃허브 소스코드 보러가기](https://github.com/terrificmn/tensorflow-od.git)

<br/>

## 사이트 방문하기
아직 도메인이 없습니다. 양해 부탁드립니다.

[사이트 방문하기](http://54.180.113.157:8501/)


