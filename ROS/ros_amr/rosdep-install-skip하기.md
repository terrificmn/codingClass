# --skip-keys 옵션

rosdep install 을 할때에 해당 프로젝트의 package.xml 의 <depend> 태그에 있는 프로그램을   
다운을 받는데,  

우분투, 페도라 등에서 패키지 관리 프로그램( apt 등) 에서 사용되는 패키지 명과 다를 경우가 있다.   

이 때에는 
```
ERROR: the following packages/stacks could not have their rosdep keys resolved to system dependencies:  
my_package: Cannot locate rosdep definition for [serial]
```

이런식으로 에러가 발생   

이때에는 rosdep install 키워드로 실행할 때 해당 의존성 패키지를 생략할 수가 있다   
`--skip-keys 패키지명`

또는 package.xml 에서 해당 <depend> 태그를 날려버린다 


전체 명령어

```

```


## rosdistro

rosdep 의 base.yaml 파일 확인해보기  
yaml파일 안에 각 리눅스 디스트로에서 사용하는 패키지명이 들어가 있다.   

base.yaml 을 열어서 확인해 보자 

[rosdistro-rosdep-base.yaml확인하기](https://github.com/ros/rosdistro/tree/master/rosdep)

