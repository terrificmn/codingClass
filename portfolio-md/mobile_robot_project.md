# 무인 로봇 프로젝트
그 동안 배운 ROS를 활용해서 로봇의 움직임을 제어하고 자율주행을 목표로 삼고   
무인 로봇 프로젝트를 시작했습니다.

비록 적은 인원으로 힘들기도 했지만 재미있고 열정적으로 한 프로젝트 입니다.

<br/>

## 어떤 서비스를 할 수 있을까?
로봇에 어쩌면 가장 중요한 기능이자 기본이 되는 자율주행을 가능하게 한다면 여러가지 서비스를 
제공할 수 있게 되는데 예를 들자면 배달, 경비, 서빙 서비스등 가능해집니다.
자율주행이 목표를 세웠지만 이는 다양하게 서비스를 제공할 수 있는 방향으로
발전할 수 있다고 생각했습니다.

이미지??


<br/>

## 사용한 하드웨어 
1. UGV (Unmanned Groundd Vehicle)은 Agile 사의 Scout-mini
    - 각기 다른 4바퀴 모터 구동

<img src=0>

2. Intel L515 라이다 카메라 
    - 3D LiDAR, RGBD 카메라 사용가능 

<img src=1>

3. Intel T265 스테레오 카메라
    - 어안렌즈와 함께 IMU 센서 제공

<img src=2>

4. INTEL NUC Mini PC
    - 인텔사의 10세대 i5 프로세서 컴퓨터

<br/>

## 소프트웨어
1. ROS (Robot Operating System): melodic 버전  
로봇을 제어하기 위해 필요한 라이브러리 제공 및 로봇 운영체제

2. Ubuntu: 18.04 Bionic Beaver
ROS melodic 버전은 ubuntu 18.04 LTS 버전에 맞춰서 나왔기 때문에 리눅스 운영체제 배포판으로 사용

3. C++ / Python: 주 개발은 C++ 사용, Python

<br/>


## 협업 툴
팀원과는 git과 github을 사용해서 사용

제가 맡은 파트를 따서 브랜치를 만들고 작업을 진행하였습니다.
예: sm-slam

팀원도 맡은 파트를 따서 다른 브랜치를 만들고 작업을 진행하였습니다.
예: jw-tracker

다른 패키지를 작업을 하고 git branch까지 사용해서 작업 간 충돌을 방지할 수 있었습니다.

각자 commit 및 push가 끝나게 되면 pull request를 통해서 main(master)브랜치와 합병을 했습니다.


[무인 모바일 프로젝트 깃허브](https://github.com/terrificmn/patrol-robot.git)

<br/>

## 핵심 기술 
1. LiDAR: Light Detection and Ranging

<img src=3>

2. SLAM: Simultaneous Localization and Mapping 

<img src=4>


<br/>

## 사용한 알고리즘
SLAM을 하기 위해서 사용한 알고리즘은 Rtabmap 입니다.

rtabmap은 입력으로 스테레오, RGBD 카메라 및 2D/3D 라이다를 지원하며, 
출력으로 맵핑을 2D, 3D 지도를 만듭니다.

프로젝트에 사용한 인텔의 l515 라이다 카메라를 사용했을 때 라이다와 카메라의 기능을 다 이용해서 
슬램을 할 수 있었습니다.

<br/>

## 슬램 구성도
프로젝트에 사용한 슬램 구성도 입니다.

<img src=5>

<br/>

## 슬램 영상
링크 걸기!

<br/>

## color 트랙커 소개
빨간색 물체를 추적해서 Scout-Mini 차가 움직이며 따라가는 패키지 입니다.

추적은 일반 카메라를 사용했고, 물체가 카메라에서 사라지면 차의 움직임이 멈춥니다.
L515 LiDAR를 이용해서 앞에 사람이 있을 경우 멈춥니다.

color-tracker 패키지의 구성도 입니다.
<img src=5>


<br/>

## color 트랙커 영상
빨간색 원형 물체를 따라가는 영상 입니다.

영상 링크
<br/>


## 3조 협업 프로젝트를 진행
직업학교 내의 다른 3조와 협업 프로젝트를 진행

1. 3조에서는 sleep-detect 을 AI 학습을 해서 눈깜빡임을 감지

2. 사용한 AI은 Yolo5

3. 차량을 제어하는 패키지와 기존 3조의 패키지를 ROS 및 master를 remote 로봇으로 설정해서 통신

4. ROS publishing 및 subscribing에 필요한 topic 조율

5. Github


과정 :   
일반 PC에서 졸음을 가정하고 눈을 감으면 프로그램(3조)이 감지하게 되고 publish를 하게 됩니다.  
우리 팀은 차량 제어 프로그램에서 topic을 구독을 해서 자동차를 멈추게 합니다.

<br/>

## sleep-detection 소개 영상
디텍팅과 자동차 제어 협업 영상입니다.

영상 링크

<br/>
