# Rocky Linux docker 설치
버전 업이 많이 되어서 몇개의 명령어면 설치 끝!
```
sudo yum install -y yum-utils
```

```
sudo yum-config-manager \
--add-repo \
https://download.docker.com/linux/centos/docker-ce.repo
```

최근에는 docker-compose도 plugin으로 바로 설치가능한 듯 하다
```
 sudo yum install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

## 시작
```
sudo systemctl start docker
```

## 버전 확인
설치가 잘 되었는지 확인  
```
docker version
```


위에서 docker-compose를 plugin형태로 설치를 했기 때문에 예전 처럼 docker-compose 명령어로 사용하지 않는듯 하다  

한칸 띄운 다음에 사용
```
docker compose version
```

