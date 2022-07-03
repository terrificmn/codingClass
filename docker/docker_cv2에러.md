importError 가 날때
libGL.so.1: cannot open shared object file: No such file or directory

Dockerfile 에 추가
```
RUN apt-get update && yes | apt-get upgrade
RUN apt-get install -y python3-opencv libgl1-mesa-glx
```
일단 apt-get update가 먼저 되어야지 python3-opencv 설치가 가능

requirements.txt 파일에 추가하기
opencv-python-headless 로  pip install 시키기


