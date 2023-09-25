리눅스 우분투 버전으로 다운받아서 dpkg로 설치하는 것이 편함

단, 의존성 때문에 설치가 안되므로  
```
sudo apt install libpangocairo-1.0-0
```

만약 호환이 안된다며 설치가 안된다면..  
```
sudo apt --fix-broken install
```

다시 의존성 패키지를 설치를 해준다.  


그리고 다시 anydesk 설치를 해준다. 그리고 나서 다운받은 패키지를 설치
```
sudo dpkg -i anydesk....파일명
```

