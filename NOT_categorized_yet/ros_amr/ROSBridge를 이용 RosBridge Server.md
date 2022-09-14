먼저 간단한 패키지를 만들고 html 파일을 만들어 준다  

파이썬 서버를 이용해서 웹 브라우저에서 사용할 수 있게 한다  

```
cd catkin_ws/src
catkin_create_pkg webpages
```

위와 같은 방법으로 간단하게 패키지를 만들고 webpages 디렉토리 안에 index.html 파일을 만들어준다   

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ros_web_test</title>
</head>

<body>
	<h1>hello from ROS</h1>
	<p>Communicate to robots from my web</p>
</body>
</html>
```

그리고 나서 파이썬3를 이용해서 서버를 실행    
일단 서버가 실행된 곳에서 index.html 를 읽는 듯 하다

먼저 실행은 
```
cd webpages
python3 -m http.server
```

이제   
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ... 메세지와 함께 웹서버가 시작된다 

이제 웹 브라우저에 http://localhost:8000 로 또는 ip주소로 접속하면 된다   


## ROSBridge

rosbridge 관련 런치파일을 실행해준다
```
roslaunch rosbridge_server rosbridge_websocket.launch 
```
설치는 이미 되어 있으나, 없다면 
```
sudo apt install ros-noetic-rosbridge-server
```

rosbridge websocket server는 9090번 포트를 이용하게 된다 

가제보 시뮬레이션을 실행해준다. 터틀봇3 등..  
rosbridge를 이용해서 topic을 퍼블리싱하는데 시뮬레이션으로 볼 수가 있다  

그리고 다시 webpages 의 index.html에 script를 추가해준다 

```js
<script type="text/javascript">
	var ros = new ROSLIB.Ros({
		url : 'ws://localhost:9090'
	});
	
	ros.on('connection', function() {
		console.log('Connected to websocket server.');
	});
	 
	
	ros.on('error', function(error) {
		console.log('Error conecting to websocket server: ', error);
	});
	
	ros.on('close', function() {
		console.log('Conection to websocket server closed.');
	});
	
	  
	// publishing a topic
	var cmdVel = new ROSLIB.Topic({
		ros : ros,
		name : '/cmd_vel',
		messageType : 'geometry_msgs/Twist'
	});
	
	var twist = new ROSLIB.Message({
		linear : {
			x : 0.2,
			y : 0.0,
			z : 0.0
		},
		angular : {
			x : 0.0,
			y : 0.0,
			z : 0.0
		}
	});
	
	
	console.log("Publishing cmd_vel..");
	cmdVel.publish(twist);
</script>
```

스크립트에서 ROSLIB.Topic, ROSLIB.Message 등을 이용해서  객체를 만들고   
각 value를 넣어주면 된다.  
이를 테면 Twist 메세지 같은 경우에는 rosmsg 를 터미널에서 입력해서 어떤 Type인지 알 수 있다 
```
rosmsg show geometry_msgs/Twist
```

다른 타입들도 이런식으로 확인하거나 구글링!
```
geometry_msgs/Vector3 linear
  float64 x
  float64 y
  float64 z
geometry_msgs/Vector3 angular
  float64 x
  float64 y
  float64 z
```
여기에서 각 상위 개념의 변수 linear,  자식개념(?)의 x, y, z 는 Javascript에서 json 형식으로 써주게 된다 

그리고 script의 ROSLIB (js라이브러리)를 head 태그에 추가해준다  CDN 방식으로 넣어준다  
해당 링크는 

[깃허브 RobotWebTools/roslibjs 에서 Usage부분을 살펴보자](https://github.com/RobotWebTools/roslibjs)  

[여기는 http://robotwebtools.org](http://robotwebtools.org/#libraries)

그래서 위의 링크에서 CDN (min) 부분 링크를 복사해서 head 태그에 넣어준다  

```html
<head>
	<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/roslib@1/build/roslib.min.js"></script>
</head>
```

이제 웹 브라우저를 다시 새로고침을 하면 body에 입력했던 내용들이 나오고  
javascript로 console.log()했던 부분을 보려면  
Ctrl+Shift+C (파이어폭스 기준) 을 누른 후 
Console 탭을 보면 메세지가 나오는 것을 알 수 있다  

그리고 연결이 되고 Publishing cmd_vel... 메세지가 나오고   
가제보 시뮬레이션을 보면 cmd_vel topic을 받아서 움직이는 모습을 볼 수가 있다   

