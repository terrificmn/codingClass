# rtc
2032 배터리와 2핀 짜리 헤더에 배터리 연결한 이후에 재부팅 할 것

일단 tinker board에 맞는 것은 3v 짜리이면 되고 CR2032 건전지로 되어 있는 것  
2핀이 연결이 되어있어야 tinker board에 연결할 수가 있는데   
C51021 커넥터가 연결되어 있으면 호환이 된다. (RB타입)   

연결은 메뉴얼 상에 나와 있는것 처럼 +, GND를 맞춰서 연결해 준다 

## rtc 관련 명령어
확인해 볼 것은 
`ls -l /dev/rtc0`

dmesg 확인
```
dmesg | grep rtc
```

> 일반적으로도 보통 컴퓨터에도(리눅스) rtc는 설치가 되어 있는 듯 하다. 

결과 
```
[    3.759189] rk808-rtc rk808-rtc: rtc core: registered rk808-rtc as rtc0
[    4.260641] [drm] Cannot find any crtc or sizes - going 1024x768
[    5.005829] rk808-rtc rk808-rtc: setting system clock to 2023-06-10 09:25:23 UTC (1686389123)
```

필요 패키지
```
sudo apt install i2c-tools
```
이미 설치되어 있음


rtc 디텍팅을 한다고 하는데 정확히는 무슨 기능인지 잘 모르겠음;;  
```
sudo i2cdetect -y 0
```

현재 rtc에 설정된 시간 읽기
```
sudo hwclock -r -f /dev/rtc0
```

> sudo 안하면 명령어 자체를 인식 못 함

이를 활용해서 프로그램을 짜서 해도 되는데 시간을 확인해서 시스템 종료까지 할 수 있게 했지만  
구지 필요가 없을 듯 하다


## 예약 하기
/sys/class/rtc/rtc0/wakealarm 파일을 이용해서 예약을 할 수가 있다  

이를 shell 스크립트를 등록해서 언제 켜질지 예약을 걸 수가 있다   
그리고 시스템을 종료하게 만들어 준다. 이 스크립트 파일을 crontab 에서 매일 실행하게  
해준다. 그러면 종료 및 시스템 wake up 및 부팅을 하게 할 수가 있다  

예약 확인
```
cat /sys/class/rtc/rtc0/wakealarm
```

아무 숫자가 안나오면 예약이 없는 것

알람 셋팅하기.
```
sudo sh -c "echo 0 > /sys/class/rtc/rtc0/wakealarm" 
sudo sh -c "echo `date '+%s' -d '+ 3 minutes'` > /sys/class/rtc/rtc0/wakealarm"
```
먼저 0을 넣어주고 (초기화 인듯?)  
3 분후에 켜지게 설정을 해준다 (3 minutes 에서 원하는 분 단위로 등록해주면 된다)   

이제 시스템을 바로 종료해보자. 물론 위의 cat 명령어로 확인해보면 숫자가 출력되는 UTC 시간으로 나온는 결과 임

시스템 종류 후 약 3분 뒤에 다시 켜지는 것을 확인한다면 잘 작동하는 것

이를 스크립트를 이용해서 만들어주고, 예약 및 시스템 종료 로 만들어준다   
`crontab -e` 명령어를 사용해서 등록을 해주면 하루에 한번씩 특정 시간에 실행이 되면서 예약을 하게 된다.   

> 자세한 스크립트는 rtc패키지 만들어 놓은 것 참고하기  


## 스크립트로 rtc 
먼저 sh 스크립트를 만들어준다. cpp를 통해서 만들 수도 있으나, sh 스크립트가 편한 것 같다   

```sh
sudo sh -c "echo 0 > /sys/class/rtc/rtc0/wakealarm"
sudo sh -c "echo `date '+%s' -d '+ 720 minutes'` > /sys/class/rtc/rtc0/wakealarm"
echo "if UTC time (below the line) is displayed, then wake_alarm set ok"
cat /sys/class/rtc/rtc0/wakealarm
sudo sh -c "shutdown -h 1"
```

위의 셀 스크립트 파일명을 shutdown_test.sh 라고 만들었다면  
```sh
sh shutdown_test.sh
```   
로 실행을 하면 된다   

첫줄은 /sys/class/rtc/rtc0/wakealarm 파일을 만들기 위해서 시작  0 으로 만들어준다   
그리고 두 번째에는 몇 분 후에 다시 켜질 지를 설정한다. 마지막줄에서는 시스템을 종료하게 된다. 3분 뒤에 꺼진다  

> 4번째는 사실 출력되는 것을 보기 위한 것인데, 테스트 할 때에는 2~3분 정도로 테스트 하고 출력이 잘 되는지 확인   
0 이 아닌 utc 타임이 나오면 설정은 잘 된 것이다. 시스템을 1분 후에 종료하게 했으므로 출력 확인 후   
1 분뒤에 종료되는 것 확인 후 이어 3분(꺼진 뒤 2분)에 시스템이 다시 켜지는 지 확인하면 된다   


### crontab 정리
이제 잘 되는 것을 확인 했으면 위의 sh 스크립트를 자동으로 실행 해주게 만들어주면 된다   

`cat /etc/crontab`

맨 아래 있는 형식에 주목
```
SHELL=/bin/bash
PATH=/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=root

# For details see man 4 crontabs

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name  command to be executed
```

위의 맨 아래에 나와 있는 `# *  *  *  *  * user-name  command to be executed` 이 부분을 보면 
이런 형식이 된다  m h dom mon dow command   
예 
```
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
```

시스템을 종료하기 위한 sh 스크립트 실행 시키기(rtc 포함)    
아래와 같은 형식을 만든다면   
```
0 21 * * * myuser /usr/local/bin/shutdown_test.sh
```
매일 21:00 에 실행을 하게 된다.

이제 셀트크립 파일을 /usr/local/bin/ 에 복사 또는 심링크를 해준다   
```
sudo ln -s /usr/local/bin/shutdown_test.sh ~/Documents/shutdown_test.sh
```

이제 crontab -e 명령을 사용해서 명령을 등록한다   




crontab -e  >>> register
crontab -l   >>> view the list



그리고 이 파일이 매 시간에 실행될 수 있게 crontab 으로 등록해준다  
그러면 rtc로 예약을 한 이후에 시스템 종료를 한다

이후 정리 다시 업데이트하기!!!!







crontab 정리하기 - 참고 

ssl_설치_셋팅_일반(도커아닌경우).md 여기도 참고



