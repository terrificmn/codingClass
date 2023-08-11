# curl 명령어로 api 활용

curl -X 을 이용해서 -X 는 request 이고 커맨드는 'GET' 등으로 사용하게 된다   
-H 옵션은 header 정의 부분인데, json 파일형식을 적어주게 된다

이런식으로 사용
```
curl -X 'GET' \
'http://주소/api/v1/엔드포인트주소이름' \
-H 'accept: application/json'
```


## 웹으로 request
웹 브라우저에서 http://주소/api엔드포인트(주소)

