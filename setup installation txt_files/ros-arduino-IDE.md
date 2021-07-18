# 아두이노
rosserial libraries 를 사용하려면 rosserial-arduino 패키지를 설치한 후 
ROS에서 IDE를 이용해서 바로 사용이 가능하다

먼저 설치
```
sudo apt-get install ros-indigo-rosserial-arduino
sudo apt-get install ros-indigo-rosserial
```

그리고 ros_lib를 설치
먼저 아두이노 IDE인 스케치북을 다운받는다. 
[다운로드](https://www.arduino.cc/en/software)

Linux 64bit에 맞춰서 다운로드를 하면 압축파일 tar
arduino-1.8.15-linux64.tar.xz 를 다운받게 되고 압축을 풀어준다

```
tar xvf arduino-1.8.15-linux64.tar.xz
```
이제 압축이 풀어진 곳으로 이동하는데 libraries 까지 이동 
```
cd arduino-1.8.15
```

install.sh 파일이 있다 실행을 해주자
```
sudo ./intall.sh
```

이제 아두이노 IDE에서 ros_lib를 설치할 수 있음
스케치북을 실행을 해주자. Arduino IDE로 찾을 수 있음

메뉴는 Sketch > Include Library > Manage Library 를 누르면 새 창이 뜬다
여기에서 rosserial를 검색을 해준다

검색이 되었으면 install 버튼을 눌러서 설치를 해준다

이제 Sketch > Include Library 에서 보면
Rosserial Arduino Library가 추가가 되어 있고

File메뉴의 Examples를 통해서 코드를 볼 수가 있음


[참고 사이트](http://wiki.ros.org/rosserial_arduino/Tutorials/Arduino%20IDE%20Setup)

아두이노를 usb로 연결한 후에 터미널에 device를 검색해보면
```
$ ls -l /dev/ttyUSB*
```

```
crw-rw----. 1 root dialout 188, 0 Jul 19 05:27 /dev/ttyUSB0
```
위 처럼 나온다

그러면 유저(현재 로그인한 계정)를 dialout이라는 그룹에 추가해주자 (dialout은 파일의 그룹 소유자임)
```
$ sudo usermod -aG dialout $USER
```
환경변수 $USER를 사용해도 되고 본인의 아이디를 넣어줘도 된다. 

터미널에 id라고 입력하면
```
id
```

```
uid=1000(octa) gid=1000(octa) groups=1000(octa),10(wheel),971(docker)
```
이런식으로 나오게 되는데 이제 로그아웃을 해야지 제대로 반영이 된다.
로그아웃 로그인을 해서 이제 다시 id를 쳐보면

```
uid=1000(octa) gid=1000(octa) groups=1000(octa),10(wheel),18(dialout),971(docker) 
```
dialout 그룹이 추가된 것을 알 수 있다

이제 아두이노를 usb에 연결한 후 serial통신으로 사용할 수 있다

[참고 블로그 및 예제코드](https://maker.pro/arduino/tutorial/how-to-use-arduino-with-robot-operating-system-ros)