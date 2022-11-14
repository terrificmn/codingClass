기존에 Tinker Board S 버전에는서는 라이브러리를 받아서 직접 빌드를 해야했던 것 같다   

[gpio 관련 라이브러리 안내 사이트, 라이브러리 사용법 등을 알 수 있다](http://serverbiz.co.kr/product-info/?vid=77)

하지만 **Tinker Board 2/S2** 에서는 이미 설치가 되어 있다. 
예를 들어 터미널에 `gpio readall` 을 쳐보면 gpio관련 핀 정보를 보여준다   
**그러므로 따로 빌드 하지말자!!(팅커보드 2/2s인 경우)**

아무튼 설치를 해야하는 줄 알고 위의 사이트를 참고해서 깃 클론 후 빌드를 했다가 오히려 빌드가 에러가 발생하면서   
되던 `gpio readall` 도 실행이 안되는 현상이 발생   
알고 봤더니 팅커보드 S 버전 내용이었다. 그래서 아예 buster10 을 다시 설치함;;;

설치는 /usr/local/share/gpio_lib_c_rk3399/examples 경로에 되어 있고   
WiringPi.h 파일도 바로 include가 가능하다. 

> 여기서 말하는 것은 C 라이브러리임. python은 잘 모르겠으나.. 확인을 아직 못해봄   


[유투브 ROS와 WiringPi 사용하는 유투브](https://youtube.com/watch?v=pSlrGDhdLkQ)


