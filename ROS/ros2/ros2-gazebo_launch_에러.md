launch 파일을 이용해서 gazebo 실행을 할 때 
아래와 같은 에러 발생할 때
```
[gzclient   -2] gzclient: /usr/include/boost/smart_ptr/shared_ptr.hpp:734: typename boost::detail::sp_member_access<T>::type boost::shared_ptr<T>::operator->() const [with T = gazebo::rendering::Camera; typename boost::detail::sp_member_access<T>::type = gazebo::rendering::Camera*]: Assertion `px != 0' failed.
```

gazebo의 setup파일을 source를 먼저 해준다
```
. /usr/share/gazebo/setup.sh 
```





