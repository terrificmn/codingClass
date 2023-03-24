# AR tag in Gazebo
ar_track_alvar pkg 이용 -- 일단 공식적으로는 melodic 버전으로만 되어 있음

마커 사이즈가 중요   


위의 패키지를 이용해서 aruco marker를 png 파일로 만든다. id 정도를 부여하면 되겠고..   
일단 나머지는 default 설정 사용   



## 이후 blender 이용해야함
**실패!!! 버전이 달라서 안됨;; 예제 영상 처럼 쉽게 안됨; 버전 업 되면서 복잡해진 듯..;;**

New 파일로 연 다음에  
오른쪽 패널에서 Units를 선택해서 Unit system을 Metric으로 해준다  
> m로 설정

큐브 위에서 단축키를 *s*를 눌러주면  축소를 할 수가 있다   
Scale X,Y,Z를 0.1로 맞춰준다  (z는 0.01 정도) 
이게 10cm가 맞는지는 확인을 해봐야 알 수 있을 듯... 


다시 오른쪽 하단의 Material 탭으로  이동 

맨 아래의 Texture 탭으로 이동 후 이미지를 오픈해준다 (없다면 New로 만든 다음에 open을 눌러준다. png만 가능한 듯)   
이제 preview 에 이미지가 보임

메뉴에서 UV editing을 해준다  


실패!!!




[aruco marker gazebo에 모델 spawn하기](https://www.theconstructsim.com/ros-qa-079-add-ar-tag-gazebo/)

[add ar tag in gazebo part2](https://www.youtube.com/watch?v=8aQGe18eGOw)


