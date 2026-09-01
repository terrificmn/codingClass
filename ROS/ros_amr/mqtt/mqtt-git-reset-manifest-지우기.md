# paho_mqtt 깃 커밋 날려버리기
라이브러리를 find_package() 에서 못 찾는 이유는 ,paho_mqtt_cpp 버전, 또는 commit이 계속 업데이트 되어서   
변경이 된 지점이 있다. 그래서 최신 버전(?)에서는 기존의 mqttpp3 으로만 찾을 수 없게 된다.

`git reset --hard 특정커밋번호` 를 이용해서 기존의 커밋을 다 없애버릴 수가 있다.  

> 단, 아무 커밋을 날려버리면 이상해질 수 있으므로 잘 사용되고 있는  commit 이후로 날려야 한다.  
2023년 Nov 커밋 중에 하나를 사용하면 좋다. 추천( e9db86fa )


## 파일 제거 후 다시 설치 (트러블슈팅)
기존의 파일들이 남아 있는 경우에 문제를 일으킬 수가 있다. 
계속 mqtt 관련해서 연결을 시키면 thread mutex 관련 에러가 발생한다.   
이 증상은 mutex를 lock을 건 후에 unlock을 안 해주는 경우, lock이 안되어 있는데 unlock을 하는 등.. 
어쨋든 그럴 때 에러가 발생한다고 하는데  

기존에 설치되었던 파일을 싹 다 지워주고 다시 빌드를 해주면 잘 된다. 

일단 각각 paho cpp 라이브러리의 build 디렉토리를 보면  
*install_manifest.txt* 파일이 있는데 여기에 어느 경로에 설치를 했는데 알 수가 있다. 

먼저 해당 파일을 읽어서 해당 경로의 파일을 자동으로 지워줄 수가 있다. (한번에)
```
sudo xargs rm < install_manifest.txt
```

이후 install_mainfest.txt 파일을 보고 해당 경로를 다 들어가 본다.  
/usr/local/lib/ /usr/local/include/mqtt, /usr/local/bin, /usr/local/share/doc, /usr/locl/lib/cmake/PahoMqttCpp/ 등이 있음


이제 다시 클론 후 git reset을 진행해준다.  
그리고 cmake 빌드, mqtt_라이브러리_link_catkin_CMakests. 파일을 참고하자  

이제 mqtt 연결해도 깔끔하게 문제 발생안하게 된다. 
