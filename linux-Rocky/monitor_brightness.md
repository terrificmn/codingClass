# monitor 밝기
모니터를 소프트웨어로 컨트롤 할 수 있는데, 마치 노트북에서 밝기 조절이 되듯 가능하다.  

DDC/CI protocol 이 모니터의 하드웨어의 brighness control 을 할 수 있게 해주는데,  

ddcutil 이 모니터의 DDC/CI 를 사용해서 모니터(하드웨어) 통신을 해서 밝기 조절 가능  

일단 GNOME 모니터 용은 (Wayland 에서도 잘 작동)  
```
sudo dnf install ddcutil
```

그리고 GNOME extensions store 에서 
https://extensions.gnome.org/extension/7308/displays-adjustments/

아마도 위의 사이트를 가게 되면 GNOME extensions 를 위한 GNOME shell integration 를 먼저 설치해준다.  
> firefox 기준으로  쉽게 extension이 설치된다.  
그리고 On 을 해주면 다운로드 / 설치를 해준다. 

좀 더 디테일한 extensions 도 있음 (참고)    
~~https://extensions.gnome.org/extension/2645/brightness-control-using-ddcutil/~~  
좀 더 디테일한 설정을 제공하지만 단, 내 모니터랑은 잘 안 맞는 듯 하다. 잘 안됨


## ic2 그룹 추가 
GNOME extensions 에서 ddcutil 사용할 때 퍼미션 에러 때문이라고 보면 된다.  

monitor 의 하드웨어 채널은 i2c 를 사용하는데 권한이 필요하다. 

그룹을 만들어 준다 .
```
sudo groupadd --system i2c
```

유저를 해당 그룹에 포함 시켜준다. 
```
sudo usermod -aG $USER i2c
```

Linux 에서는 DDC 를 i2c-dev 모듈로 통신하므로 load가 될 수 있게 해준다. 
```
sudo sh -c 'echo i2c-dev >> /etc/modules-load.d/i2c.conf'
```
> echo 자체는 퍼미션 때문에 실행이 안되는데 sh -c 를 이용하면 echo 가 잘 먹힘,  
i2c.conf 는 조금 의심되는게 있어도 또는 없어도 크게 상관이 없는 듯 하다. 일단 해줌 ㅋ

udevrule 도 포함 시킬 수 있으나, 이것도 생략했다. 안해도 일단 크게 문제는 없다.  
참고:  
`sudo sh -c 'echo \'KERNEL=="i2c-[0-9]*", GROUP="i2c", MODE="0660"\' > /etc/udev/rules.d/45-ddcutil-i2c.rules'`


재부팅을 하게 되면 gnome 어쩌구 저쩌구 하면서 ddcutil-service 를 설치해야 한다고 나오면서  
extensions failed 했다고 나온다.  
일단 공식 dnf 에서는 해당 패키지를 설치가 기본 제공 되지 않음

빌드를 따로 해준다.

```
sudo dnf install make gcc ddcutil libddcutil-devel glib2-devel
```

클론 / 빌드 및 설치
```
cd ~/third_parties
# Clone the repository
git clone --branch v1.0.14 https://github.com/digitaltrails/ddcutil-service.git

# Move into the folder
cd ddcutil-service

# Compile and install the service
make
make install
```
크게 문제 빌드 및 설치가 완료 된다. 

다시 재부팅을 해주면 셋팅을 진입하기 위해서 오른쪽 상단에 마우스를 가져다 놓으면   
노트북 처럼 슬라이드 2개가 나타나고, 밝기 조절을 할 수 있다. 

## 테스트  
터미널에서 `ddcutil detect` 를 해보면  

모니터 리스트가 나옴, 내 모니터는 한개는 지원이 안됨







