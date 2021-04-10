예전에는 회사에서 서버를 구성하고 
웹서버 한 대, DB서버 한 대 
이런식으로 사용을 하는데 
트래픽이 증가하면 서버 증설을 하고 트래픽을 분산해주는 load balancer 도 설치해주고
데이터베이스도 꽉 차면 또 DB서버도 증설하고 
이런식으로 했었다고 한다

시스템 엔지니어 등이 설치하고 있었으나 ..

Scale UP 서버 사양을 올리는 것 (예를 들어 cpu를 16코어로 업그레이드)
Scale out  서버를 병렬적으로 늘리는 것


근데 이제 클라우드 서비스에서 자동적으로 다 해주는 방식으로 바뀌어서 사용하고 있다

대표적으로 AWS가 있는데 

여기에서는 서버 증설 EC2를 늘리는 것도 마우스 클릭으로만 하면 되고 
Elastic Load Balancing 도 마우스 클릭만 하면 되고, 
데이터 베이스 RDS도 더 쉽게 할 수 있게 클라우드에서 제공해주게 되었다.

기존 회사에서 하던 것들을 클라우드에서 할 수 있게 된 것임

이제 서버 없이도 할 수 있게 되는 서비스들이 나오게 되는데
ssh로 접속할 필요도 없고, centos / ubuntu등을 설치할 필요도 없다고 한다.
이것이 바로 서버리스 인데 

대표적으로 AWS의 람다와 API Gateway가 있다고 한다

API Gateway를 통해서 Lambda 가 실행이 되면서 RDS(db)를 할 수 있게 한다고 함

프리티어는 
API Gateway 월 1백만건까지 무료
람다도 월 1백만건 무료




로컬에 있는 소스코드를 서버리스에 어떻게 옮길 것 인가?

먼저 Git hub에 리포지터리를 생성해서 push를 해서 올린다

AWS클라우드에서 설정을 하면 git hub에서 자동으로 가져온다

API Gateway에서 자동으로 경로를 설정하고 
람다에 자동으로 배포가 된다 
서버는 RDS를 사용하게 된다

이제 접속은 (테스트, 일반사용자 모두 ) API Gateway에의 endpoint로 접속을 하게 된다
트래픽이 증가하면 람다에서 알아서 서버 scaling out, up등을 알아서 처리하게 된다

소스코드를 수정했다면 깃허브에 올리면 또 이제 
AWS API Gateway에서 자동으로 다운을 받아서 또 자동으로 하게 되는 것이라고 한다

깃허브에서 API Gateway로 연결해줘서 자동으로 배포해주는 서비스도 있는데
Serverless Framework 가 있다. (무료 가입해야함)

aws 프리티어를 사용하고 있지만 
서버리스 프레임워크를 사용하기 위해서 aws의 credential을 새로 가입해줘야한다

IAM 서비스 AWS 리스스에 대한 권한 관리
사용자를 하나 추가해준다
이 사용자는 git hub에서 aws api로 액세스 할 수 있는 것을 만들어 준다
(웹페이지를 열어서 접속하는게 아니고 프로그래밍 방식으로 액세스로 하는 것: 필수)
AWS Management Console access도 가능하게 해주자

그 다음에 
Attach existing policies directly  기존정책직접 연결에서 
AdministratorAccess를 체크해서 선택해준다

태그는 안해도 됨

그리고 최종적으로 유저를 만든다.

그리고 나서 중요!csv는 꼭 다운로드 해야한다 
new_user_credentials.csv

이 파일을 기억하기 쉽게 파일명을 변경해준다 . 예: api_serve_credential.csv
```shell
$cp cp new_user_credentials.csv /원하는경로/api_server_credential.csv
```

그리고 nodejs가 필요하다~
이미 설치가 되어 있어서 패스

[서버리스프레임 워크https://www.serverless.com/](https://www.serverless.com/)

회원가입을 해줘야한다. 
원하는 다양한 언어+db 등을 제공한다

이 중에서 serverless Flask API를 사용할 것 임

회원가입을 한후에 

python flask API apps을 선택해준다

이제 어플리케이션 이름을 정해주는데 어플리케이션 이름은 깃허브 리포지터리의
프로젝트 명이랑 같게 해서 넣어준다

deploy를 눌러준다

그 후에 
provider credentials을 정해주는데 
여기에서 
AWS Amazon Web Services setup을 눌러준다

그 다음에 name은 User name을 넣어준다
provider type은 Access Key를 선택한 후에 

aws access key 와 aws secret key를 넣어준다

User name,Password,Access key ID,Secret access key,Console login link
api_server,여기가-패스워드,여기가-시크릿키,https://콘솔-로그인-주소


그 다음에 인스톨에 나온 명령어로 npm 설치해준다
이게 완료되면 deploy에 나온 명령어를 복사해서 터미널에 실행

사이트에 나온 명령어를 복사해서 사용하면 됨


이제 어플리케이션 이름으로 디렉토리가 하나 생김

이제 여기에서 serverless.yml 파일을 수정해주는데 
파이썬 버전을 3.7로 개발했으므로 
provider: 
    runtime: python3.7
로 바꿔준다

그리고 requirements.txt 파일의 내용도 넣어준다
그리고 app.py 및 다른 디렉토리들을 어플리케이션 안으로 복사해서 넣어준다

그리고 배포하기
```shell
$serverless deploy 
```

이제 배포가 끝나면 endpoint주소가 나오는데 
이거를 이제 postman에서 endpoint로 변경해서 restful api를 테스트 하면 된다

<트러블슈팅>
만약 deploy 명령어로 실행을 하고 있는데 계속 파이썬 3.7이 없다고 할 때

Error: python3.7 not found! Try the pythonBin option.

serverless.yml 파일의 custom: 부분에 pythonRequirements:부분을 추가로 넣어준다
```yml
custom:
  wsgi:
    app: app.app
  pythonRequirements:
    pythonBin: python3
```

위처럼해도 위의 에러는 처리가 됨. 하지만
파이선 3.8을 다시 설치한 다음에 아예 새로운 서버리스 애플리케이션을 만들고 진행하니
위의 pythonRequirements: pythonBin: python3 부분을 추가 안해도 문제가 없었다.

하지만 이제는 로그인을 하라고 에러가 남
You are not currently logged in. To log in, use: $ serverless login
로그인 하시란다;;;; 로그인이 되있다고;;
어쨌든 로그인 방법도 알려주시니 그래도 해본다

```
$ serverless login
```
그러면 웹브라우저 상으로 로그인이 되어진다
다시 터미널로 와서 

다시 
```
$ sudo serverless deploy
```
이번에도 같은 에러 
You are not currently logged in. To log in, use: $ serverless login

해결방안은 
serverless.yml 파일에 있는 
org: 내아디
적혀있을텐데 org 부분을 주석처리해버거나 지워준다. 그리고 저장

그리고 다시 해서 되면 ok

만약 여기에서 
Serverless Error ----------------------------------------
AWS provider credentials not found. Learn how to set up AWS provider credentials in our docs here: <http://slss.io/aws-creds-setup>.
위와 같은 에러가 발생하면 환경변수를 설정해줘야하는데, serverless 명령어로 처리해보자
위의 사이트에 가면 잘 나와있다 참고하면 되는데
export로 환경변수를 하는 방법은 나름 빠른 셋팅 방법이라고 되어 있으나 계속 같은 에러가 발생했다.   serverless config credentials 명령어로 파일로 만드는 방법도 마찬가지 계속 같은 에러   

참고로 환경변수 지정은 아래처럼 한다. 하지만 내 경우에는 안됨 (키 2개다 등록해야함)
```shell
$export AWS_ACCESS_KEY_ID=IA2MASDFWBs239Q46VSD
```
(예를 든 가짜키임)

Serverless Error ----------------------------------------

그래서 최종 결론은!!!
홈디렉토리에 있는 크레덴셜 파일을 지워버리는 것!
```
$cd ~/.aws/
$ls
$rm -i credentials
```
찾아보면 파일이 하나 있는데 지워준다
그리고 나서 다시 

```shell
$ 
serverless config credentials --provider aws --key IA2sMASszDFWBQ4SAE6VSD --secret sdfEsdfWNPUrAj4rnxSDOIsdfFJO9sadfz1rhF6casdfH0
```
(예를 든 가짜키임)
이렇게 하면 다시 credentials 파일을 만들어 준다

이제 다시 deploy를 할 차례
```shell
$sudo sls deploy
```
*serverless는 sls로 해도됨

드뎌 반나절동안 씨름하던 것 해결 ㅠㅠㅠ 배포가 잘 되고 endpoins 주소가 나오고 
한번 브라우저로 링크 열어주면 json 형태로 보여지면 성공!!
이제 깃허브로 연동하는 것 할 차례!!

참고로 serverless config 할 때에...
디폴트 프로파일이 이미 있다고 할 때에는 -o or --overwrite 옵션을 넣어주고 해보자
사실 저 옵션을 해도 안되서 (credentials 파일을 아예 지움)

[serverless프레임워크 참고매뉴얼](https://www.serverless.com/framework/docs/providers/aws/guide/credentials/)  



# ci/cd 연결하기

먼저 깃허브 리포지터리 연결하고  깃 허브에 로그인을 하고 
깃에서 어떤 리포지터리를 연결할지 정해준다. 
인증을 해준다 그러면 연결이 되는데 

connect aws도 aws serverlss를 연결이 되어 있을 것이고

이제 위에서 리포지터리를 연결했으므로 아래에서 

branch deploys 에서 
깃허브 브랜치를 선택해준다 (main)
stage 는 dev로 선택


notification은 email로 선택하고 email주소를 입력해준다
성공 실패만 받기로 체크하고 이메일을 입력해준다

참고: 그 중..
slack 팀 협업 툴인데 notifications를 현업에서 많이 사용하는데 (나중에 알아보기)

그러면 CICD 셋팅은 완료된 것이고

그리고 나서 다시 로컬의 파일에 와서 파일을 일부 수정한후 다시 깃 커밋을 한 후 push를 하면

serverless에서 자동으로 감지해서 (git과 연결을 해놨기때문에)
CICD 메뉴에 보면 자동으로 deploying이 되고 있는 것을 알 수 있음


