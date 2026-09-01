# docker 용량 
용량 확인 - GUI Disk Usage Analyzer 에서는 안나오는 것이 많음 (permission 때문)   

용량을 얼마나 사용하고 있는지 확인
```
sudo du -sh /* 2>/dev/null | sort -h

#보통 sudo du -sh /var/ 2>/dev/null | sort -h
```

특정 디렉토리 이하를 찾기
```
sudo du -sh /var/lib/* 2>/dev/null | sort -h
```

예를 들어서 결과
```
119M	/var/lib/flatpak
1.4G	/var/lib/systemd
51G	/var/lib/docker
```

docker 컨테이너에서 51G 나 차지 하고 있다.

특히 */var/lib/docker/overlay2* 에 디렉토리가 많은데 사용 안하는 것을 지울 수도 있지만  
매뉴얼로도 지울 수 있지만, 안전하게 하려면 .. 

`docker system prune` 가 가장 안전한 방법. 단, **stop 되어 있는 container도 지우므로**  
사용하는 docker 들을 docker compose up 으로 실행을 해서   
일단 컨테이너를 띄운 다음에 실행하는 것이 가장 좋음  
이렇게 하면 

옵션을 안 사용해도 잘 지워준다. 옵션은 --all --volumes --force 등을 사용할 수 있음  
```
docker system prune
docker system prune --all --volumes --force
```

```
WARNING! This will remove:
  - all stopped containers
  - all networks not used by at least one container
  - all dangling images
  - unused build cache

Are you sure you want to continue? [y/N] y
```
물어본 다음에 나머지만 삭제해 줌  

## symlink 로 용량이 파티션에 연결
예를 들어 /home 파티션 용량이 여유가 있다면, 용량 부족 시 symlink 로 해결하는 방법이 있다.   
기존의 /var/lib/docker 를 /home 으로 이동 시킨 후 심링크를 걸어준다. 

테스트는 안 해봤지만, 꽤 유용할 듯 하다.  
예
```
sudo systemctl stop docker
sudo mv /var/lib/docker /home/docker
sudo ln -s /home/docker /var/lib/docker
sudo systemctl start docker
```

