이미지 파일등을 등록을 해서 사용을 할 수가 있는데 바로qrc 파일이다   

프로젝트가 열려있는 상태에서  
New file 그리고Qt를 선택 후  Qt Resource File 선택  
file이름을 (resources)지정해주고 Path를 지정 해준다  

이제 Edit창에 resources.qrc 파일이 생긴다  

파일을 클릭해서 
Add prefix를 할 수가 있다   

원하는 /icon 또는 /image 등 처럼 추가를 해주고  
거기에 file을 추가해주는데  image 파일을 추가해준다   

> 이미지 파일등을 다운받은 후 프로젝트 디렉토리에 위치 시켜준다

저장을 꼭 해주고  

mainwindow.ui 디자인 화면에서   

버튼 등에서 현재의 이미지를 사용할 수가 있게 된다  

버튼을 눌르고 Property에서 icon을 눌러준다음에 
몇개의 항목이 있는데 Normal off, Normal On, 등.. 에서 
... 버튼을 눌러주면 resoure root가 나오고 등록했던 prefix가 나온다 
원하는 이미지를 선택해주면 된다  


아직 미완성!!!
더 공부할 것
