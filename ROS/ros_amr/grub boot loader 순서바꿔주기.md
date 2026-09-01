# grub boot loader 순서 바꾸기
처음 부팅 할 때 나오는 grub 에서 부팅 순서가 지정이 되어 있는데  

예를 들어서 
```
* ubuntu
ubuntu 20.04
ubuntu 20.04 (advanced)
```
여기에서 *에 주목을 해야하는데 * 표시가 있는 것이 기본값으로 설정이 되어 있어서   
지정한 시간이 다 되면 부팅이 되게 되어있다.

만약 이것을 바꿀려면 부팅 순서 디폴트 값을 바꿔주면 되는데  
위의 레이블을 바꾸려면 아래를 참고.....   
어쨋든 순서는 고정이 되어 있고 위에서부터 0, 1, 2 ... 순으로 기억을 하자   

바꿀려고 하는 우분투 버전으로 들어간 다음에 터미널을 열어준다  

## 우분투 선택 하기
우분투 18.04와 20.04 버전이 각각 설치되어 있는 경우에 ubuntu20.04를 먼저 선택이 되게 하려면  

먼저 부팅 순서가 나오게 하고 싶은 버전으로 부팅을 해준다

먼저 백업본을 만들자
```
sudo cp /etc/default/grub /etc/default/grub.bak
```

그리고 파일 열기
```
sudo vi /etc/default/grub
```

GRUB_DEFAULT를 수정하기  
```
GRUB_DEFAULT=0
```

시간을 줄이고 싶으면 변경
```
GRUB_TIMEOUT=1
```

수정이 끝났으면 저장 후 grub update를 해준다
```
sudo update-grub
```
위의 명령어를 수행해야지 /boot/grub/grub.cfg 파일을 업데이트 시켜준다 


## grub의 해당 버전 이름 변경하기
이것도 위의 grub 파일을 수정한다 
```
sudo vi /etc/default/grub
```
> 백업도 해두자

처음 GRUB_DISTRIBUTOR 부분은 주석 처리하거나 지운다
```
# GRUB_DISTRIBUTOR=`lsb_release -i -s 2> /dev/null || echo Debian`
GRUB_DISTRIBUTOR=`{ printf 원하는텍스트 && lsb_release -d -s ; } 2> /dev/null || echo Debian`
```

예를 들면
```
GRUB_DISTRIBUTOR=`{ printf ubuntu20.04:ROS-Noetic && lsb_release -i -s; } 2> /dev/null || echo Debian`
```


또는 
```
GRUB_DISTRIBUTOR=cat /etc/hostname || lsb_release -i -s 2> /dev/null || echo Debian
```
user명으로 대체 

> 처음에 grub 화면에 선택되는 ubuntu 버전의 레이블명이 바뀌어서 나온다 


## 또는 Grub Customizer 프로그램 사용   

```
sudo apt install grub-customizer
```

```
sudo dnf install grub-customizer
```
List configuration 탭에서 순서를 바꿔줄 수도 있고  
General settings 에서 default entry를 지정해 줄 수도 있다  

> 물론 사용, 테스트는 안 해봄;;;