ssh로 접속

디렉토리를 하나 만듬  
```
mkdir streamlit_tfod_docker
```

만든 디렉토리로 이동

이제 깃 클롤을 2개를 받는다. 하나는 스트림릿 프로젝트(내꺼) 그리고 tensorflow-models를 받는다 

```
git clone https://github.com/terrificmn/tensorflow-od.git
```

그리고 레퍼지토리 명으로 만들어진 것을 src 로 이름을 바꾼다 .   
도커에서 만들때 그렇게 설계함 ㅋㅋ  
mv tensorflow-od/ src  
사실 클론 받은 디렉토리 명은 중요하지 않고 (그 안의 .git 으로 되어 있는 부분이 중요하니깐 )  
그리고 디렉토리를 src로 바꿔서 도커에서 인식할 수 있게 한다.  
아니면 도커파일을 바꿔도 됨  
옵션 1 도커의 workdir 부분을 리파지토리 명으로 바꾼다   


d어쨋든 이제 바뀐 src (또는 리파지터리 명)으로 이동  
이 안에서 tensorflow/models 깃을 클론한다 

```
git clone https://github.com/tensorflow/models.git
```

깃 클론이 다 되면 확인
```
ls -l 
```
models가 잘 받아져 있으면 ok!

src디렉토리 안에   
원래 내 프로젝트로 process ,utils 디렉토리가 있고 이제 models까지 생겼으면 잘 하고 있는 것

그리고 깃에서 이그노어 했던 디렉토리를 만들어 줘야한다   
src 디렉토리 안으로 이동  
```
mkdir -p data/images/user-upload
```
만들 필요 없이.. 어차피 sftp로 접속해서 이미지와 필요한 동영상을 업로드 해야하므로   
ftp접속해서 생성한다.


이제 도커 파일을 만들어야하는데 내 리파지터리 속에 포함시켜놓아서 받을 수 있게 하였음   
뭔가 좀 복잡하게 만들었는데;;; 머리를 더 굴려야할 듯 ㅋㅋ

어쨋든 원래는 도커파일 도커 컴포즈와엠엘은 리콰이어.txt 상위 디렉토리에 위치 해야하므로 복사를 시켜준다   
(파일을 어차피 ssh로 작업하는 거라 vi에서 복사 붙여넣기 식으로 하면 되겠지만 그렇게 되면 들여쓰기가 잘 안됬던더 같기도 하고..)  
어쨋든 상위에 복사한 파일은 지우지 않고 나둔다..  
지우면 어차피 다음에 로컬에서 다시 푸시를 하고 aws에서 다시 pull하면 다시 생기거나 뭔가 충돌이 날 수 있으니  
로컬에서 지운다음에 push하기로 한다.. (로컬에서도 src 상위 디렉토리에 위치함 )  

그리고 Dockerfile의 pip3 install 부분에 --no-cache-dir 을 추가해서 캐쉬 생성을 안하고 도커 이미지도 줄인다. 
```
RUN python3.8 -m pip install . --no-cache-dir

RUN pip3.8 install -r requirements.txt --no-cache-dir
```
이부분... (첫번째에서는 pip3로 하면 없는 모듈이라고 나온다.. python 이라고 해도 되지만 3.8로 특정해줌)


그리고 복사, 현재 디렉토리 src 디렉토리 pwd  
/home/ubuntu/streamlit_tfod_docker/src #결과

cp docker-compose.yml Dockerfile requirements.txt ../



이제 준비는 끝난다.. 
```
systemctl status docker
```
도커가 가동 중이 아니라면
```
systemctl start docker
```

빌드하기 전에 라라벨 도커를 중지시켜야 한다.
```
 ps -ef | grep docker
```
그러면 웹서버 등 여러개가 돌아가고 있는데 그중에 공통되는 PPID 가 하나 있다.    
하나를 죽여주면 된다.

그리고 프로젝트 디렉토리의 최상단에서 
```
$docker-compose build 
```
그리고 마무리가 완료되면
```
$docker-compose up
```

정확히 yolo모델이 없다고 나올 것임  
ctrl+c로 도커를 중지시킨다음에   
최종적으로 파일질라 등을 이용해서 데이터파일 이미지 파일등을 업로드 시킨다.  

파일질라 클라이언트 프로그램이 설치가 안되어 있으면 
```
sudo yum install filezilla
```

filezilla 셋팅은 편하다.. new site로 하나 등록을 해주면서   
sftp로 맞춰주고 포트번호는 생략해도 됨  
그리고 아이디 ubuntu,  pem키만 등록해주면 된다.   

이제 필요한 디렉토리는 3개  
로컬의 data, enet_data, yolo_model 3개 디렉토리를 서버의 src 디렉토리 안으로 업로드 시켜준다


다시 docker를 실행시켜준다
```
docker-compose up
```
잘된다.. 유일하게 되는 기능인 세그멘테이션, 이것마저 cpu뻑나지 않을까 걱정했는데.. 딜레이 거의 없이 잘 된다.  
다행임!! 



## 아래는 메모리 부족 에러 --------------

이렇게 끝날리가 없지 ㅋㅋ

tensorflow를 설치하면서 에러발생

```
Killed
The command '/bin/sh -c pip install -r requirements.txt' returned a non-zero code: 137
ERROR: Service 'web' failed to build
```

텐서플로우를 설치하면서 장렬히 전사;;ㅠ

2번째 시도에도 같은 결과

로그 파일을 보면 알 수 있다고 한다
```
tail -f /var/log/kern.log
```
```
oom-kill:constraint=CONSTRAINT_NONE,nodemask=(null),cpuset=591ddda6caebcd035a9c5234a798ae8f0b4ab4aa10cf9d0d4284bdfca24e1895,mems_allowed=0,global_oom,task_memcg=/docker/591ddda6caebcd035a9c5234a798ae8f0b4ab4aa10cf9d0d4284bdfca24e1895,task=pip,pid=5155,uid=0
Apr 27 06:52:40 ip-172-31-34-51 kernel: [4068414.990905] Out of memory: Killed process 5155 (pip) total-vm:1573532kB, anon-rss:798816kB, file-rss:8kB, shmem-rss:0kB, UID:0 pgtables:3116kB oom_score_adj:0
```
뭔가 눈에 들어오는것이 Out of memory

일단.. 도커 컨테이너가 돌아가는게 있어서 종료 시켰다
```
sudo ps -ef | grep docker
```
현재 돌아가고 있는 웹서버가 보인다 

```
root     10249   822  0 Apr07 ?        00:00:01 /usr/bin/docker-proxy -proto tcp -host-ip 0.0.0.0 -host-port 8080 -container-ip 172.20.0.2 -container-port 80
root     10307   822  0 Apr07 ?        00:00:01 /usr/bin/docker-proxy -proto tcp -host-ip 0.0.0.0 -host-port 9000 -container-ip 172.20.0.4 -container-port 9000
root     10356   822  0 Apr07 ?        00:00:01 /usr/bin/docker-proxy -proto tcp -host-ip 0.0.0.0 -host-port 3306 -container-ip 172.20.0.5 -container-port 3306
root     10856   822  0 Apr07 ?        00:00:01 /usr/bin/docker-proxy -proto tcp -host-ip 0.0.0.0 -host-port 80 -container-ip 172.20.0.3 -container-port 80
```

미안하다 ㅠ kill 명령어로 PID를 꺼준다
```
sudo kill -9 822
```
```
sudo systemctl restart docker
```
다시 시작해준다.

---------------------

## 실패 (기록)

결국 cpu 95% 10분 이상 지속되다가 에러   
완전 크리티컬 했나보다 결국은 20분이상 ssh로도 접속 안되서 open support인가를 신청했는데 이마저도   
신청도 잘 안됨. impaired라고 나오면서 신청도 안되고   
재부팅, 인스턴스 중지 다시 시작도 소용없다..  
참고로 인스턴스 중지는 ip주소가 바뀐다. 재부팅은 말그대로 재부팅  

1/2 check passed 나오고 뭔가 문제가 발생했다. 암튼 이 방법 저 방법 다 썻지만 살릴 수가 없었다.  
인스턴스 반납을 하던가. terminate 아예 삭제하는 거  
아니면 restore가 있어서했더니 복구는 되었지만 초기상태로 돌아왔다. 하하하하하;; ㅠㅠㅠ  

좋은 경험? 했다고생각하고   
tensorflow는 여기에다 하면 안되고 학습용이면 로컬에서 gpu를 이용해서 한번해보고   
서버는 gpu달린 서버를 사용하던가.. 안해야겠다 ㅋㅋㅋ  





