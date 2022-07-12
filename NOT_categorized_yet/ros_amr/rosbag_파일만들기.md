rosbag --help를 적극 활용한다 

-a 옵션은 모든 topic  
-O 옵션은 파일 이름 저장할 수가 있다  

예
```
rosbag record -a -O bag_test.bag
```


rosbag파일 플레이 시키기, publish가 된다   
rosbag play --bags=파일명
