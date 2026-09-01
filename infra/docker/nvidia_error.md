# nvidia 에러 관련
아래와 같은 에러가 발생하는 경우
```
nvidia-container-cli: initialization error: nvml error: driver not loaded: unknown
```

nvidia-docker2 관련해서 설치가 되어 있음에도 불구하고 unknown이 발생한 경우   
그래픽 드라이버가 제대로 설치가 안 되어 있는 경우도 있다   

## 그래픽 드라이버 설치
Nvidia 사이트에서 자신의 그래픽 카드에 맞춰서 드라이버를 설치해 줄 수도 있고   

또는 우분투라면 추천해주는 것을 설치할 수도 있다   

```
sudo ubuntu-drivers devices
```

가능한 드라이버들이 검색이 되어 출력이 되는데   
그 중 `nvidia-driver-000 - distro non-free recommended` 이런식으로 나온다   

해당 그래픽 드라이버 번호를 입력해서 설치를 하면 된다   
예를 들어서 410 이라고 하면  

```
sudo apt install nvidia-driver-410
```


> secure boot 관련해서 나올 수도 있으나, 그래픽 드라이버 설치하면서 따로 나오지는 않음   
만약 secure boot 관련해서 나오면 ok 후 password를 설정해 준다   
그리고 재부팅을 하게 되면 MOK management 화면으로 넘어가는데 키를 찾아보는 경우가 아니라면  
continue boot 를 눌러서 진행 후 설정한 패스워드를 눌러준다. 그리고 재부팅을 할 수가 있다   


## 다시 docker
도커에서 다시 `docker compose up` 등을 해보면 에러 없이 잘 실행이 된다   



