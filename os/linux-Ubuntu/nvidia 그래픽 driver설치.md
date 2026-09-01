nvidia 공식 홈에서 다운로드를 받아서 설치를 할 수도 있고  
예를 들어 Nvidia-Linux-x86_64-515.57.run 파일인데   
바로 실행을 해주면 된다   

하지만 가끔식 듀얼 모니터가 해제되고 한개만 인식하는 현상이 발생해서  
다시 설치를 하다가, (그냥 다시 새로 설치하면 잘 인식됨)

package를 이용해서 그냥 설치할 수있는 방법이 있다고 인스톨 과정에서 안내를 함  
그래서 찾아봄  

```
ubuntu-drivers devices
```

결과가 나오는데..
```
vendor   : NVIDIA Corporation
driver   : nvidia-driver-515-server - distro non-free
driver   : nvidia-driver-510-server - distro non-free
driver   : nvidia-driver-515 - distro non-free recommended
driver   : nvidia-driver-470-server - distro non-free
driver   : nvidia-driver-470 - distro non-free
driver   : nvidia-driver-510 - distro non-free
driver   : xserver-xorg-video-nouveau - distro free builtin
```
이런식으로 결과가 나오는데 recommended 되어있는 515버전을 설치

```
sudo apt install nvidia-driver-515
```

설치가 다 된 후 재부팅하면 듀얼 인식 잘 됨

