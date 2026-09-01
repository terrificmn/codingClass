
rostopic list | grep initialpose

> init 정도까지만 쳐도 topic명이 나온다   


amcl 노드에서 subscribe 하고 있다   

msg 타입은  Type: geometry_msgs/PoseWithCovarianceStamped

만들어서 publish를 해주면 된다   

pose.pose.position.x 와 y
pose.pose.orientation.w 를 지정해주면 된다    w=1

msg를 만들어준 다음에 publish를 해주면 될 듯 하다 





