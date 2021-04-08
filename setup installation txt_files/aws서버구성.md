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





