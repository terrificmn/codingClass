기존에 Tinker Board S 버전에는서는 라이브러리를 받아서 직접 빌드를 해야했던 것 같다    
하지만 **Tinker Board 2/S2** 에서는 이미 설치가 되어 있다. 
그러므로 2버전에는 **빌드가 필요없다 (팅커보드 2/2s인 경우)**

[gpio 관련 라이브러리 안내 사이트, 라이브러리 사용법 등을 알 수 있다](http://serverbiz.co.kr/product-info/?vid=77)

예를 들어 터미널에 `gpio readall` 을 쳐보면 gpio관련 핀 정보를 보여준다   

참고로...  
https://github.com/TinkerBoard/gpio_lib_c 여기에 있는 라이브러리는 2/2s와는 호환이 안되는 듯 하다  

### 실패 
먼저 gpio readall 을 했을 때 나오는 데이터에서 gpio 핀들의 Physical 번호는 같으나,   
Mode, Name, CPU(핀번호)등이 조금씩 다르게 되어 있는 듯 하다      
아무튼 설치를 해야하는 줄 알고 위의 사이트를 참고해서 깃 클론 후 빌드를 했다가 오히려 빌드가 에러가 발생하면서   
되던 `gpio readall` 도 실행이 안되는 현상이 발생   
알고 봤더니 팅커보드 S 버전 내용이었다. 그래서 아예 buster10 을 다시 설치함;;;

설치는 /usr/local/share/gpio_lib_c_rk3399/examples 경로에 되어 있고   
WiringPi.h 파일도 바로 include가 가능하다. 

> 여기서 말하는 것은 C 라이브러리임. python은 잘 모르겠으나.. 확인을 아직 못해봄   

[유투브 ROS와 WiringPi 사용하는 유투브](https://youtube.com/watch?v=pSlrGDhdLkQ)


