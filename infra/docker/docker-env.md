# Docker에서 env, arg 의 이해  

## .env파일
일단 .env 파일을 많이 활용을 했었는데 docker-compose.yml 파일에서만 인식한다  
같은 디렉토리에 있어야 한다  
USER=me  - .env 파일에서   
${USER} 식으로 사용 - yml파일에서     


## ARG
그리고 ARG는 Docker image를 만들 때 사용된다 즉 build-time variables. 임  
그래서 RUN 으로는 사용 가능 하다  (빌드가 끝나고 컨테이너가 up 되는 순간에는 사용 못함)
그래서.. 컨테이너가 시작되었을 때에는 사용이 안됨  
ENTRYPOINT, CMD 등에서 사용 못함  

ARG Dockerfile 에서 사용 시 
```
ARG BUILDTIME_VARIABLE=default_value
``` 

그리고 변수를 사용할 때에는 `$BUILDTIME_VARIABLE` 이렇게 써주면 되는데  
docker_compose에서 쓰이는 ${} {}로 묶는 방식은 인식을 못함

docker-compose.yml 에서는 아래처럼 사용
```
args:  
    VARIABLE_NAME: a_value
```
그리고 중요한 것이 RUN 에서만 변수를 사용할 수 있고 거의 다 사용 못하는 듯 하다  

예를 들어 ARG 변수를 USER, WORKDIR 등에서 사용이 안된다 
```
ARG USER=me
USER $USER  #변수를 인식 못함
```

## ENV
ENV 는 컨테이너에서 사용가능, RUN 커맨드도 사용가능   
ENV 도 빌드할 때 사용 가능하다. 그리고 빌드가 끝난 후에도 사용이 가능함
사용예  
```
ENV TERM xterm
# a default value
ENV foo /bar
# or ENV foo=/bar
```


### 빌드했던 ARG를 ENV로도 지정을 해서 사용할 수가 있다
```
ARG MY_NAME

### 이것을 ENV로 설정
ENV MY_ENV_VAR=$MY_NAME
```
이제 빌드가 된 후에도 같은 것을 사용할 수 있음




docker-compose 에 env_file 로 파일로 직접 위치를 설정해주는 것이 있는데  
```
services:
  web:
    image: examle
    env_file: env_file_name
```

따로 env_file을 만들고 (현재 디렉토리가 기본) 파일명을 해주고 빌드 하면   
환경변수가 설정이 안된다고 나옴   

실패- 일단 Dockerfile에서는 ARG/ENV 를 사용하고, docker-compose에서는 .env 파일을 사용하기로...



