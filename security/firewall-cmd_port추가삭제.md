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