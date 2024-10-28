# msi fedora 설치
msi thin GF63 12UCX-i5
geforce RTX 2050
12gen Intel Core i5-12459H

> 참고로 윈도우 드라이버는 12UCX 버전이 아직 없는 듯 하다. Dec2023 기준, 아마도 2023? 최신이라서? msi 공식 사이트에 Thin GF63 12UCX-484US 버전이 있는데 일단 cpu, 그래픽 카드 등이 동일한 듯 하다. 테스트 필요   


먼저 그래픽 드라이버는 nvidia 사이트에서 구할 수 있지만 설치가 쉽지 않다. 일단 디펜던시를 다 설치를 해줘도  
결국은 error와 함께 실패 

그래서 fedora에서는 dnf 를 (fedora workstation 38) 이용해서 설치할 수 있다.

일단 nvidia 외장 그래픽일 경우 사용 가능한 듯 하다.

먼저 dnf 업그레이드. 모든 패키지들을 업데이트
```
sudo dnf upgrade
```
중요 dnf upgrade 로 패키지들을 최신화 해준다. 커널도 업데이트 될 듯  


그래픽 카드 어떤 것을 사용할 수 있는지 확인. 터미널에 입력
```
lspci | grep -Ei 'VGA|3D'
```
인텔(내장 그래픽), nvidia 표시된다


### 의존성 패키지 설치
```
sudo dnf install kernel-devel kernel-headers gcc make dkms acpid libglvnd-glx libglvnd-opengl libglvnd-devel pkgconfig
```


### rpm fusion Repositories 설치 및 등록
일단 없이 한번 해보자. 포맷 후 다시 설치를 할 기회가 있었는데 설치는 잘 되었지만   
드라이버 인식되는 것은 실패   

아마도 이유는 1. dnf grade를 생략하고 함.   
어쨋든 아래 repo 를 등록안하고 다시 시도.  
akmod-nvidia 등이 설치된다. 아마도 그 전에 repo가 등록된적이 있었거나, 한 듯 하다.  
```
sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
sudo dnf install https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

패키지 리퍼지토리 캐쉬 업데이트 
```
sudo dnf makecache
```

### Install NVIDIA Driver and CUDA Support
nvidia 드라이버와 CUDA 툴킷 설치
```
sudo dnf install akmod-nvidia xorg-x11-drv-nvidia-cuda
```

> waylands에서 작동이 안되는지는 잘 모르겠다.;; 테스트 필요

이후 리부팅 하면 Nouveau drivers 는 자동으로 비활성 되면서 부팅됨

> 참고로 외장그래픽 상태에서는 fedora 부팅이 진입이 불가능. 부트로더에서 e 를 누른 후에 작업해야함. *처음fedora_설치화면_부팅_nouveau_driver.md* 참고하기



### 참고로 매뉴얼로 설치할 경우
의존성 패키지 설치
```
sudo dnf install kernel-devel kernel-headers gcc make dkms acpid libglvnd-glx libglvnd-opengl libglvnd-devel pkgconfig
```


그리고 사이트에서 Linux 64-bit에 맞는 그래픽 드라이버를 받아준다. 
하지만, 실패 

그래서 위에 방법으로 설치하면 된다. 

### 실패했을 경우
부팅화면 grub 화면에서 이전 커널을 버전을 선택해서 부팅 한 후   
다시 설치를 시도하자
