# docker 컨테이너 안에 WiringPi Library 설치

처음에 tinker board 2 상태에는 gpio 관련 wiringPi가 잘 설치되어 있다.   
하지만 docker 를 사용할 때에는 gpio 라이브러리를 사용을 해야하는데 당연히도(?) host 컴퓨터의 wiringPi 라이브러리를 인식하지 못한다 

먼저 wiringPi 압축 파일을 공유 디렉토리로 이동해준다(또는 복사)

```
mv ./wiringPi.tar.xz ~/Workspace/docker-ws
```

> 공유된 디렉토리가 docker-ws라고 가정

그래서 도커를 up한 후에 컨테이너 안에 설치를 해주자
`docker-compose up`  후에 

```
docker exec -it ros bash
```

bash 쉘로 들어간다.  

다시 컨테이너 내의 /usr/local/share 디렉토리로 이동시켜줘야한다.   
```
mv ./wiringPi.tar.xz /usr/local/share
```

압축 풀기
```
cd /usr/local/share
tar xvf wiringPi.tar.xz
```

압축이 풀렸다면 해당 디렉토리로 들어가서 빌드를 해주면 끝
```
cd wiringpi_c_3399
sudo ./build
```
> 해당 디렉토리명은 정확히 기억이;;;



All Done. 이라고 나오면 잘 설치가 된 것 이다   
컴파일할 때 -lwiringPi 요렇게 옵션을 넣어서 해주면 된다   



