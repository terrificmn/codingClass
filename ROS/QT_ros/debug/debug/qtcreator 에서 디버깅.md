## Run 부분에 rosrun으로 설정해주는 방법
qtcreator의 왼쪽 화면에서   
Projects -> Build & Run 부분에서   
Run 부분을 클릭한 후 오른쪽 화면 (중앙)에서 Executable을 설정해주면 된다  

Executable에는  `rosrun` 이라고 해주고   
Command line arguments 에는 보통 rosrun 하던 커맨드를 입력해준다 
```
패키지명 노드명
```

Working directory에는 해당 워크스페이스를 Browse해서 클릭 해주거나   
직접 입력한다 `/home/유저명/catkin_ws`

마지막에는 Run in terminal 에 check 버튼을 눌러서 실행하게 설정해준다 

이제 준비는 완료가 되었고 왼쪽 하단의 세모 디버그 버튼을 눌러서 진행하면 된다   



## Attach to Unstarted Application 
Debug 메뉴 -> Start Debugging 에서 
Attach to Unstarted Application 을 눌러서  새로운 창이 뜨면  
Executable 에 
```
"${CATKIN_WORKSPACE_FOLDER}"/devel/lib/패키지명/노드명
```
또는 (/home/catkin_ws)로 해줘도 됨, 그리고나서 Start Watching을 눌러준다   

그리고 터미널에서 해당 노드를 rosrun 해주면 된다    


## Attach to Running Application
이 부분은 vscode에서 디버깅과 비슷하다   

터미널에서 먼저 rosrun으로 노드 실행을 시킨 후에   

Debug 메뉴 -> Start Debugging 에서    
Attach to Running Application 을 클릭한 후에   
Filter 부분에서 검색을 해주면 된다  

> 잘 안 될 수 도 있음








