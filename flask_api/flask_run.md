# flask run으로 실행하기, 환경변수 설정
[flask 매뉴얼-사이트](https://flask.palletsprojects.com/en/1.1.x/cli/)  

<br>

python app.py 이런식으로 실행을 하면 페이지를 만든 것이 실시간으로 적용이 안되고, 
코드를 수정을 해도 반영이 안된다.

그래서 flask run 으로 실행을 하면 되는데
기본으로 app.py 를 열어준다

만약 실행시킬 파일을 바꾸려면 환경변수를 바꿔준다  
환경변수 $FLASK_APP=app2.py 이런식으로 지정해주게되면  
처음에 열리는 파일로 지정이 된어서 app2.py가 열리게 된다.

```shell
$export $FLASK_APP=app2.py
```

윈도우즈에서는 cmd에서 실행
```shell
$set FLASK_APP=app2.py
```

서버 포트 셋팅, 기본은 5000번   
만약 포트를 5001번으로 하고 싶다면..아래 코드를 참고
```shell
$export $FLASK_RUN_PORT=5001
```

윈도우즈는 환경변수의 $싸인을 빼고 set으로 처리해주면 됨. (위에 처럼)
```shell
$set FLASK_RUN_PORT=5001
```

만약 코드 수정한 것이 바로 반영이 안된다면 FLASK_ENV가 development로 해주면 된다.
```shell
$export FLASK_ENV=development
```
