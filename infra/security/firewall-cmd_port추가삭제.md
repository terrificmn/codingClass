리스트로 보기 
```shell
sudo firewall-cmd --list-all
```

--add-port=포트번호/프로토콜
```shell
sudo firewall-cmd --permanent --add-port=8501/tcp
```

--remove-port=<portid>[-<portid>]/<protocol> 옵션 사용
```shell
sudo firewall-cmd --permanent --remove-port=8501/tcp
```


--add-servce=서비스명 예 dns  
`sudo firewall-cmd --permanent --add-service=dns`


삭제
--remove-servce=서비스명 예 dns  
`sudo firewall-cmd --permanent --remove-service=dns`

물론 이후 reload 를 해서 적용해준다. 



```
sudo firewall-cmd --reload
sudo firewall-cmd --list-all
```