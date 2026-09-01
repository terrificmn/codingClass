유저 만들 때 사용하거나. 뒤의 문자열이 패스워드가 된다    

```
RUN echo 'root:Docker!' | chpasswd  
```
또는   
```
RUN echo 'Docker!' | passwd --stdin root   
```

docker는 root권한으로 build를 하는데 일반 유저로 하려고 하면  (먼저 유저를 만들기는 해야함)
sudo등을 할 때 비번을 쳐야하는데 build 하는 경우네는 입력을 할 수가 없음   

> 빌드 완료 후 exec, run 등으로 tty로 하는 것은 얼마든지 가능  

## echo로 입력을 대신해서 넘겨줄 수 있다

일반 유저로 sudo 사용할 때 비번 넘겨주기  
```
echo "pass" | sudo -S apt update
```
예:
```
RUN echo "user" | sudo -S chmod 777 /home
```

비번이 노출이 되므로 적절히 사용해야할 듯 하다  



## docker USER

USER 키워드를 이용해서 사용자를 바꿀 수 있다  
`USER root`

보통의 docker compose build 시에는 root로 진행되는 것이 많으나 간혹 유저로 관리자 권한 없이  
사용되야 할 경우 유저를 만들 수가 있는데   

```Dockerfile
ARG USER=my_user
ARG HOME=/home/my_user

RUN useradd -m $USER  && \
    ## password
    echo "$USER:password" | chpasswd && \
    ## root privileges, (sudo install필요)
    adduser $USER sudo && \
    cp /root/.bashrc $HOME
```

위의 password 라고 한 부분이 비번으로 등록되게 된다.   
이상하게도 $USER은 환경변수에서 가져오는데 (ARG), 패스워드는 환경변수를 만들고 해도   
패스워드 등록이 이상한 값이 들어가는 듯하다.   

아마도 , ENV, ARG 에서 잘 못가지고 오는 듯??

어쨋든 차라리 저 부분을 shell script로 만들어서 COPY를 한 후에 실행을 하는 것도 방법이다. 

비번같은 경우는 미리 다른 파일에서 불러와서 읽은다음에 수행하고, 숨겨 놓고 (깃허브등에는 올리지 않는다)  
라고 하면 쬐금(?) 보안이 좋아진다 ㅋㅋ

대충.. 
```Dockerfile
COPY ./scripts/* .\ 

WORKDIR /
## Create user 
RUN /bin/bash -c "./create_user.sh"
```

update해야함!!