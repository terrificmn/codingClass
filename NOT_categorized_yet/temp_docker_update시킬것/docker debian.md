debain buster 10 에서 docker-compose build를 하는 중에 
`Country of origin for keyboard` 라고 나오면서 키보드를 지정해달라고 나오면서 
더 이상 진행이 안 되는 경우 (입력이 안되고 계속 대기 상태에 있게 된다)

Dockerfile 에 변수를 하나 설정해준다. 

```
FROM=.....
DEBIAN_FRONTEND=noninteractive
```

다시 빌드를 해주자. 그러면 막힘없이 잘 진행이 된다

