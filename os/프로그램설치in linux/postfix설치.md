# Postfix 설치
sendmail 과 비슷한 메일 프로그램

> 웹에서 메일을 mail()함수로 해결해보려고 했는데   
sendmail, postfix 등은 메일은 잘 보내지는 것 같으나 보내진 메일은 거의 스팸메일로 들어가지거나 아예 차단되는 듯 하다
그래서 이래저래 시도하다가 결국은 메일은 포기하고 라이브러리를 이용해서 보내는걸로 바꿈: swiftmailer 등.. )

> 예전에는 도메인 없이 localhost로만 하던 것이라 도메인이 있을 경우에는 다시 도전해 볼만할 듯하다

참고설명:  
Postfix is one of the most popular open-source Mail Transfer Agent (MTA) which route and delivers mails.   
It is an alternative to Sendmail MTA which comes pre-installed in all version before Centos/RHEL 5.   
CentOS Postfix installation is a process which requires a lot of precision.  

일단 sendmail이 있다면 검색 후 제거 
```
  $rpm -qa | grep sendmail
```
있으면 지우는게 좋다. 
```
  $sudo yum remove sendmail*
```

그 다음 postfix 깔기
마찬가지로 rpm -qa | grep postfix 로 깔려 있는지 확인한 후 
```
  $sudo yum install postfix
```

postfix 설정
```
  $ sudo vim /etc/postfix/main.cf
```

주석 제거 후 추가해준다 
```
myhostname = mail.example.com
mydomain = example.com
myorigin = $mydomain

inet_interfaces = all 
## (localhost 에서 all변경한다)
inet_protocols = all

mydestination = $myhostname, localhost.$mydomain, localhost
##(주석처리제거한다)

mynetworks = 192.168.1.0/24, 127.0.0.0/8
## 추가 및 변경
home_mailbox = Maildir/
##주석 제거
```

: 누른 후 qa 로 저장 후 나가기

재시작 및 자동으로 시작되게 등록
```
  $systemctl restart postfix
  $systemctl enable postfix
```

