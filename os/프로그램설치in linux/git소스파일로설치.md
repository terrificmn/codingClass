# git 설치하기 
git 설치하기

## 쉽게 설치
패키지 업데이트 해준다 (시간이 좀 걸릴 수 있음)
```
  $sudo dnf update -y
```
그 다음 설치
```
  $sudo dnf install git -y
```

## git 설치하기 소스코드 받아서 직접 빌드하기
일단 의존성 해결해주기 위해서 필요한 프로그램 설치해주기   
```
  $sudo dnf install gettext-devel openssl-devel perl-CPAN perl-devel zlib-devel gcc autoconf curl-devel expat-devel -y
```

**참고:  
Git을 깔기위해서 dependencies를 해결해줘야하기 때문에 위에 것들을(?) 업데이트 해준다   
설치되어 있거나 한 것은 빼고 설치함. 나중에 소스파일 빌드? 할 때 에러나면 구글링해서 필요한 프로그램 깔아주기    

source파일 다운받기  
깃 사이트에서 git-2.9.5.tar.xz 로 소스파일 다운로드 함   

그다음 압축풀기
```
$tar -xvf git-2.9.5.tar.xz 
```
그 다음에 디렉토리로 이동해서 make를 해준다 (시간 좀 걸림)
```
  $make prefix=/usr/local all
  $sudo make prefix=/usr/local install
```

> 참고: 우분투에서는 $sudo make all install 까지만 해주면 됨 (버전 2.3.1버전쯤 됨)

중간에 에러가 나면 대게는 dependency가 문제 (구글링 해볼 것)   

make가 완료되면 버전확인해보면 설치가 잘 되었는지 알 수 있음
```
$git --version
```
git version 2.9.5 라고 나오면 ok!
