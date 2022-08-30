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
위의 레이아웃을 안 바뀌는 듯 하다. 순서는 고정이 되어 있고 위에서부터 0, 1, 2 ... 순으로 기억을 하자   

바꿀려고 하는 우분투 버전으로 들어간 다음에 터미널을 열어준다  
참고로 첫 번째 ubuntu는 18.04 버전  

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


## grub 이름 변경
처음 GRUB_DISTRIBUTOR 부분은 주석 처리하고 
```
# GRUB_DISTRIBUTOR=`lsb_release -i -s 2> /dev/null || echo Debian`
GRUB_DISTRIBUTOR=`{ printf 원하는텍스트 && lsb_release -d -s ; } 2> /dev/null || echo Debian`
```
또는 

```
GRUB_DISTRIBUTOR=cat /etc/hostname || lsb_release -i -s 2> /dev/null || echo Debian
```
user명으로 대체 

> 이것도 사용/테스트 안 해봄


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