## humble-desktop
osrf/ros:humble-desktop 를 사용하는 경우에는 apt 키등을 등록할 필요가 없고,   
apt install 로 ros-humble-desktop 도 필요가 없다   

### rosdep
rosdep update 하려면 `apt update` 부터 해준다

```
sudo apt update
rosdep update
```

rosdep install 할 경우에는 --rosdistro 옵션을 잘 선택해준다   
humble 일 경우에는 --rosdistro $ROS_DISTRO   
라고 하거나 아예 humble 이라고 하드코딩 해준다 


### gui 관련 프로그램 띄울 때
```
ALSA lib pcm_dmix.c:1032:(snd_pcm_dmix_open) unable to open slave
AL lib: (EE) ALCplaybackAlsa_open: Could not open playback device 'default': Device or resource busy
```

일단 정확히는 모르겠지만 HDMI, audio hardware 와 관련된 사항인듯한데..  
일단 gazebo, rviz2 등 gui 프로그램을 실행시키는 것은 잘 된다 


공식 ros 도커 이미지를 사용하면서, 
기존 nvidia 용으로 사용했던 nvidia/cudagl:11.3.0-devel 도 설치를 해봤지만   
차이는 없었고, 아마도 nvidia-docker2 를 설치해서 되는 것일지도 모르겠다   

> 일단 nvidia 이미지는 ubuntu 22.04 버전이 아직 없는 듯   

왜냐하면 docker-compose.yml 파일의 runtime: nvidia을 빼버리면 아예 GUI 프로그램 실행할 때   
검은 화면으로 열리는 현상이 있음

일단 nvidia를 사용하면 nvidia-docker2는 설치를 해야한다




