# 기술 및 공유 Blog 프로젝트
현재 보고 계시는 Blog 입니다.
Blog를 직접 개발, 배포 하고 직접 운영도 하는 프로젝트입니다.

많은 블로그들이 있지만, 나만의 블로그를 직접 만들어보고 싶어서 하게된 프로젝트이며  
깃허브로 프로젝트를 개발/진행하면서 AWS에 직접 배포하고 운영하고 있습니다.

<br/>

## 기능
1. Posts - 기술 블러그 및 공부한 내용을 업로드 합니다.
2. DevNotes - 개발과정을 일지처럼 남길 수 있는 게시판 입니다.
3. Portfolio - 포트폴리오를 업로드

<br/>

## 사용언어
PHP 8  객체 지향 언어를 사용합니다.

<br/>

## 사용DB
MariaDB - OpenSource RDBMS 

<br/>

## 웹서버
무료 오픈소스 Nginx 사용    
(docker를 구성할 때 default.conf 설정파일을 사용해서 웹서버의 경로를 설정)

<br/>

## 프레임워크
1. Laravel    
    - 중복되는 작업을 줄여줄 수 있는 프레임워크 입니다.   
    - php언어로 MVC 아키텍쳐에 의해 작성할 수 있습니다.

2. tailwindcss  
    - css를 미리 만들어져 있는 tailwindcss를 사용해서 쉽게 적용할 수 있습니다.

<br/>

## 개발환경
1. 리눅스 배포판 운영체제 (CentOS 8 / Ubuntu 18.04)

2. Docker: 우분투에서도 쉽게 작업할 수 있게 도커 환경 구축  

3. Docker3 테스트

- 컨테이너 구성은 nginx, php, mariadb, composer, npm, artisan  PhpMyAdmin: DB tool을 사용 합니다    
- npm, composer 같은 패키지(라이브러리) 관리     
- Laravel 프레임워크의 Command Line Interface인 artisan도 container로 구성하여 쉽게 사용할 수 있습니다.  

<br/>

## 서버
AWS - EC2 t2.micro Free Tier
아마존에 배포해서 사용하고 있습니다.

<br/>

## 깃허브
[깃허브 소스코드 보러가기](https://github.com/terrificmn/laravelBlog.git)
