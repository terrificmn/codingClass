# app release in the docker
Dockerfile 의 마지막에 넣어준다.
```
WORKDIR ${HOME}/my_app/release
CMD ["./my_app"]
```

해당 바이너리 파일 실행하게 하면 실행이 된다. 

단 파일이 없거나 하면 컨터이너가 실행이 안되거나 재실행이 되어 있다면 계속 재실행하게 되고  
결국은 docker exec 로 접근할 수가 없다. 


이때 docker-compose.yml 파일에 
command 를 넣어주면 debug 용으로 컨테이너를 계속 유지할 수가 있다. 

```
command: tail -f /dev/null
restart: no
```

이렇게 하면 컨테이너는 유지가 되고 접근할 수가 있지만, 다시 빌드를 하거나 해당 파일을 복사하고  
다시 command 를 삭제하고  
Dockerfile의 CMD가 실행되게 하면  

다시 컨테이너가 새롭게 만들어지면서 복사/빌드 했던 파일이 없어지게 된다.  
그래서 계속 도돌이표, 파일이 없으므로 CMD ["./my_app"] 이 실행이 안되는 문제가 발생


## Dockerfile 
COPY (source 또는 binary)
또는 직접 빌드 커맨드를 넣어줘서 빌드를 하게 해서 해당 컨테이너에 파일이 계속 유지가 되게 한다. 

또는 development 에서 많이 사용할 수가 있게 하는 방식은   
volumn 을 추가해놓고 해당 파일을 계속 잘 읽어 올 수 있게 해주기 

TODO: 추가 기록