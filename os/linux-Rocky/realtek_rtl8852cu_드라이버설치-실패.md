# rtl8852cu 설치하기
Fenvi AXE5400  
lsusb 하기

ID 0bda:c832 이면 rtl8852cu 

일단 페도라42 에서는 실패했다.  아래는 일단 참고만 하자.  

## 트러블슈팅
realtek 드라이버를 설치하기 위해서는 dkms kernel-devel 을 먼저 설치를 해야하는데  
이때 kernel-devel 만 설치를 하면 다른 의존성을 지워버려서   
kennel-devel 설치시에 kernel-modules 이 삭제 되어서   
재부팅 시 해상도가 800 x 600 에 고정되어 버리는 현상이 발생  

```
rpm -qa | grep kernel | sort
```

abrt-addon-kerneloops-2.17.8-1.fc42.x86_64 kernel-6.17.13-200.fc42.x86_64 kernel-6.18.5-100.fc42.x86_64 kernel-core-6.17.13-200.fc42.x86_64 kernel-core-6.18.5-100.fc42.x86_64 kernel-core-6.18.6-100.fc42.x86_64 kernel-devel-6.18.6-100.fc42.x86_64 kernel-devel-matched-6.18.6-100.fc42.x86_64 kernel-headers-6.18.3-100.fc42.x86_64 kernel-modules-6.17.13-200.fc42.x86_64 kernel-modules-6.18.5-100.fc42.x86_64 kernel-modules-core-6.17.13-200.fc42.x86_64 kernel-modules-core-6.18.5-100.fc42.x86_64 kernel-modules-core-6.18.6-100.fc42.x86_64 kernel-modules-extra-6.17.13-200.fc42.x86_64 kernel-modules-extra-6.18.5-100.fc42.x86_64 kernel-tools-6.18.5-100.fc42.x86_64 kernel-tools-libs-6.18.5-100.fc42.x86_64 libreport-plugin-kerneloops-2.17.15-5.fc42.x86_64

6.18.6-100.fc42.x86_64 인데  
kernel-modules-6.18.6-100.fc42.x86_64
kernel-modules-extra-6.18.6-100.fc42.x86_64 없음

older 버전 6.18.5-100 , 6.17.13-200 만 있음  
그래서 modprobe amdgpu → Module not found 이 없어서 해상도가 날라감  

그래서 다시 재설치  

```
sudo dnf install -y \
  kernel-modules-6.18.6-100.fc42.x86_64 \
  kernel-modules-extra-6.18.6-100.fc42.x86_64
```
이후 재부팅하면 해상도가 다시 돌아온다.



## install 참고  
의존성 설치 - kernel-devel 설치시에 아래처럼 하면 확실하고  
빨간색으로 삭제가 되는게 있으면 꼭 챙기자. 
> 지워진다는 로그를 보았으나 그냥 넘어갔더니 문제가 발생  

```
sudo dnf install \
  dkms \
  git \
  gcc \
  make \
  elfutils-libelf-devel \
  kernel-devel-$(uname -r)
```

https://github.com/morrownr/rtl8852cu-20240510  
클론 디렉토리로 이동 후

설치 `sudo ./install-driver.sh`

일단 와이파이는 생성이 되나 비번을 눌러서 접근을 할 수가 없다. 일단은 실패


