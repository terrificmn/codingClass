# NVIDIA Container Toolkit
먼저 도커를 설치가 다 된 후에  

[링크 참고 https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#setting-up-nvidia-container-toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#setting-up-nvidia-container-toolkit)

을 설치해준다  

Requirements  
- NVIDIA Driver 
- GNU/Linux x86_64 with kernel version > 3.10  
- Docker >= 19.03 (recommended, but some distributions may include older versions of Docker. The minimum supported version is 1.12)   
- NVIDIA GPU with Architecture >= Kepler (or compute capability 3.0)  
- NVIDIA Linux drivers >= 41  


## 우분투 
먼저 각 리눅스 distribution에 맞는 엔진을 설치해주기  

아래는 우분투 docker 스크립트 다운 / 도커를 설치했다면 스킵 가능할 듯 하다
```
curl https://get.docker.com | sh \
  && sudo systemctl --now enable docker
```

repository GPG key setup  
```
distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
      && curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
      && curl -s -L https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.list | \
            sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
            sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

인스톨 nvidia-docker2 package   

sudo apt-get update

sudo apt-get install -y nvidia-docker2

sudo systemctl restart docker

sudo docker run --rm --gpus all nvidia/cuda:11.0.3-base-ubuntu20.04 nvidia-smi



CentOS 관련은 위 링크로 참고할 것


