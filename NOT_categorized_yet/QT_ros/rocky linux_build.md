qtcreator-ros를 빌드를 설치하기 위한 dependenceis 이지만..

```
sudo dnf install mesa-libGL-devel ninja-build yaml-cpp-devel utf8proc-devel 
```

이 것만으로는 불충분함...

Could NOT find XKB  XKB 위치를 찾지 못하고, (설치는 되어 있는 듯)   
빌드는 되고, ros plugin을 만들어 준다
단, qt creator를 실행 후 빌드 후 실행을 하면 그래픽 화면을 잘 띄우지 못함

원인을 못 찾음.  
정식 qt 공홈에서 opensource 버전으로 qt creator를 설치를 해도 결과는 같음.. 
qtcreator만 설치를 했을 때 안됨.   
다른 qt 및 다른 것들을 설치를 하면 되었던 것 같은데 용량을 많이 차지함 
(최초 design studio? 와 qt 5버전을 설치한 듯 함 )

> dnf 패키지로 qt5 버전을 설치할 수가 있는데 5.15 버전이다

qtcreator가 8버전인데~ 아직 Rocky Linux 8.5 기준으로는 아직 잘 안되는 것 같음

그래서 
## dnf 로 설치를 하고 그냥 사용하고  
qtcreator 4 버전과 qt5.15 버전으로 작성한 project가 ubuntu에서도 잘 돌아간다면  (호환))

Rocky Linux에 다는 적당히 설치를 하고 연습 하는 것이...
그리고 ubuntu에 설치를 한 것으로 사용하는 것이 맘편할 듯 하다  

> snap버전은 파일 경로를 설정거나 할 때 에러가 발생하며 제대로 실행이 안된다  
> 이것은 ubuntu 버전도 같음   


결론: 
빌드는 되기는 하나, qt공홈-qtcreator  설치는 잘 되나   
project실행시 그래픽화면 제대로 안나옴  

dnf 패키지에서 제공하는 qtcreator 4. 버전을 그냥 사용해야겠다~
그리고 qt버전은 5.15버전임 

또는  
qt 공홈에서 다운 받아서 설치를 할 경우에는  
기존의 qt 5.15 와 호환이 잘 안되는 듯 하다. 그래픽 화면은 실행을 했을 때 오래걸리고 제대로 표시를 못함  
빌드로 생성한 qt 6.3 은 아예 crash가 되고  


Qt Creator 8.0.1 Debug Symbol
Qt Creator 8.0.1 Plugin Development
Cmake, Ninja 등만 설치를 했는데 Qt는 생략    
qt 버전까지 제대로 설치를 해야하는 듯 하다 
qt 5.15.2 버전 gcc 64만 추가로 update함- 그래도 실패
(아마도 거의 풀버전으로 해야지 작동하는 듯 하다. )

아마도.. ubunut에서 하는게 맘 편할지도 모르겠다  
.**
#### ros plugin이 작동하는지 테스트



