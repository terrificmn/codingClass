## mqtt ssl
서버의 cert 받기
```
openssl s_client -connect 도메인:포트번호 -showcerts
```

-----BEGIN CERTIFICATE-----    
으로 시작해서    
-----END CERTIFICATE-----    
끝나는 부분을 참고한다   

서버쪽.crt 인 server.crt 와 private key로 pem키를 만들어 줘야 한다.  
서버 인증은 Server Certificate (CA) 를 의미   - 인증기관에서 인증했거나 셀프로 인증   

private key는 
-----BEGIN RSA PRIVATE KEY-----   
로 시작   
-----END RSA PRIVATE KEY-----   
로 끝나는 키 이며    

pem 키는 두 개의 인증서를 합쳐 주면 된다.   

```
cat server.crt server.key > server.pem
```
 
> 또는 직접 합쳐도 된다. 순서는 certificate이 먼저 바로 이후에 Rsa private key가 온다


// TODO
현재는 서버에서 받은 인증서를 사용했지만 client 쪽에서 만든 인증서가 접속이 되는지 테스트를 해봐야겠다.    
--- 아직까지는 해본 결과 클라이언트에서 만들어진 cert와 private key 조합은 안되는 듯 하다.


### 참고 자료 
추후 더 정리하기   

rsa private key를 만들어 주고
```
openssl genrsa -out private-key.pem 2048
```

만들어진 private-key.pem 파일로 certificate를 만들어 준다. 
```
openssl req -new -x509 -key private-key.pem -out cert.pem -days 360
```

[여기 정리 참고하기](https://www.scottbrady91.com/openssl/creating-rsa-keys-using-openssl)

