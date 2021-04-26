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


정확하지는 않지만, 몇번의 5~6번의 실패 끝에;; 
최초 deploy를 한 후에 로컬에서 디플로이를 할 때는 sls deploy를 하면은 잘 된다
근데 만약 이렇게해서 로컬에서 디플로이가 성공한 다음에 다시 깃허브를 연동해서 작업하면
ci/cd 연동시 fail이 되는 듯 하다. (정확하지는 않지만.. 이제 테스트는 그만 ㅠ)

깃허브를 연동할 때에는 어플리케이션 만든 후 최초 deploy만 로컬에 해주고 
그 다음에는 cicd설정을 한 후에 깃허브로 push해서 자동배포가 이루어지게 하면 
성공적으로 배포가 되었음~

# 깃허브 연동시키기 , 서버레스 프레임워크에 어플리케이션 만드는 것부터 시작
https://www.serverless.com/ 
1. flask 어플리케이션 추가

2. deply now 화면으로 바뀌면 provider credentials를 
3. 화면에 나오는 복사 붙여넣기를 해준다 먼저 install
```
$sudo npm i -g serverless && serverless init sf_4SsdZq
```
처음 npm실행에만 sudo를 해주고, 뒤의 serverless 에는 sudo를 실행시키면 안됨
init sf-문자열 은 어플리케이션을 만들면 자동으로 생성되는 고유의 문자열

4. 아마 모듈에서 퍼미션 에러가 발생할 것임. 추측하기로는 npm 버전을 낮추면 되는거 같은데 아직 해결을 못함
참고로 위와 같은 에러가 발생시에는 sudo를 해도 계속 같은 퍼미션 에러가 발생
yp ERR! configure error 
gyp ERR! stack Error: EACCES: permission denied, mkdir '/usr/lib/node_modules/serverless/node_modules/snappy/.node-gyp'
gyp ERR! System Linux 4.18.0-294.el8.x86_64
gyp ERR! command "/usr/bin/node" "/usr/lib/node_modules/npm/node_modules/node-gyp/bin/node-gyp.js" "rebuild"
gyp ERR! cwd /usr/lib/node_modules/serverless/node_modules/snappy
gyp ERR! node -v v14.16.1
gyp ERR! node-gyp -v v5.1.0
gyp ERR! not ok 
일단 이그노어하기로 함 ㅡㅡ;, 단, 마지막 메세지가 
serverless ⚡framework
Serverless › Template successfully installed. Run "cd movie-recommendation-api && serverless deploy" to get started...
이렇게는 나와야함

참고.. 
일단 글로벌 설치로 안되는 이유가 npm 버전이 안맞아서 인거 같기도 한데 
알아보니 6.1x 대로 바꿨더니 됐다는 것도 봤지만, 일단 npm을 사용하고 있기 때문에 
최악의 경우 다운그레이드 하기로 함


5. deploy 하기. cd로 생성된 디렉토리로 이동한 다음에 
serverless deploy하기 sudo를 붙인다
```
$cd movie-recommendation-api && sudo serverless deploy
```

이제 endpoints 주소와 성공적으로 만들어졌다는 메세지가 나오면 일단 성공인데

Publishing service to the Serverless Dashboard...
Serverless: Successfully published your service to the Serverless Dashboard: https://app.serverless.com/terrificmn/apps/test2-cicd/test2-cicd/dev/us-east-1

**중요!!!**
그리고 나서 이제 브라우저 화면으로 돌아가면 (서버레스 프레임워크 대시보드(홈피))
자동으로 새로고침이 될 것임. 만약 새로고침이 안된다면 화면을 클릭해본다 
어쨋든 디폴로이 버튼을 막 클릭해준다 ㅋㅋ 새로고침하지말고 그러면 잘 생성이 된다 
여기에서 **절대 새로고침 누르지 말것;;** 
화면이 자동으로 안바뀐다고 새로고침을 안했더니 어플리케이션이 연결이 안되는 버그가 있었다.
물론 endpoint도 있어서 url에 치면되기는하나 홈페이지 대시보드(?) 화면에서 내용을 볼 수가 없었음

뭔가 잘못되었다면 지울 수도 있다. 로컬에 생성된 파일을 먼저 지우면 안되고 
생성된 어플리케이션 디렉토리로 이동한 후 (디폴리 된 디렉토리)
참고로 아마존에 올라간 서버리스는 sls remove로 지울 수 있음
```shell
$sudo sls remove
```
만약..
삭제하다가 실패해서 디렉토리를 지워버렸다면 sls remove 가 되지 않는다 
아마존 S3 에 가서 buckets에 있는 것을 직접 지워야한다
아마도 지우다가 실패했기 때문에 empty로 만든다음에 
지우기를 하면 된다. 

이제 프로그래밍한 프로젝트를 디렉토리(파일)을 복사해서 deploy된 디렉토리에 붙여넣어준다
이제 깃 허브와 연동할 차례다!

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
.gitignore 파일을 만들고 node_modules 를 추가해준다 (node_modules은 필요없음)
private으로 만들어주는게 좋다. 
(config파일의 비번이 노출되기때문에 이 파일은 ignore시키면 안됨)
서버리스가 아니면 보통 깃허브라면 비번이 들어가있는 파일은 ignore시켜야한다

그리고 프로그래밍한 프로젝트의 모든 파일들을 복사해서 넣어준다.
그리고 깃허브 리포지터리에 first commmit push를 해준다. 

먼저 git init을 한 후에 
.gitignore 를 만들고 
```
node_modules
__pycache__
```
그리고 serverless.yml 파일의 python 버전을 3.7로 수정하고 
requirements.txt 파일에도 필요한 라이브러리를 넣어주고 
pandas만 일단 빼고 하기로 했다 
(**2차 커밋이 중요하다!!** 왜냐하면 이때 ci/cd로 연동이 되어서 이때 자동배포가 이루어지고 
실제 프로젝트가 배포가 되는 것이기 때문이다)

그리고 git remote add를 하고 commit & push를 해준다

이제 깃허브 리포지터리가 셋팅이 되었고 서버레스 프레임워크의 CICD를 설정해준다

그리고 서버레스 프레임워크의 설정을 해준다
git 연동은 serverless 프레임워크 홈페이지에서 내가 만든 app를 선택하면 그 중에 ... 이 있고 
거기를 클릭하면 settings가 있는데 클릭하면 된다
여기에서는 git과 connect를 설정해주고 
(전에 연동한게 있으면 disconnect 한 후 다시 연동- 리포지터리를 다시 연결해준다)
전에 만든 repository settings 에서 branch deploys 브랜치등을 셋팅해준다. (main으로 함)

이제 연동이 끝났으므로 테스트 2차 commit을 해서 push를 하면 
requirements.txt 에서 pandas를 추가해준다음에 다시 commit 하고 push한다

그러면
serverless framework에서 감지하고 자동으로 깃허브 push를 감지해서 
자동으로 배포를 시작한다
홈페이지 대시보드의 ci/cd deploys 을 들어가면 바로 deploying 을 확인할 수 있다.

이번에는 3;11 걸려서 성공



참고: 
나중에 깃허브로 연동이 되는 것이라 프로젝트명(디렉토리명) 자체는 문제가 안되는 듯 하다.

로컬에서 테스트하기 위해서는 디렉토리명이 src로 되어야했는데(프로젝트명으로 바꿀 수는 있으나..)
테스겸 디렉토리명을 바꾼다음에 해보니, 로컬에서도 문제없고
깃허브 연동해서 cicd도 바로 적용된다.