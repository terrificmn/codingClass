ROS_WARN("true or false : %d", getReadNGo());

ROS_WARN("true or false : %s", getReadNGo() ? "true" : "false");

%d는 정수형
%s는 string  

첫 번째는 true/ false는 1, 0으로만 표시가 된다.   
좀 더 보기 좋게 출력하려면   %s에 if(?) 문을 사용해주면 좋다

