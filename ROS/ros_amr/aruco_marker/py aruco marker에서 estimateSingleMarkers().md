
```python
rvec, tvec, markerPoints = aruco.estimatePoseSingleMarkers(corners[i], 0.05, matrix_coefficients, distortion_coefficients) # markerLength width 0.1m
```

이런식으로 사용을 할 때, 두 번째 아규먼트가 marker length라고 하는데 이 길이를 통해서 줄여주면
pose 데이터를 예측해서 나오는 tvec 에서  z 값이 distance가 되는데 이것을 좀 줄여줄 수 있다  

> 사실 임시 방편;;;;

일단 카메라를 calibration을 하면서  
```json
K: data: [ 1659.3723, 0., 639.5, 
		  0., 1659.3723, 359.5, 
		  0., 0., 1. ]
```
이런 데이터가 나오면 예를 들어 여기에서 1659는 초첨 거리가 되는데 이 데이터를 통해서 카메라와 
pose간의 거리가 결정되는 것 같다.   
> 
> 요 크기가 적어지면 pose 값 tvec의 3번째 요소인 z 값도 줄어든다 

조금 더 연구를 해봐야겠다.  
아마도 목표는 위의 marker length를 0.05 로 두고, (4x4 50으로 marker를 만들었을 경우에)   
카메라의 calibration을 좀 더 잘 하는 방향으로....