.devcontainer 디렉토리를 만들고 devcontainer.json 파일을 설정해서 하는 방법은
몇개 소개가 되고 있는데.. 잘 안된다~

그래서 그냥 기존에 사용하고 있는 도커 컨테이너에 접속해서 하는 방법으로 시도했다

VScode를 실행 시킨 후에 왼쪽 하단에 있는 버튼을 클릭하거나
Ctrl + Shift + p 를 눌러서 

Attach to running container 를 선택해서 눌러주면 지금 실행되고 있는 컨테이너가 나오는데
실행되고 있는 도커 컨테이너를 선택해주고 실행해주면 열린다



/ 바로 이하 경로에 ros_entrypoint.sh 셸 스크립트로 도커 시작할 수 있는지 확인해볼 것 
추후 
```bash
#!/bin/bash
set -e

# setup ros2 environment
source "/opt/ros/$ROS_DISTRO/setup.bash"
exec "$@"
```