# wheel joint 에서 axis
wheel link 관련 joint 를 만들 때  
axis 부분에서 해당 링크의 rpy 를 확인한 후에 맞춰서 넣어주는데  

모델에 meshes 파일이 있는 경우에는 다 그렇지는 않겠지만  
모델 자체가 누워있는 경우가 많음   

그래서  wheel 의 link 부분에서 roll 로 회전을 해줘서 사용해야 하는 경우가 있음  
이렇게 회전이 되어서 바퀴가 제대로  rviz에서 보인다면  

해당 바퀴에서 xyz 를 본 후에 맞는 축을 선택해서 넣어준다.

예를 들어 바퀴를 roll 시킨 후에, 축이 z 축이라면 
```xml
<child>right_wheel</child>
<axis>
    <xyz>0 0 -1 </xyz>
// 생략
```
물론 z축 방향에 따라서 1, -1 선택  

간혹 meshes 파일에 따라서 link 의 방향을 바꿔야 할 수도 있음


