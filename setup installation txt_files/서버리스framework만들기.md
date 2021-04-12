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



yp ERR! configure error 
gyp ERR! stack Error: EACCES: permission denied, mkdir '/usr/lib/node_modules/serverless/node_modules/snappy/.node-gyp'
gyp ERR! System Linux 4.18.0-294.el8.x86_64
gyp ERR! command "/usr/bin/node" "/usr/lib/node_modules/npm/node_modules/node-gyp/bin/node-gyp.js" "rebuild"
gyp ERR! cwd /usr/lib/node_modules/serverless/node_modules/snappy
gyp ERR! node -v v14.16.1
gyp ERR! node-gyp -v v5.1.0
gyp ERR! not ok 



원래 npm i -g serverless && serverless init sf_tx8CdtzP
요런식으로 설치를 하는데 

위와 같은 에러가 발생시에는 sudo를 해도 계속 같은 퍼미션 에러가 발생
퍼미션 에러가 나는 경우에도 파일들을 잘 설치되고 deploy도 되지만 그래서 
enpoint도 나와서 접속도 되는데 정작 serverless framework 홈페이지에는 반영이 안됨

일단 sudo로 npm 을 설치하면 error가 뜨지만 일단 메세지는 무시;;; 
깃허브로 연동할 것이므로 
마지막 deploy가 잘 되면 

Publishing service to the Serverless Dashboard...
Serverless: Successfully published your service to the Serverless Dashboard: https://app.serverless.com/terrificmn/apps/test2-cicd/test2-cicd/dev/us-east-1
이 메세지가 나올 때까지 기다리고 안나온다면 
/웹브라우저로 serverless 프레임워크가 있던 페이지로 돌아간다. 절대 새로고침 누르지 말것;;
이것때문에;;; 암튼 버그가 많은거 같다;; 내가 문제일 수도 있겠지만
어쨋든 디폴로이 버튼을 막 클릭해준다 ㅋㅋ 새로고침하지말고 그러면 잘 생성이 된다 

참고로 아마존에 올라간 서버리스는 sls remove로 지울 수 있음
sudo sls remove

일단 글로벌 설치로 안되는 이유가 npm 버전이 안맞아서 인거 같기도 한데 
알아보니 6.11 대로 바꿨더니 됐다는 것도 봤지만, 일단 npm을 사용하고 있기 때문에 
최악의 경우 다운그레이드 하기로 함

삭제하다가 실패해서 디렉토리를 지워버렸다면 sls remove 가 되지 않는다 
아마존 S3 에 가서 buckets에 있는 것을 직접 지워야한다
아마도 지우다가 실패했기 때문에 empty로 만든다음에 
지우기를 하면 된다. 


# ci/cd 연결하기

ci/cd 설정에서 add provide 를 정해주는데 provide type을 Role ARN 으로 설정해서 만들어 준다
그러면 asw 페이지로 이동하는데 
The following resource(s) require capabilities: [AWS::IAM::Role]
This template contains Identity and Access Management (IAM) resources. Check that you want to create each of these resources and that they have the minimum required permissions. In addition, they have custom names. Check that the custom names are unique within your AWS account.Learn more
이부분에서 퍼미션에 동의를 해준다 

aws에서 생성이 완료되면 자동으로 aws와 연결이 된다


이제 깃과 연동할 차례인데 
먼저 리포지터리를 새로 만들어 준다음에
로컬 프로젝트 디렉토리에서 (sls deploy로 생긴 프로젝트 디렉토리)안에서 git init을 실행한 후에 
.gitignore 파일을 만들고 node_modules 를 추가해준다 
그리고 깃허브 리포지터리에 first commmit push를 해준다

그리고 서버레스 프레임워크의 설정을 해준다
git 연동은 serverless 프레임워크 홈페이지에서 내가 만든 app를 선택하면 그 중에 ... 이 있고 
거기를 클릭하면 settings가 있는데 클릭하면 된다
여기에서는 git과 connect를 설정해주고
전에 만든 repository settings 에서 브랜치등을 셋팅해준다. 

그리고 나서 테스트로 app.py 파일의 message만 조금 손을 본 후에 (테스트로)
그리고 serverless.yml 파일의 python 버전 3.7로 바꿔주고 (로컬 3.7에서 개발함)
requirements.txt 필요한 패키지 목록 넣어준다 
대망의 커밋 후 푸쉬~!

이제 서버리스 프레임워크 대시보드의(홈피)의 ci/cd 메뉴를 보면
자동으로 깃허브 push를 감지해서 deploying을 시작한다

(오 4분걸려서;; success로 바뀜!)
(일단 branch 가 master main은 상관이 없는 듯)
이제 엔드포인트 주소로 복사해서 사이트가 뜨는지 확인!
메세지가 커밋한 것으로 바뀌어 있음!! 굿!!