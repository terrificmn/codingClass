# disply invert하기

디스플레이를 거꾸로 표시 해야할 경우
```
DISPLAY=:0 xrandr -o inverted
```

*-o* 옵션에는 normal,inverted,left,right,0,1,2,3 등이 있음  


## 터치 가능 시 터치도 바꾸려면 
```
DISPLAY=:0 xinput list
```
로 확인

Virtual core pointer 에서 해당 장치를 선택해주면됨  
예를 들어서 WaveShare WS170120 이라면 이것을 선택해서 바꿔줘야하는데   
Coordinate Transformation Matrix를 바꿔야 한다   

9개의 요소를 가진 배열의 형태로 바꿔줘야함
```
DISPLAY=:0 xinput set-prop "WaveShare WS170120" --type=float "Coordinate Transformation Matrix" -1 0 1 0 -1 1 0 0 1
```

다만 2D transformation matrix 라고 하는데, 전체 스크린의 width/height = 1 로 normalised 된 상태라고 하는데  
숫자에 대해서는 잘 모르겠음   

모니터를 뒤집어서 설치했을 때 한번 해볼만 한 것도 같지만, 장치가 같다는 보장도 없고   
다시 원래 상태로 터치 input을 바꾸는 방법도 알아봐야 할 듯 하다   

> 어쨋든 참고로만 알고 있자.

