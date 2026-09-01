docker의 경우 

뭔가 설치하려고 할 때 이런 비슷한 에러가 발생한다면.. 
```
are supported and installed on your system.
perl: warning: Falling back to the standard locale ("C").
[docker_noetic@docker-remote scripts]$ locale
locale: Cannot set LC_CTYPE to default locale: No such file or directory
locale: Cannot set LC_MESSAGES to default locale: No such file or directory
locale: Cannot set LC_ALL to default locale: No such file or directory
```

일 때

Dockerfile에 
`RUN apt-get update && apt-get install locales` 를 추가해준다   

그리고 ENV도 추가해준다  
```
ENV DEBIAN_FRONTEND noninteractive
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
```

이 정도로 설정하고 다시 docker compose build 해준 다음에   
어떤 특정 프로그램을 설치할 때 잘 넘어갔다  




## 그래도 안되면 

To solve this issue you can add a default locale to the /etc/default/locale file:


```
locale
```
And generate the missing locale:
```
sudo locale-gen az_AZ.UTF-8
```
Then reconfigure locales:
```
sudo dpkg-reconfigure locales
```

테스트는 안해봄;
