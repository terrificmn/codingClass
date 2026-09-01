# nvidia tool kit
기존에 nvidia 일부 그래픽 카드에서 `xhost +` 등을 사용하더라도 gui 프로그램을 띄우지 못했을 경우에   
nvidia-docker2 를 사용해서 nvidia 이미지를 사용해서   
runtime 을 nvidia 를 사용해서 nvidia gpu를 사용할 수 있게 할 수 있었는데..

노트북에서 nvidia gtx 2050 를 사용하는데 이럴 경우에는 nvidia-docker2 등을 사용할 필요 없이  
보통 ros 이미지를 사용하는 것이 가능했다.   


## nvidia container toolkit 설치
그냥 ros 이미지를 설치해도 되겠지만, nvidia container toolkit 를 설치하려면   

fedora 경우   

리포지터리 셋팅
```
curl -s -L https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo | \
  sudo tee /etc/yum.repos.d/nvidia-container-toolkit.repo
```

설치
```
sudo dnf install -y nvidia-container-toolkit
```

이후 ros를 사용하는 컨테이너에서 runtime 부분에 nvidia를 사용할 수 있게 해주면 된다.   

> nvidia-docker2 를 사용안하고도 가능하다. (contianer tool kit를 포함하는 듯 하다.)  


fedora 경우에는 docker 설치 이후 **/etc/docker/daemon.json** 파일을 설정해서 메모리가 막 상승하는 것을 막아준다.   

docker_rocky_linux_memory_increasing.md 파일을 참고하자

우분투의 경우에는 마찬가지로 apt 로 설치할 수가 있는데 ..

[여기 다큐먼트 사이트를 참고하자](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#installing-with-yum-or-dnf)

아마 마찬가지로 nvidia-docker2는 설치를 안해도 될 듯하지만 (테스트는 안해봄 - 우분투)


## 참고 nvidia-docker2 fedora에서 설치
위의 방법만 해도 충분히 될 것이라고 생각되나,   
위의 방법이 안될 경우 참고   

우분투는 방법은 다른 파일에서 참고 

먼저 centos8의 리포를 setup해준다. 
```
curl -s -L https://nvidia.github.io/nvidia-docker/centos8/nvidia-docker.repo | sudo tee /etc/yum.repos.d/nvidia-docker.repo
```

이후 
```
sudo dnf install nvidia-docker2
```

