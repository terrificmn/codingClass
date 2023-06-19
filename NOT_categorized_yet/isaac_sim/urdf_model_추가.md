# urdf robot model 추가
메뉴에서 Create -> Isaac -> Robots -> 

Manipulators 에서 
맘에 드는 로봇 팔을 선택해준다  

Wheeled Robots 에서 모바일 로봇도 선택이 가능  


> 기본적인 조작은 Alt 키를 누른 상태에서 마우스를 왼쪽을 드래그 하면 카메라 회전이 가능   
모델 이동은 Move 토글 버튼을 눌러서 (오른쪽 Stage 패널에서 해당 모델 객체를 선택해주면 다 선택이 된다)   




## urdf 파일 열기
isaac sim 에서는 urdf 파일을 지원하므로 urdf 파일을 선택해주면 모델을 불러올 수가 있다   

> USD 파일로 변환이 된다   

쉽게 구할 수 있는 urdf-로 클론해서 불러올 수가 있다 

[Techman 로봇 팔 깃허브 클론](https://github.com/TechmanRobotInc/tmr_ros1)   

여기에서는 다른 것은 다 필요 없고, **tm_description 패키지만 필요** (나머지는 다 지워도 됨)  

파일메뉴에서 Isaac Utils -> Workflows -> URDF importer 선택

Import 부분에서 input file 을 지정해준다   
해당 tm_description 의 urdf 디렉토리에서 tm5-900.urdf 선택  
Select Urdf를 클릭한 후에   

Import 버튼을 클릭해주면 된다 
  
> Output Directory로 지정할 수 있다. 디폴트로 사용, 같은 디렉토리에 USD 변환 파일 및 디렉토리를 만들어준다   
해당 urdf의 디렉토리에 새로 생성된 디렉토리(urdf 이름)을 보면 .usd 파일이 만들어져 있다 


## xacro 변환
단, usdf 파일로 되어 있어야 하므로 xacro 파일등은 미리 변환을 해야한다  

보통 xacro 파일로 많이 되어 있으므로 xacro 파일도 urdf로 변경을 해줘야하는데 메인 xacro프로그램을 지정해주면 된다   
xacro 파일을 리다이렉트로(생성) 만들어 준다.   
예:  
```
rosrun xacro xacro main_xacro파일.xacro > converted.urdf
```
