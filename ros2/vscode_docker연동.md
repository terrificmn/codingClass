# VScode에서 docker로 연동하기

[update필요...]

기존에 docker-compose에서 연동시켜 놓았던 컨테이너 안의 워크 스테이션과 
로컬안에서 접근할 수 있게 해놓아서 사용을 했었는데

로컬에서 패키지 파일들을 수정하고 했으나, Lint 기능등은 그냥 포기하고 했었는데 
일단 로컬에서 ros2 자체가 없으니 그냥 그러려니 했는데   
따로 환경 설정해서 법이 있었음

하지만 그 방법은 나중에 다시 알아보기로 하고.. 실패함 ㅋㅋㅋ

일단 컨테이너를 실행시킨 상태에서 docker exec 명령어로 컨테이너로 들어가서 하는 방법을 자주 사용하는데

일단 vscode를 실행해서 remote 기능을 활성화..

먼저 extensions 탭에서 Remote Development 검색/설치를 한 후  
왼쪽에 Remote Explorer 가 생기는데 여기에서 클릭 후 검색되는 container에서 
예를 들어 docker-ros 컨테이너가 보인다면 + 아이콘을 눌러서 Attach to Container를 눌러준다   
그러면 vscode가 열리면 컨테이너에 접속하면서 새로 열린다   

include 정도만 손 봐주면 ros/ros.h 정도는 잘 불러와준다  

> attach to container를 하기전에 docker container를 실행을 해줘야 한다   


## ctrl+shift+p 로 검색
attach로 검색하면  
`Dev Container: Attach to Running Container` 가 나오는데 클릭 후   
실행되고 있는 docker container를 선택해주면 된다   




스샷
스샷 필요







