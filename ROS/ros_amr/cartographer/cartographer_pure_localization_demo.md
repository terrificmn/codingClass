## demo 실행

bag파일은 다를 수 있다 

먼저 2개의 파일이 필요함
[카토그래퍼 doc에서 다운로드](https://google-cartographer-ros.readthedocs.io/en/latest/demos.html#pure-localization)

첫 번째, 두 번째 파일 모두 필요하다  
첫 번째 bag 파일로는 슬램, localizaiton을 하고, 두 번째 파일은 로컬리제이션을 할 때 로봇이 움직임(?) bag 파일

먼저 다운 후에 런치파일 실행해서 슬램 및 최적화 작업을 기다린다
```
roslaunch cartographer_ros offline_backpack_2d.launch bag_filenames:=${HOME}/Downloads/b2-2016-04-05-14-44-52.bag
```

먼저 실행을 한 후에 맵핑을 다 하게 되면  맵이 다 만들어지고   
맵이 조금씩 틀어져있는데 최적화 작업을 하게 된다. 계속 나두면   
Optimizing: Done.  과 함께 끝나게 된다. 맵도 정상적으로 만들어진다   
그리고 pbstream이라는 파일도 생성이 됨   (Downloads에 bag파일이 있어서 같은 위치에 만들어짐)   

b2-2016-04-05-14-44-52.bag.pbstream

이제 ctrl+C 로 종료한 후에  pure localization 실행

```
roslaunch cartographer_ros demo_backpack_2d_localization.launch \
   load_state_filename:=${HOME}/Downloads/b2-2016-04-05-14-44-52.bag.pbstream \
   bag_filename:=${HOME}/Downloads/b2-2016-04-27-12-31-41.bag
```

load_state_filename 아규먼트에는 pbstream 파일을 지정해준다    
bag_filename에는 끝자리 ...52.bag 파일이 아닌 두 번째 파일인 ...41.bag  파일로 지정



