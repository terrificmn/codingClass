# postman 설치 
yum dnf로 install 도 가능   
postman 홈페이지에서 다운로드를 받는다

그 후 압축을 풀고
```shell
$tar xvf postman압축파일.tar
```

압축 푼 파일을 /opt 경로로 이동시켜준다
```shell
$cd /opt
$sudo mv ~/Downloads/Postman ./
```

심볼릭 링크를 만들어준다.  
Postman 실행파일을 /usr/local/bin/postman에 심볼릭링크로 만들어준다
```shell
$sudo ln -s /opt/Postman/Postman /usr/local/bin/postman
```

이제 postman이라고 실행시키면 됨   
심볼릭 링크가 잘 연결되었는지 확인하려면
```shell
$ls -l /usr/local/bin/postman