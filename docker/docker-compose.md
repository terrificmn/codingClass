docker-compose.yml 파일에서 설정을 바꿀 경우에는 docker compose build를 다시 않하고도 잘 되는 듯 하다   

> compose.yml 파일이 파라미터를 받는 것 같다. 그래서 기존의 빌드된 것에서 내용만 다르게 실행되는 것 같음  

하지만 Dockerfile에서 내용이 바뀌는 경우  
COPY, ENTRYPOINT 등 스펠링이 다르거나, 틀릴 경우에는 docker-compose up으로는   
이미 예전 빌드 된 내용을 실행하기 때문에 계속 에러가 나고 다시 docker-compose build를 해줘야한다   

(COPY등은 host컴에서 파일을 복사하는데 예를 들어 example.sh 파일을 복사하는데 그 내용을 수정했다면은  
자동반영이 안되고 다시 build를 해줘야한다)




