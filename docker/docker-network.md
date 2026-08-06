# docker network
docker 에서 잘 사용하던 network 가 갑자기 안된다.   
db 접속을 할 때 mysql 서비스 이름으로 접속하면 잘 되야 하는데, 갑자기 mysql 를 찾지 못하는 현상이 발생  

failed to connect: Unknown MySQL server host 'mysql' (-2)

Unknown 으로 전혀 찾지를 못한다.  

일단 의심은 같은 서비스 이름인 mysql 로 다른 프로젝트에서 또 사용을 하고 있다는 점,   

단, 컨테이너 이름은 다르고, 프로젝트 자체도 다르다, network 도 다르게 사용하고 있다.  


일단, docker network 를 찾아보면  

```
docker network ls
```

로 찾아볼 수가 있는데 여기에서 나오는 내가 현재 사용하고 있는 프로젝트의 network 를 inspect 를 할 수가 있다. 


```
NETWORK ID     NAME                DRIVER    SCOPE
8af2d99372cb   bridge              bridge    local
b2229e23465b   host                host      local
ad5r561179d   my-api   bridge    local
```

여기에서 my-api 의 network를 찾아보면 
`docker network inspect my-api`  

결과 
```
[
    {
        "Name": "my-api",
        "Id": "ad5r561179d486f210a455da185d7bbadfba912e87a02a423d218eca0cd3799",
        "Created": "2026-08-03T17:56:37.746706296+09:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv4": true,
... 생략 
    "Containers": {
            "17321a0e87a70651eaf927f3c53ed7da5737096384b060153fcdc098e0feaf29": {
                "Name": "my_nginx",
                "EndpointID": "25339efe411edb4dc6ad5040a52805fc37d2d3dc9fff43655741353ad4093fbf",
                "MacAddress": "91:d0:f3:46:ef:d7",
                "IPv4Address": "172.18.0.3/16",
                "IPv6Address": ""
            },
            "663516021d0b81ee05c5ec7a80d9763922197d09903188a55aa53b5aa0430e13": {
                "Name": "my-other-container1",
                "EndpointID": "748bad1d1d564c2d4c219509095ab14d0b3dd72c9a03b8343e2c22e33316d7da",
                "MacAddress": "d2:f0:e5:18:74:65",
                "IPv4Address": "172.18.0.5/16",
                "IPv6Address": ""
            },
            "ea6ebf7ded2cf071beef5a626e02a813f39eea110b3a442dd6e08c14cff62ed5": {
                "Name": "my-other-container2",
                "EndpointID": "1be82810cf43be06f851e50a1935dab2e87ff6b9846beb5d191b7a0a03ab442a",
                "MacAddress": "91:6c:e2:4a:c7:7c",
                "IPv4Address": "172.18.0.4/16",
                "IPv6Address": ""
            },
            "f7b1400ad65a216b5e9f82d5f79d7ad5d1e2f4872dba72e2df48a623fd6312c9": {
                "Name": "my_mysql",
                "EndpointID": "eb7f5570c7d0d1d59d38ff2845ec2d2e5e26a74ad20b7c45caa2719e71f66c2e",
                "MacAddress": "71:4d:2a:f3:7c:42",
                "IPv4Address": "172.18.0.2/16",
                "IPv6Address": ""
            }
    }
]
```

위 처럼 컨테이너 중에 mysql 이 설정한 (container_name 으로 설정한) 이 꼭 나와야 한다.  
이번 케이스에는 my_mysql 컨테이너가 빠져있었다.  아마도 다른 도커 컨테이너를 정리한다고 docker prune 등을 했었는데  
아마도 이때 네트워크 등이 지워지면서 제대로 설정이 만들어지지 않은 듯 하다.  


### network 삭제
다시 실행하려면  

현재 docker container 를 down 시킨 후에 network 를 삭제해준다. network가 다 삭제가 되지만 어쩔 수 없다 ㅠ  

```
cd ~/current-my-docker-project
docker compose down
docker network prune
docker compose up
```

이렇게 하면 다시 network 설정이 다시 잘 만들어져서 도커 내부에서 mysql 로 접속을 시도했을 때   
해당 컨테이너를 잘 찾아서 접속해 준다.  


