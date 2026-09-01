# mjpegcanvasjs 빌드
간단하게 cdn 버전을 사용할 수 있지만, 그렇게 잘 사용하고 있었는데 cdn 서버가 다운이 되었고~  
한 일주일 넘게 계속 다운이 되어 있는 듯 하다. 아마 관리를 안하고 있는 듯 하다   

> robotwebtools.org 자체가 먹통이 된 듯 하다   

CDN을 이용하면 코드 한 줄이면 되고 편하고 빠르고 쉽고, 다운이 되면 못 사용할 수 있다는 것은 알았지만   
실제로 다운이 되는 경우도 처음 보는 듯 하다  

## 빌드
먼저 깃 클론

```
git clone https://github.com/rctoris/mjpegcanvasjs
```

도커 버전을 하려고 했으나, grunt를 이용해서 빌드를 하게 되는데   
경로를 또 잘 못찾아서, container를 만들기 귀찮아서 일반 케이스로 진행  

먼저 npm 설치 (nodejs도 설치해준다)
```
sudo dnf install npm
```
> 우분투는 `sudo apt install npm`

Grunt 를 npm을 이용해서 설치
```
sudo npm install -g grunt-cli
```
> 참고로 이 때 설치된 버전은 1.4.3

깃 클론한 위치로 이동 후 인스톨 또 해주는데, 현재 디렉토리(프로젝트)로 지정해주는 것
```
cd ~/mjpegcanvasjs
npm install .
```

현 디렉토리 (프로젝트) root에서 grunt로 빌드
```
grunt build
```

## 완료
mjpegcanvasjs 디렉토리의 build 디렉토리에 만들어 준다   
mjpegcanvas.js, mjpegcanvas.min.js 로 만들어 준다   

> 다행히 쉽고 간단하다  

이제 자신의 프로젝트안에 적당한 곳에 카피한 후 사용하면 되겠다  
대충 예를 들어서..
```
mkdir -p my_project/js_lib
cp ~/mjpegcanvasjs/mjpegcanvas.min.js ~/my_project/js_lib/
```

그리고 자신의 index 페이지 등에  스크립트로 넣어주면 됨
```html
<script type="text/javascript" src="lib-js/mjpegcanvas.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/eventemitter2@5.0.1/lib/eventemitter2.min.js"></script>
```

> mjpegcanvasjs depends on eventemitter2 
> 그리고 깃클론을 받으면 이미 build 디렉토리에 파일이 있는데 이미 되어 있는 건가??;;;;