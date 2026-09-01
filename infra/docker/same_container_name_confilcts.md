## 같은 이름의 컨테이너 충돌
```
Error response from daemon: Conflict. The container name "/npm" is already in use by container "a8f6cd3a3b51daced4f412643fa8034fd91f3f4ccf65325c310ff0b2c6a5f4d6". You have to remove (or rename) that container to be able to reuse that name.
```
이름이 같을 경우 docker compose -p  옵션을 해서 프로젝트 옵션을 넣어줄 수가 있는데  
이렇게 되면 같은 컨테이너 이름이 있어도 다른 프로젝트에 속한 것이라   
같은 이름이라도 사용할 수 있다고 한다.   

> 네임스페이스 같은 기능은 없고, 프로젝트 옵션을 넣어서 할 수 있다.

하지만 테스트 했을 경우, -p 옵션을 넣어서 해도 위의 같은 컨테이너 이름이 사용된다는  
에러는 계속 발생했다.   
혹시 아예 처음부터 프로젝트 명을 넣어서 적용해서 되는지 여부를 확인해봐야 할 듯 하다.   

> 그래도 안된다면 컨테이너 이름을 바꿔서 사용하는 것이 가장 편한 방법

## .env
-p 옵션과 같은 효과를 줄 수 있는 것이 docker compose.yaml이 있는 디렉토리에서  
.env 파일을 만들고 거기에 
```
COMPOSE_PROJECT_NAME=myproject
```
하고 실행을 하면 된다.  

마찬가지로 아예 처음부터 모든 프로젝트에 프로젝트명을 부여해서 해봐야 할 듯 하다.   

