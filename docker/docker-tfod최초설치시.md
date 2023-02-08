현재 codingClass 깃허브에 
codingClass/setup installation txt_files/tensorflow_docker환경.md 
파일비교 후 업데이트 해주기

참고로 우분투 이미지 없어도 됨 지우기

1. 먼저 자신의 Workspace 디렉토리나 (아무곳) 에 디렉토리 만든 후
```
mkdir -p Workspace/docker-tfod
cd docker-tfod
```

2. git 클론하기
```
git clone https://github.com/terrificmn/tensorflow-od.git
```

3. tensorflow-od 디렉토리가 생겼을 것이고 src로 디렉토리명을 변경해준다.
```
mv tensorflow-od src
```

4. 깃허브에 push가 안되어 있는 파일들이 있다. 깃이그노어 파일들  
```
├── data
│   ├── images
│   └── videos
├── enet_data
│   └── enet-cityscapes
├── models
│   ├── community
│   ├── official
│   ├── orbit
│   └── research
└── yolo_model
```
각 디렉토리를 src 디렉토리로 복사시켜준다. 

어쨋든 data 디렉토리 안에 coco_classes.txt 파일과, yolo.h5 파일이 위치해야한다   

그리고 yolo_model 디렉토리 안에는 yolo_model.py, darknet53.py 가 위치해야한다   

 > data파일은 google드라이브 확인 

5. docker-compose.yml, Dockerfile, requirements.txt 을 상위 디렉토리로(docker-tfod) 복사 시켜준다   
```
cp Dockerfile docker-compose.yml requirements.txt ../
```

잠깐!!   
여기서 그냥 복사 안하고 docker-compose 에서 그냥 파일들 경로만 바꿔서 해줘도 됨  
뭐가 나을 지 생각후 결정. 경로 변경해줄꺼면 깃허브 업데이트 시켜주기


6. 상위 디렉토리로(docker-tfod) 이동 후 build를 해준다
```
cd ..
docker-compose build
```

7. 도커 업
```
docker-compose up
```


### 에러 트러블 슈팅
새로운 에러 
RROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
tf-models-official 2.9.2 requires tensorflow~=2.9.0, but you have tensorflow 2.2.0 which is incompatible.
tensorflow-text 2.9.0 requires tensorflow<2.10,>=2.9.0; platform_machine != "arm64" or platform_system != "Darwin", but you have tensorflow 2.2.0 which is incompatible.


또한 이런 에러 일 경우에는 
```
module 'tensorflow.compat.v2.__internal__' has no attribute
```

requirement.txt 파일에서   
tensorflow==2.2.0   
keras==2.3.1 으로 맞춰준다 

