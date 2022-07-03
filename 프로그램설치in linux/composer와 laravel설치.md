# composer 와 laravel 설치
composer 와 laravel 설치

## composer 설치 (php 관리도구 dependency)
다른 php라이브러리를 사용하려면 composer를 먼저 설치해야한다 (swiftmailer같은 것)  
(아예 su 권한으로 시작는게 좋다)  
```
  $su-
```

**참고 사이트  
https://getcomposer.org/download/  
Command-line installation 설치 법을 참고해서 할 것:    
웹 사이트에서 명령어를 입력하라고 나온대로 하면 됨, 위의 사이트 접속해볼 것  

원래 사이트에 나와있는 스탠다드로 깔면 $php composer.phar 로 실행해야 함  
터미널 어디에서든 하고 싶을 때는 

composer.phar 파일을 이동시켜준다   
```
$mv composer.phar /usr/local/bin/composer
```

참고   
https://getcomposer.org/doc/00-intro.md#globally   
우분투에서는 잘 됨

그냥 매뉴얼 사이트에서 나온 그대로 설치하되  
3번째 설치할 때 --filename 만 준다음에 설치   
php composer-setup.php --filename=composer   
그러면 현재 위치에 composer파일이 다운되는데  
그 파일을 /usr/local/bin/composer로 이동시키면 composer만 입력해도 전역에서 사용할 수 있게 된다   

아니면 --install-dir=/usr/local/bin
으로 하면 되겠음   
암튼 centOS 8과 경로가 다름에 주의!   


**설명 1~4까지 설명 본 후 (다음에 까먹었을 경우 ㅋ) 옵션 잘 넣어서 설치!!  
1. 
```
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"   
```
---->Download the installer to the current directory   
---->현재 위치한 디렉토리에 받아지는거에 유의 (어차피 나중에 지워짐)

2. verify하기   
```
php -r "if (hash_file('sha384', 'composer-setup.php') === '756890a4488ce9024fc62c56153228907f1545c228516cbf63f885e036d37e9a59d27d63f46af1d4d07ee0f76181c7d3') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
```
---> Verify the installer SHA-384  
---> 이 명령어 붙여넣기 하면 다운받은 인스톨러를 확인  
---> 그러면 Installer verified 라고 나옴  

3. **중요!**   
  주의: php composer의 디렉토리와 파일네임 변경 옵션인데 설명을 보고 한번에 옵션 넣어서 실행할 것   
일단 이렇게 생김 --install-dir --filename 옵션 보고 실행할 것

```
php composer-setup.php
```
--->Run the installer  
--->여기서 다른 옵션값을 넣어서 해주는것이 좋다.    
--->디렉토리와 파일이름이 composer.phar 기본값으로 되어 있어서 옵션으로 바꿔주는것이 좋다.(이번에 설치할때 디렉토리만 변경, 파일네임은 변경못함)   
--->예:   
  첫번째 디렉토리 변경 옵션 --install-dir   
  (You can install composer to a specific directory by using the --install-dir option and providing a target directory. Example:)   
  예: $php composer-setup.php --install-dir=bin  

  결과: 디렉토리 지정안했을 경우   
```
    All settings correct for using Composer   
    Downloading...  
    Composer (version 2.0.8) successfully installed to: //composer.phar  
    Use it: php composer.phar  
```
  결과: 디렉토리 bin으로 지정했을 경우 아래처럼 나온다
```
    All settings correct for using Composer
    Downloading...
    Composer (version 2.0.8) successfully installed to: /usr/bin/composer.phar
    Use it: php bin/composer.phar
```

**우분투 경우**에는 --install-dir을 /usr/local/bin 으로 해줘야 함     
```
php composer-setup.php --filename=composer --install-dir=/usr/local/bin
```
directory /usr/local/bin is not writable 이라고 하면 sudo 로 진행한다

**CentOS 경우**에는 /usr/bin으로 
```
$php composer-setup.php --install-dir=/usr/bin --filename=composer
```

install-dir 옵션을 잘 지정하면 경로 어디에서나 composer라고 하면 잘 된다   
php composer 라고 안 해도 됨   
옵션을 지정 안하면 php composer 라고 해야하는 듯 하나, 다른 라이브러리 등에서 잘 실행이 안되서 곤란해질 수 있다   


  파일 네임 변경 옵션 --filename   
  (You can specify the filename (default: composer.phar) using the --filename option. Example:)  
  $php composer-setup.php --filename=composer  

  (tutorial로 알려주는 곳에서 거의 명령어를 composer로 알려줘서 실행을 해도 --filename으로 옵션을 안했다면   
  composer명령어 실행할 떄 그런 명령어 없다고 에러;;; ㅡㅡ; 그때는 composer.phar 로 쳐야한다)   
  즉 실행 3번에서 --filename 옵션에 따라 달라진다   

4. unlink로 지우기
```
php -r "unlink('composer-setup.php');"
```
Remove the installer 인스톨러를 지워준다


## 지울 때 (우분투의 경우)
rm /usr/local/bin/composer



## Laravel 설치 
[참고사이트:https://laravel.com/docs/8.x/installation#getting-started-on-linux](https://laravel.com/docs/8.x/installation#getting-started-on-linux)

> composer가 먼저 설치되어 있어야 함  

설치하기
```
$composer global require laravel/installer
```

*참고:
우분투에서는 php composer라고 입력해야함

그러면 설치를 해준다
```
Changed current directory to /home/cta/.config/composer
6개의 패키지를 설치 sympony, laravel ...etc
Installing dependencies
```
등을 해줌 

```
$ laravel
```
이라고 입력하면 명령어를 못 찾음
bash: laravel: command not found...   

그래서 이제 $PATH 변수에 넣어서 Laravel만 쳐도 실행이 되도록 만들어줘야함

라라벨이 실행가능하게 파일은 리눅스라면 
$HOME/.config/composer/vendor/bin 또는 $HOME/.composer/vendor/bin
위 둘 중 한 곳인데 

참고: 우분투도 경로가   
~/.config/composer/vendor/bin 에 laravel이 들어 있음

$HOME 변수에는 유저 디렉토리 경로가 들어가 있음   
그래서 홈 경로로 간 후에 찾아보면     
$cd ~ 또는 $cd ~/.composer   

어쨋든 composer 까지 쳐보면 아니 쳐보기 전에라도 탭을 누르면 자동완성이 안됨 디렉토리가 없음

위의 디렉토리 중에 .config 디렉토리 안에 들어가 있음을 나중에 알게 됨  

많은 사이트 튜토리얼에서는 .composer/ 안 경로로 설명하는데 그 쪽에 안깔려있으니 경로를 먼저 확인해야함   

참고  
정확하지는 않지만 처음에는 composer를 설치한 후 실행을 안해서 그런가  
위의 두 곳의 경로다 없었던 같은데.. 암튼 컴포저를 일단 한번 실행해보고
$composer로 먼저 터미널에 실행을 한 후에  
그 다음에 확인해 보니 .config/composer/....생략 안에 생성되어 있음   

암튼 다시 돌아와서   
이제 $PATH 를 등록? 해줘야함  
```
$vi ~/.bashrc
```
편집기에서 맨 아래줄에 아래와 같은 코드를 입력

```
# laravel
export PATH="$HOME/.config/composer/vendor/bin:$PATH"
```
그리고 :wq 저장을 한다

터미널을 끄고 다시 열던가 아니면 
```
$source ~/.bashrc
``` 

그러면 업데이트가 되어서 echo명령어로 확인해보면 등록이 되어 있음  
```
$echo $PATH
```

```
/home/내계정/.config/composer/vendor/bin:/home/내계정/.composer/vendor/bin: ...생략
```

이제 라라벨 실행해보기
```
$laravel
```

그러면 버전정보와 help 옵션이 뜨면 오키
