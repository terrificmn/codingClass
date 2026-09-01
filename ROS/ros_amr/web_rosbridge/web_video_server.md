설치는 
```
sudo apt install ros-noetic-web-video-server
```

11315를 기본 포트로 사용하므로 docker를 사용한다면 port를 매칭해준다   

정리필요!!!!


 <script src="https://cdn.jsdelivr.net/npm/eventemitter2@5.0.1/lib/eventemitter2.min.js">
    </script>
    <script type="text/javascript" src="https://static.robotwebtools.org/mjpegcanvasjs/current/mjpegcanvas.min.js">
    </script>



 <div class="col-md-6">
        <div id="mjpeg"></div>
    </div>


rosrun web_video_server web_video_server _port:=11315

java sc
 setCamera: function() {
            console.log('set camera method')
            this.cameraViewer = new MJPEGCANVAS.Viewer({
                divID: 'mjpeg',
                host: '54.167.21.209',
                width: 640,
                height: 480,
                topic: '/camera/rgb/image_raw',
                port: 11315,
            })
        },



로스 브릿지 연결될 때 같이 연결 
            this.ros.on('connection', () => {
                this.logs.unshift((new Date()).toTimeString() + ' - Connected!')
                this.connected = true
                this.loading = false
                this.setCamera()
            })

public_ip 를 통해 ip도 알 수 있다고 함 



