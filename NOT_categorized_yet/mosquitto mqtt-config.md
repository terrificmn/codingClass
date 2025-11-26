# mosquitto mqtt
apt 로 설치  
``` 
sudo apt install mosquitto
```

`sudo systemctl start mosquitto` 으로 실행  
> 원할시 enable 도 실행

이렇게 하면 mqtt client 에서 사용할 경우에  
localhost 로 접근하면 크게 문제 없이 사용할 수가 있다. (기본 설정)

## 외부에서 접속할 시
일단 외부에서 접속할 수 없을 경우에는  
anonymous 와 ip 및 port를 확인해본다.  
보통 방화벽은 아예 설정 안하면 열려 있어서 크게 문제가 없는 듯 하다.  

외부에서 mqtt 브로커 아이피 및 포트 확인하기
```
nmap 192.168.10.111 -p 1883
```
host가 up 및 state 가 open 인지 확인
```
Nmap scan report for 192.168.10.111 
Host is up (0.0032s latency).

PORT     STATE SERVICE
1883/tcp open  mqtt
```

/etc/mosquitto/ 안에서 확인할 수가 있다.

custom 파일을 만들어서 사용해준다. 

listener 1883 0.0.0.0
외부에서 연결할 수 있게 ip 설정
> to listen on all network interfaces

anonymous 설정도 커스텀 파일을 만든 후에 관리

anonymous true 로 해주면된다 

anonymous false 로 사용할 시에는 
anonymous false
패스워드 파일을 설정한다.  

mosquitto.conf
```
# =================================================================
# LISTENER CONFIGURATION
# Binds the listener to all network interfaces (0.0.0.0) on port 1883 (standard MQTT port).
# This is required for the broker to accept connections from *other* machines on the network.
# =================================================================
listener 1883 0.0.0.0

# =================================================================
# AUTHENTICATION CONFIGURATION
# Enables anonymous (unauthenticated) client connections.
# NOTE: This setting is ONLY recommended for isolated/test environments.
# =================================================================
allow_anonymous true

# =================================================================
# OTHER RECOMMENDED SETTINGS
# Set the user Mosquitto runs as after startup (improves security).
# This user must exist on your system and have read/write access to necessary files/folders.
# You may need to comment this out if running in a container or on a non-standard OS.
# =================================================================
# user mosquitto

# =================================================================
# OPTIONAL: PERSISTENCE (Saves messages/subscriptions across restarts)
# =================================================================
# persistence true
# persistence_location /var/lib/mosquitto/
```



## 패스워드 설정시에는 
```
# For Production/Secure environments:
listener 1883 0.0.0.0
allow_anonymous false
password_file /etc/mosquitto/passwd
```


세이브하기, 디렉토리 위치 확인, 아마도 /etc/mosquitto 쯤
```
mosquitto -c /path/to/your/mosquitto.conf
```

`sudo systemctl restart mosquitto`


