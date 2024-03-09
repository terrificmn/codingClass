# cpp fork() 사용하기

std::system() 등을 사용해서 사용할 수 도 있다.   
아래 코드 참고

```cpp
        std::string launch_name = "lidarodom_robot.launch"; 
        std::string launch_arg = " use_rviz:=false";
        //// std::string whole_path = apiBridge.pkg_path + "/launch/" + launch_name + " &";
        /////TODO: to exclude the result via grep, use regular expression 
        // if() {
        //     // ex: ps -ef | grep "[l]idarodom_robot.launch"
        //     // or ps -ef | grep lidarodom | grep -v grep 
        ///// use the above result....
        //     ////
        //     ROS_ERROR("amrslam is running, now.");
        //     return false (using os.str() );
        // }

        std::string cmd = "roslaunch amrslam " + launch_name + launch_arg + " &";
        ROS_INFO("cmd: %s", cmd.c_str());
        ///todo: sperate the amrslam from current api program...
        bool result = std::system(cmd.c_str());
        if(result == 0) {
            ROS_WARN("cmd executed and ros launched");
```

정리가 필요

먼저 system으로 실행하게 되면 block 을 하게 되서 프로그램이 실행되는 동안 원래의 프로그램이 막히는 현상이 발생할 수 있다.  

이때 백그라운드로 작업할 수 있게 해주면 간단히 해결할 수 있다.  문자열에 *&* 를 추가해준다. 

**하지만** 여기에는 치명적 단점이 있는데, 만약 프로그램이 백그라운드라고 해도 계속 돌아가는 상항이라면   
원래 system으로 실행하게 되면 parent 프로세서; 현재 실행되고 있는 프로그램에 종속되서  
parent가 죽으면 system으로 실행한 프로그램도 죽게 된다.

> 상황에 따라서 프로그램이 계속 실행되어야 하는 경우가 아닌 경우에는 상관이 없을 수도 있으므로  
테스트를 해보는 것이 좋다.  


## 그래서 이하 fork 로 사용하는 것 정리하기
참고 amrslam_api  참고

https://itecnote.com/tecnote/c-how-to-spawn-child-processes-that-dont-die-with-parent/#google_vignette
