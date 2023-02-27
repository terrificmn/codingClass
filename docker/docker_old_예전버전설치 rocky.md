
최신 stable 버전을 23을 받았다가 원하는 대로 작동을 안해서   
> 하지만.. 버전 문제는 아닌 듯 하다ㅠ

버전을 내려서 설치를 해봄   

참고로 버전 명시해서 dnf 인스톨은 **실패**  

> 만약 추후 또 다운그레이드에 실패한다면 rpm을 직접 다운로드에서 시도 권장  아래에서 확인

버전을 찾으려면 먼저 터미널에   
```
sudo yum list | grep docker-ce
```
그러면 아래와 같은 결과 표시가 됨   

```
Rocky Linux 9 - AppStream                       4.8 kB/s | 4.5 kB     00:00    
Extra Packages for Enterprise Linux 9 - x86_64  7.7 kB/s | 8.4 kB     00:01    
Extra Packages for Enterprise Linux 9 - x86_64  6.5 MB/s |  14 MB     00:02    
docker-ce.x86_64                3:23.0.1-1.el9                  docker-ce-stable
docker-ce.x86_64                3:23.0.0-1.el9                  docker-ce-stable
docker-ce.x86_64                3:20.10.23-3.el9                docker-ce-stable
docker-ce.x86_64                3:20.10.22-3.el9                docker-ce-stable
docker-ce.x86_64                3:20.10.21-3.el9                docker-ce-stable
docker-ce.x86_64                3:20.10.20-3.el9                docker-ce-stable
docker-ce.x86_64                3:20.10.19-3.el9                docker-ce-stable
docker-ce.x86_64                3:20.10.18-3.el9                docker-ce-stable
docker-ce.x86_64                3:20.10.17-3.el9                docker-ce-stable
docker-ce.x86_64                3:20.10.16-3.el9                docker-ce-stable
docker-ce.x86_64                3:20.10.15-3.el9                docker-ce-stable
Docker CE Stable - x86_64                        30
```
일단 여기에 나오는 패키지들만 설치를 할 수 있고 그 이하 버전은 설치가 안된다 

docker-ce, docker-ce-cli 만 버전 기술이 필요  
3:23.0.1-1 또는 3:20.10.23-3 처럼 나오는데 : 이후의 버전만 필요하다  
> : 이후부터 - 까지  예를 docker-ce-20.10.23

이런식으로 
```
sudo dnf install docker-ce-20.10.23 docker-ce-cli-20.10.23 containerd.io docker-buildx-plugin docker-compose-plugin
```

하지만 buildx-plugin 0.10.2-1 이 호환이 안된다고 하면서 설치가 안된다  

```
You can remove cached packages by executing 'yum clean packages'.
Error: Transaction test error:
  file /usr/libexec/docker/cli-plugins/docker-buildx conflicts between attempted installs of docker-buildx-plugin-0:0.10.2-1.el9.x86_64 and docker-ce-cli-1:20.10.15-3.el9.x86_64
```

중간에 실패했다면 캐쉬에 저장되어 있는 다운로드 받은 것을 지울 수가 있다 (사용한 패키지매니저 사용)
```
sudo yum clean packages
혹은 
sudo dnf clean packages
```

리포지터리에서 지우기 
```
cd /etc/yum.repos.d 
```
로 이동하면 docker관련 repo 파일이 있는데 지울 수도 있다  


**위의 방법으로는 실패**




## rpm으로 직접 다운 후 설치
다행히 rpm파일도 받을 수가 있다. docker engine 관련 페이지를 보면 링크가 있는데   

rocky는 9.1 선택 후 x86_64 후 아마 stable 버전인가 있었던 것 같다   

docker-ce,  docker-ce-cli 등 보이는 5를 다 받아준다(버전에 맞춰서)

다운받은 파일을 rpm -ivh 로 설치를 하려고 하면 의존성 패키지 때문에 안됨  

그래서 해당 rpm파일을 dnf 로 설치해준다 

```
sudo dnf install docker-ce-20.10.15-3.el9.x86_64.rpm docker-ce-cli-20.10.15-3.el9.x86_64.rpm docker-compose-plugin-2.10.2-3.el9.x86_64.rpm docker-buildx-plugin-0.10.2-1.el9.x86_64.rpm containerd.io-1.6.10-3.1.el9.x86_64.rpm docker-ce-rootless-extras-20.10.15-3.el9.x86_64.rpm
```

그런데 docker-buildx-plugin-0.10.2-1.el9.x86_64.rpm 파일이 문제인다 buildx-plugin은 한개 밖에 다운로드를 제공을 안하는데 또 의존성 문제를 일으킨다  

> 추후에 또 docker-buildx-plugin이 문제를 일으킨다면 빼고 해본다 

docker-buildx-plugin 빼고 (현재 Feb26에는 이 방법으로 설치 성공)
```
sudo dnf install docker-ce-20.10.15-3.el9.x86_64.rpm docker-ce-cli-20.10.15-3.el9.x86_64.rpm docker-compose-plugin-2.10.2-3.el9.x86_64.rpm containerd.io-1.6.10-3.1.el9.x86_64.rpm docker-ce-rootless-extras-20.10.15-3.el9.x86_64.rpm
```


### 하나만 지정하면 나머지는 자동으로 설치
`sudo dnf install ./docker-ce-20.10.15-3.el9.x86_64.rpm` 

예를 들어 docker-ce-20.10.15-3 버전을 rpm파일로 설치한다고 하면  
나머지 의존성 파일은 기존 리포지터리 docker-ce-stable 에서 다운을 받아서 설치를 하게 되므로  
모든 rpm파일을 다 받은 후 설치를 하자

```
 Package                    Arch    Version             Repository         Size
================================================================================
Installing:
 docker-ce                  x86_64  3:20.10.15-3.el9    @commandline       21 M
Installing dependencies:
 containerd.io              x86_64  1.6.18-3.1.el9      docker-ce-stable   32 M
 docker-ce-cli              x86_64  1:23.0.1-1.el9      docker-ce-stable  7.0 M
 docker-ce-rootless-extras  x86_64  23.0.1-1.el9        docker-ce-stable  3.8 M
Installing weak dependencies:
 docker-buildx-plugin       x86_64  0.10.2-1.el9        docker-ce-stable   12 M
 docker-compose-plugin      x86_64  2.16.0-1.el9        docker-ce-stable   11 M
```




