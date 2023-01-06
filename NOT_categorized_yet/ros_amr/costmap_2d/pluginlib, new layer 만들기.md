
new layer 등록
http://wiki.ros.org/costmap_2d/Tutorials/Creating%20a%20New%20Layer

참고
http://wiki.ros.org/pluginlib  


정확하지는 않음.. 공부 중..

1. navigation 패키지를 따로 깃 클론 해야한다 
2. simple_layer 클래스를 만드는 예제 처럼, 따로 클래스를 만들어서 등록을 해준다 
3. costmap_2d 패키지에 costmap_plugin.xml, package.xml 파일에 적용
4. move_base 용 파라미터에 global_costmap, common_costmap 등에 플러그인을 등록

