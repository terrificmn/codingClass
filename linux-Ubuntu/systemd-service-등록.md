# systemd service 등록
rc.local 스크립트를 실행하는  rc-local.service 를 주로 사용해왔지만   
service를 직접 등록해서 스크립트를 실행할 수 있는, 즉 시작 프로그램 등록을 시도

일단 `/etc/systemd/system` 이하에 파일을 만들어 주면 된다.   
> my-startup.service 이런식으로 만들어 줄 수가 있다.  

```
sudo vi /etc/systemd/system/my-startup.service
```

이후 권한은 640 정도 바꿔준다. 그룹까지만 권한을 주고 other는 빼버린다. 


파일의 내용은 아래와 같다.
```sh
[Unit]
Description=my-start up
Wants=network-online.target
Requires=network.target
After=syslog.target network-online.target

[Service]
Type=forking
ExecStart=/usr/local/bin/my_startup_sh
PIDFile=/var/run/my_startup.pid
Restart=on-failure
RestartSec=10
KillMode=process
User=myuser
StandardOutput=tty

[Install]
WantedBy=multi-user.target                         
```

> network-online 타겟으로 했을 때 ping도 되고 ip도 되는 상태였지만 내부 네트워크 트러블이 있었는데   
**syslog.target** 을 추가한 이후에 그러한 문제가 해결 되었다.  
물론 user가 root가 아닌 원래 사용하던 유저로 했던 것도 있지만 어떤 것 때문에 해결되었는지 확실하지 않다.    

~~추후 좀 더 테스트 필요~~
user / root 때문에 네트워크 프로그램이 발생한 것은 아니였다. 

단, user로 구성해도 문제는 발생하지 않으나, 파워off 등을 할 때 권한 때문에 shutdown이 안 되는 경우가 있는 듯 하다.   


### 구성
대충 rc-local.service 등록하는 것과 거의 비슷하다.   
[Unit], [Service], [Install] 로 구성  


#### Unit
Unit에서 Wants 는 꼭 그렇게 되는 것은 아니고 말 그대로 원하는 target 이라고 볼 수 있고   
중요한 것은 
After 이다. 측정 서비스나 network-online 된 후에 실행이 되게 되므로   
위의 스크립트는 네트워크 가능해진 이후 실행된다.  

정확히는 network 장치들이 준비가 되고 ip address 등이 할당 된 후이다.  
만약 network 할당 전에 실행하고 싶을 때에는  `Atfer=network-pre.target` 으로 해주면 된다.   

> After=systemd-user-sessions.service   
위 처럼 특정 sessions 이후 실행하게 할 수도 있다.   
테스트 필요 user-sessions 가 로그인 이후를 말하는 것인지 아닌지 잘 모르겠음   

#### Service
Type 은 simple 과 forking등이 있고. 단순히 생각하면 simple는 foreground, forking는 background 로 볼 수 있음  

Restart 옵션으로 fail 일 경우 다시 수행하게 할 수 있다.

KillMode 를 process로 하면  systemctl 로 stop를 했을 때 service를 중지할 수 있게 해준다.  
main process만 죽이고, 만약 복잡한 스크립트가 수행이 되어서 여러 spawned processes 까지 중지하려면   
*mixed*"로 해준다.

User는 생략하면 root로 실행이 되는 듯 하고, 특정 user를 넣어주면 특정 user로 실행을 한다.   
재부팅 테스트 시, 특정 스크립트를 유저의 home디렉토리안에 만들어주게 했는데 테스트 결과 User로 등록한  
PIDFile 은 지정한 경로에 pid 넘버를 생성해준다.   


ExecStart 는 특정 쉘 스크립트를 실행하게 해준다.   
rc-lcoal.service 에서 rc.local 파일을 지정한 것과 같다.   
파일은 실행가능하게 744 가 되거나 chmod +x 로 권한을 지정해줘야한다.

여기에 추가로 파라미터를 넣어서 지정할 수도 있다.    
[밑에서 좀 더 ExecStart 관련 참고하기](#execstart-구성-하기)


#### Install
WantedBy 는 multi-user.target

해당 서비스가 system이 멀티 유저가 로그인 할 수 있는 상태가 되면 시작 될 수 있는 것을 의미
either cli or graphical user interface



### ExecStart 구성 하기

ExecStart=/path/to/shell_script start
ExecStop=/path/to/shell_script stop
ExecRestart=/path/to/shell_script restart

위에 처럼 지정한 후에 해당 쉡 스크립트 뒤에 있는 argument로 받아서 사용할 수 있게 되어 있다.   
> 쉡스크립트에서 파라미터 받을 수 있게 코딩  
하지만 한편으로는 start 자체는 기본 옵션이고, stop도 가능하지 구지 필요할지는 모르겠다   

///TODO:   
추후 테스트 필요
 


