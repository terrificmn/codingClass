## fail2ban 설치
CentOS / RHEL 계열

Web server nginx, apache 등..
Helps prevent brute-force attacks
Watches logs for authenticationfailure
Creates firewall rules to block IP addresses

epel-release 리포지터리 등록 시킨 후 설치하기
```
sudo dnf update
sudo dnf install epel-release
sudo dnf install fail2ban
```

> Extra Packages for Enterprise Linux 8 : EPEL


설치된 파일은   
/etc/fail2ban
에 파일들이 있고

그중 카피해서 사용해야 한다
```
sudo cp fail2ban.conf fail2ban.local
```

`vi fail2ban.local` 보면

주요내용은 참고
```
loglevel: The level of detail that Fail2ban’s logs provide can be set to 1 (error), 2 (warn), 3 (info), or 4 (debug).
logtarget: Logs actions into a specific file. The default value of /var/log/fail2ban.log puts all logging into the defined file. Alternately, you can change the value to:
    STDOUT: output any data
    STDERR: output any errors
    SYSLOG: message-based logging
    FILE: output to a file
socket: The location of the socket file.
pidfile: The location of the PID file.
```

## 이번에는 Fail2ban Backend Configuration 인 jail파일을 살펴봐야함
먼저 jail.conf 파일을 카피한다
```
sudo cp jail.conf jail.local
```

먼저 example
```
  [DEFAULT]

    ignoreip = 127.0.0.1/8
    bantime = 600
    findtime = 600
    maxretry = 3
    backend = systemd
    usedns = warn
    destemail = root@localhost
    sendername = Fail2Ban
    banaction = iptables-multiport
    mta = sendmail
    protocol = tcp
    chain = INPUT
    action_ = %(banaction)...
    action_mw = %(banaction)...
    protocol="%(protocol)s"...
    action_mwl = %(banaction)s...
```
이게 거의 디폴트라고 볼 수 있을 듯

jail.local을 열어서 몇개를 수정하는데 먼저 backend를 찾아서 systemd로 바꿔준다
centos, fedora 계열은 auto에서 systemd 로 바꿔준다

```
backend = systemd
```
거의 앞 부분에서 찾을 수 있음 (다른 계열 ubuntu에서는 이 옵션은 필요없다)


```
# "ignoreip" can be a list of IP addresses, CIDR masks or DNS hosts. Fail2ban
# will not ban a host which matches an address in this list. Several addresses
# can be defined using space (and/or comma) separator.
#ignoreip = 127.0.0.1/8 ::1
```
주석해제 후 remote PC 즉 내 desktop의 ip를 적어준다. (서버 기준)


```
ignoreip = 127.0.0.1/8 ::1 123.45.63.85
```

bantime option 설정
```
# "bantime" is the number of seconds that a host is banned.
bantime  = 10m
```


findtime 안에 몇번이나 failures가 있는지 설정   
10분안에 5번이 최고치로 설정되어 있음 기본
```
# A host is banned if it has generated "maxretry" during the last "findtime"
# seconds.
findtime  = 10m

# "maxretry" is the number of failures before a host get banned.
maxretry = 5
```

### 좀 더 아래로 내려서 email 설정을 해줄 수가 있다
메일을 사용하려면 sendmail을 설치를 해야지 할 수가 있고 option사항이다  
안하려면 스킵
```

```

```
# Destination email address used solely for the interpolations in
# jail.{conf,local,d/*} configuration files.
destemail = root@localhost

# Sender email address used solely for some actions
sender = root@<fq-hostname>

# E-mail action. Since 0.8.1 Fail2Ban uses sendmail MTA for the
# mailing. Change mta configuration parameter to mail if you want to
# revert to conventional 'mail'.
mta = sendmail
```

예 destemail 메일 받을 주소, sender는 보내는 메일 주소
```
destemail = someone@somewhere.net

sender = fail2ban@somewhere.net
```
보통의 메일로도 보내지는지 모르겠음



이제 좀 더 내려보면 JAILS 섹션에 있는데 
```
[sshd]
...
..
생략

[selinux-ssh]
...
...생략..

[apache-auth]
...
...
생략..
```

대충 이런식으로 하나씩 구분이(?) 되어 있는데 이 중 sshd의 jail 옵션을 넣어주고 싶으면   
해당 [sshd] 카테고리(?) 안에다가    
`enabled = true` 라고 적어주면 된다

예를 들어
```
[sshd]

# To use more aggressive sshd modes set filter parameter "mode" in jail.local:
# normal (default), ddos, extra or aggressive (combines all).
# See "tests/files/logs/sshd" or "filter.d/sshd.conf" for usage example and details.
#mode   = normal
enabled = true
port    = ssh
logpath = %(sshd_log)s
backend = %(sshd_backend)s
```

그리고 저장 후 Crtl+z로 background로 잠깐 보내고 

> 다시 vi 사용하던 것을 foreground로 올려면   
`fg` 라고 치면 된다   
구지 잠깐 멈춰놓을 것이 아니고 wq 로 저장을 하고 나가고 됨


먼서 fail2ban 시작을 해준다

```
systemctl start fail2ban
systemctl enable fail2ban
```

> enable을 해둬야 다음에 재부팅 시에 자동으로 시작이 됨

sendmail이 있다면 메일을 보내는 주는 기능이 있다고 한다 (해보지는 않음)   
하지만 없으면 실행하지 않고 스킵!
```
systemctl start sendmail
systemctl enable sendmail
```


확인을 해보면
```
fail2ban-client status
```

```
 sudo fail2ban-client status
Status
|- Number of jail:	1
`- Jail list:	sshd
```

이제 다시 `sudo vi /etc/fail2ban/jail.local` 을 열어서 enabled를 주석처리 해준다음에
```
systemctl reload fail2ban
```

이제 
```
octa@localhost fail2ban]$ systemctl reload fail2ban
[sgtocta@localhost fail2ban]$ sudo fail2ban-client status
Status
|- Number of jail:	0
`- Jail list:	
```
라고 바뀐 것을 확인할 수 있다


[linode 메뉴얼-fail2ban](https://www.linode.com/docs/guides/using-fail2ban-to-secure-your-server-a-tutorial/)   


[fail2ban 설정하기](https://linuxhandbook.com/fail2ban-basic/)



## log 확인하기
로그는 /var/log/fail2ban 파일에서 확인할 수 가 있다. 

```
cat /var/log/fail2ban
```

결과
```
2022-06-07 08:03:28,824 fail2ban.actions        [25832]: NOTICE  [sshd] Unban 141.98.11.112

2022-06-07 10:15:21,982 fail2ban.filter         [25832]: INFO    [sshd] Found 45.144.225.175 - 2022-06-07 10:15:21
2022-06-07 10:15:22,629 fail2ban.actions        [25832]: NOTICE  [sshd] Ban 45.144.225.175

2022-06-07 10:43:16,227 fail2ban.filter         [25832]: INFO    [sshd] Found 141.98.11.112 - 2022-06-07 10:43:16
2022-06-07 10:43:18,359 fail2ban.filter         [25832]: INFO    [sshd] Found 141.98.11.112 - 2022-06-07 10:43:18
2022-06-07 10:43:18,799 fail2ban.actions        [25832]: NOTICE  [sshd] Ban 141.98.11.112
```
대충 몇개만 추려봤는데 재역활을 잘 해주고 있는 것 같다  
단, 141.98.11.112는 오전 8시에 ban이 풀렸다가 다시 10 40분쯤에 다시 또 와서 
다시 ban 당함.

일단 ban 당하는 시간을 좀 늘려야 할 듯 하다

### 좀 더 자세히 보기 
```
sudo fail2ban-client status sshd
```

ssh에 현재 상태를 알려준다
예: 
```
Status for the jail: sshd
|- Filter
|  |- Currently failed:	2
|  |- Total failed:	632
|  `- Journal matches:	_SYSTEMD_UNIT=sshd.service + _COMM=sshd
`- Actions
   |- Currently banned:	2
   |- Total banned:	152
   `- Banned IP list:	141.98.11.112 45.144.225.175
```

bantime 늘리기
```
sudo vim /etc/fail2ban/jail.local 파일에서 
```
bantime을 1d 로 설정했다

```
sudo fail2ban-client reload
```
ok 가 떨어지기는 하는데 ban 오래 가는 지 봐야겠다


## 특정 ip 찾아서 ban 풀기
```
 sudo cat /var/log/fail2ban.log | grep 'Ban 141.98.11.1*'
```

이런식으로 특정 ip를 찾아 준다음에 해당 ip가 Ban에 리스트에 있다면 
예:  
```
2022-06-07 10:43:18,799 fail2ban.actions        [25832]: NOTICE  [sshd] Ban 141.98.11.112
2022-06-07 11:22:59,548 fail2ban.actions        [25832]: NOTICE  [sshd] Ban 141.98.11.112
```

풀어주기
fail2ban-client set {jailname} unbanip {ip주소} 형식으로 입력
```
sudo fail2ban-client set sshd unbanip 141.98.11.112
```

## whitelist 만들기
fail2ban-client set {jailname} addignoreip {ip주소} 식으로 입력

```
fail2ban-client set sshd addignoreip 202.96.110.52
```

이런식으로 해주면 된다.

영구적으로 제외시키려면  
jail.local 파일의 ignoreip 부분에 ip주소를 입력해준다
```
#ignoreip = 127.0.0.1/8 ::1
```
되어 있는 곳을 찾아서 주석을 해제한 후 ip주소를 적어준다. 


## whiltelist 해제
fail2ban-client set {jailname} delignoreip {ip주소}
```
fail2ban-client set sshd delignoreip 202.96.110.52
```

마찬가지로 /etc/fail2ban/jail.locl 파일에서 ignoreip 제거해주기
