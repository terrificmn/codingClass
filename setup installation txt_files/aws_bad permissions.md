Load key "./key.pem": bad permissions
ubuntu@54.110.123.52: Permission denied (publickey).

또는 

Permissions 0640 for './key.pem' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.

이런식으로 에러가 날 때 

퍼미션이 다른 사용자들도 사용할 수 있게 되어 있어서 거부가 된다 

간단하게 바꿔주자

```
sudo chmod 400 ./key.pem 
```

이제 aws에 접속을 하면 
```
ssh 54.110.123.52 -i ./key.pem -l ubuntu
```

잘 된다