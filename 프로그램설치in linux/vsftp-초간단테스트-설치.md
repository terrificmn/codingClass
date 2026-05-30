# vsftpd 초간단 설정
plain 방식으로 빨리 테스트를 해볼려고 할 경우

설치
```
sudo dnf install vsftpd
```

vsftpd.conf 파일 설정
`/etc/vsftpd/vsftpd.conf`

```
# Disable anonymous users
anonymous_enable=NO

# Allow local system users to log in
local_enable=YES

# Enable file changes (uploading, deleting, etc.)
write_enable=YES

# Lock users to their home directories
chroot_local_user=YES
allow_writeable_chroot=YES
```
> home directories 를 지정해주면 (ftp 서버) 해당 유저의 홈 디렉토리가  root 가 된다.  
더 설정할 수 있지만, 여기에서는 중요하지 않다. 


다른 것은 필요 없다. 

재시작 vsftpd
```
sudo systemctl restart vsftpd
sudo systemctl enable vsftpd
```

nmap 등을 이용해서 테스트를 해보면  
`nmap localhost`
```
PORT      STATE SERVICE
21/tcp    open  ftp
```
포트가 잘 열려 있다.  

systemctl status vsftpd 를 했을 경우에도 문제가 없다면,  
     Active: active (running) 로 나와야 한다. 

서비스가 작동하고, 21 포트는 열려있지만   
방화벽이 막고 있으므로 외부에서 들어올 수가 없다.  

> 확실히 외부에서 테스트하면 접속이 실패한다. 확인!


```
sudo firewall-cmd --permanent --add-port=21/tcp
sudo firewall-cmd --reload
```

이렇게 하면 초간단 빨리 테스트를 해볼 수가 있다. 


테스트 후 방화벽 해제하기
```
sudo firewall-cmd --permanent --remove-service=ftp

sudo firewall-cmd --reload

systemctl stop vsftpd.service 
```




