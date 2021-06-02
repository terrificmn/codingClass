# ROS 같은 로봇 프로그램

오픈 소스인 ROS와 비슷한 로봇 프로그램은 어떤 것들이 있는지 찾아보았다. 
대표적으로 모바일 로봇 프로그래밍, 마이크로소프트의 로봇틱스 개발자 스튜디오, 
Carmen 등이 있다.

## Mobile Robot Programming Toolkit
MRPT라고 불리는 이것은 Open소스 C++ 라이브러리 이고 슬램 (SLAM: Simultaneous Localization and Mapping), 컴퓨터 비전, 모션 계획(장애물 피하기)을 하게 도와주는 프로그램이다.

[Discover MRPT](https://www.mrpt.org/)

다운로드, 튜토리얼 및 API 사용법이 문서화되어 있다

<br>

## Webbots
3D 로봇 시뮬레이터 이다. 산업, 교육, 연구등에 사용되고 있다.
1996년에 Webbots 프로젝트가 스위스 Federal Institute of Technology 의 Dr. Oliveier Michel 시작이 되었고, 아파치2 라이센스 오픈소스이다.

ROS의 gazebo와 비슷한 것 같다. 로봇 모델, 센서, 액츄에이터등을 포함한다.

로봇 controller 프로그래밍은 C, C++, Python 등을 사용하고 간단한 API를 사용하게 되어 있다.

<img src=0>
<br>

(Commons is a freely licensed media file repository)


<br>

## Microsoft Robotics Developer Studio
MRDS라고 불리는 윈도우즈 기반의 로봇 컨트롤 프로그램 및 시뮬레이션이다.
학자, 취미로 하는사람들, 개발자 (상업적)을 위해서 만들어졌고 윈도즈 7 OS가 필요하다

Visaul Programming tool, Microsoft Visual Programming Language, 웹기반의 윈도우즈 기반의 인터페이스, 3D 시뮬레이션, 로봇 센서 및 액츄에이터를 쉽게 접근할 수 있게 되어 있고

프로그래밍 언어는 C# 을 이용한다

MRDS는 로봇에게 직접 컴파일 및 로드를 시킬 수 없고, Windows 장치를 이용해한다고 한다.

CCR Common Concurrent Runtime 멀티 태스킹을 처리하기 위해서 개발되었다고 하는데 이를 이용한다.

VSE Visual Simulation Environment 을 이용해서 비싼 로봇을 직접 사용하기보다 시뮬레이션 환경을 이용해서 3D 가상환경으로 마이크로소프트의 XNA 2.0 플랫폼을 사용한다

<br>

## Carmen Robot Navigation Toolkit
로봇 컨트롤을 하기위한 오픈소스 모음 소프트웨어 이다. 
로봇 내비게이션을 하기 위한 프로그램 같지만, 현재는 홈페이지도 제대로 운영이 안되고 있는 것 같다
2008까지 beta 버전이 나오고 더이상의 업데이트는 없는 것 같다.

<br>

## ROS2
같은 ROS이지만 완전 새로운 시스템이자 같은 시스템(?)이라고 해서 알아보았다

로봇을 위한 라이브러리, 툴 등의 소프트웨어이며 Robot Operating System 이다.

ROS 는 2007년부터 시작되었고, 휴머노이드 PR2라는 로봇을 바탕으로 Willow  Garage에 의해 만들어졌고 PR2만 있는 것이 아니였기에 더 많은 로봇에 표준적이면서 향상시킬 수 있는 소프트웨어를 향상 시키고 수정 적용하고 싶어했기에 미들웨어로서 ROS가 발전하게 되었는데

ROS를 향상시키기 위해서는 많은 변화가 있어야하고, 이는 ROS를 아주 불안정하게 만들어 버릴 것을 알았기 때문에 
ROS 2 프로젝트는 ROS를 향상시키기 보다는 처음부터 새롭게 NEW ROS를 만들었다고 한다.

그리고 현재 ROS 시스템을 바꾸는 것을 매우 큰 리스크였다고 한다. 왜냐하면 ROS는 이미 
많은 사람들에게 개발되어서 사용되고 있었기 때문이다. 

지금 현재는 ROS Noetic (2020년 업데이트 됨) 마지막 ROS 버전이며, Python3를 지원하기 위해서 나왔다고 하며, 이는 당분간 개발자들이 ROS를 사용가능하게 해줄 것이라고 한다. 
그리고 우분투 20 지원함 

ROS2는 Foxy Fitzroy 이며 (2020년 업데이트 됨), 1년마다 ROS2 버전이 나올 예정이라고 한다.

<img src=1>
<br>

-아래는 간단 비교-

ROS는 우분투에서 사용 되고 있고 OS X와 다른 리눅스 디스트리뷰션에서는 experimental 실험적이라고 칭하고 있다. (사용은 가능)

ROS2는 Ubuntu Xenial과 OS X EI Captian 과 Windows 10에서 테스트 하고 있으며, 
C++ 를 사용하고, 파이썬 3.5 이상이다.

ROS는 하나의 프로세스에서 하나의 노드만 생성이 가능했지만, ROS2는 하나의 프로세스에 멀티플 노드를 생성하는 것이 가능하다.

ROS는 roslaunch를 XML로 정의를 하는데 이는 제한된 성능을 발휘, 반면에 ROS2 는 파이썬으로 작성할 수 있고 복잡한 로직이 (조건문)등이 가능해진다.

<br>

## 하지만 배우는 학생 입장에서는 ROS를 배우라
학생, 교수, 연구자까지는 아직까지는 ROS
회사와, 생산자들은 ROS2로 전환을 시도하라

이유는 아직까지는 ROS2는 패키지 호환성이 떨어지고, 소프트웨어 안정성도 약하기 때문
하지만 곧 ROS2가 적용되는 날이 온다면 ROS2는 다양한 컨셉등이 ROS와 크게 다르지 않기 때문에 그때 배우면 될 듯하다


[참고 사이트 - ros vs ros2](https://blog.generationrobots.com/en/ros-vs-ros2/
)  

[참고 사이트 -ros2 살펴보기](https://roboticsbackend.com/ros1-vs-ros2-practical-overview/
)



