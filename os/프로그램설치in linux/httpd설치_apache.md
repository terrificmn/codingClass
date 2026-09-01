# HTTPD (apache) 설치
```
  $ sudo dnf -y install httpd
```
서버 시작은
```
  $ systemctl start httpd.service 
```

참고   
https://docs.fedoraproject.org/en-US/quick-docs/getting-started-with-apache-http-server/index.html


httpd 최신 버전  source 파일은 2.4.46 인데   
소스파일로 받아서 컴파일러 하려고 했더니 의존성 해결해야하는것이 꽤 많은 듯   
APR 없다고 하고 아마도 APR-util 암튼 귀찮아서    

참고 컴파일-빌드-인스톨까지 잘 나와 있음   
https://httpd.apache.org/docs/2.4/install.html

그냥 dnf로 쉽게 설치하자ㅋㅋㅋ
2.4.37 임
