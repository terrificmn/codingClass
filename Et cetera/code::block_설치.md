# code::block 설치
우분투의 경우에는 20.04 기준
```
sudo apt install codeblocks
```
무난하게 잘 설치가 된다 , debian에서도 잘 설치된다. 


## 기존 프로젝트 열기 - New 프로젝트
주로 vscode를 사용하지만 싱글보드컴퓨터에서 사용할려고 하면 메모리를 많이 사용한다. 
vscode를 사용하면 편하지만 총 2G 짜리의 메모리에 약 400~500Mb는 사용하는 것 같다. 이게 엄청 크다.   
그래서 catkin build까지 사용해서 빌드를 하면 싱글보드컴이 뻗어 버리기도 한다

code::block IDE 같은 경우는 약 100mb 정도 메모리를 사용하고, 빠르므로 간단한 수정에는 좋을 듯해서 
사용하기로 결정했다. 물론 단점은 C/C++ 위주로 지원이 된다는 것?

### New 프로젝트 
프로젝트 통째로 열기가 참 힘들다. 프로젝트를 새로 만들때는 상관이 없겠지만   
기존에 존재하는 프로젝트를 열려면(Code::blocks로 작업했던 것이 아니라면)  
vscode 처럼 디렉토리 째 열 수 있는 것은 아니다.  

그래서 new 프로젝트를 해야한다. 메뉴 New -> Project 를 누르고, Empty 프로젝트로 선택/ 만들어준다   
start 화면에서 Create a new project를 클릭  

기존의 프로젝트 이름과 동일하게 Project title을 지정. 그리고 해당 디렉토리를 지정해준다  
이제 *마지막칸의 Resulting filename*에서 보면 해당 프로젝트안에 또 같은 이름으로 디렉토리가 생기므로  
최종 경로를 확인하여 하위로 다시 또 생성되는 않게 해줘야한다 (하나 지워준다)

예, servo_ros 라는 패키지를 열려고 했던 것인데 그 안에 경로를 또 생성한다. 그래서 **기존 프로젝트의 root에 생성**이 되게 해주자
```
/my_work/servo_ros/servo_ros/servo_ros.cbp
# 이것을 아래 처럼
/my_work/servo_ros/servo_ros.cbp
```

그 다음 컴파일러를 선택해주는데, Debug, Release 관련해서 2개의 디렉토리가 생기는데 이거는 그냥 감안하고  
만들어준다. 최소 1개는 선택해야한다  

> 어차피 catkin을 사용할 것이기 때문에 여기서 빌드는 안 할 것이기 때문에 최소 Debug만 선택해줌   
> 그리고 혹시 프로젝트에 생기는  bin/Debug, obj/Debug 는 gitignore 시켜버린다  

### file 추가
완료가 되면 프로젝트가 만들어지는데.. 파일이 하나도 안 보인다   
Project 메뉴를 누르고 *Add file recursively* 를 눌러준다.   
그러면 해당 디렉토리가 뜨는데 Open으로 열어준 뒤에 Select All을 눌러서 다 인식할 수 있게 해주자

이제 왼쪽 Projects 패널에서 해당 프로젝트를 누르면 Sources, Headers 등에서 볼 수가 있다

> IDE 특성상, 카테고리화 되서 보여지는데, vscode 처럼 그냥 직관적으로 모든 파일이 보이는 형태는 아니지만   
> IDE 들이 좀 그런 것 같다. 암튼 새로운 Sources, Headers 같은 디렉토리가 실제 생긴 것은 아니므로   
> 실제로는 cbp 파일이 한개 만들어진다. 고로 프로젝트에 영향을 미치지는 않는다  


## 파일 추가
New -> file 파일로 선택하면 Empty file을 cpp로 만들 수 있다   
해당 파일은 src 디렉토리에 만들어 주는 것이 좋다.  

파일명 변경 등은 파일이 열려있는 상태에서는 안됨. 

## 빌드 
cpp파일은 src 디렉토리에 만들어서 넣어주는 것이 좋다.   
아니라면 Project 메뉴의 -> Properties 을 설정을 열어서   
Build targets 에서 Build target files를 선택해줄 수 있는데 변경하기 조금 까다로운 듯 하다   

> 그래서 애초에 cpp 파일은 src 디렉토리에 만들어주고, header 파일은 include 디렉토리에 넣어주는 것 좋다
