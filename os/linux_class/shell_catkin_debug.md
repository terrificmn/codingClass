# catkin build debug 빌드

```sh
#!/bin/sh
pkg=$1
if [ -z $pkg ]
then
        echo "Please specify the name of package."
else if [ $pkg = 'a' ]
    then
    echo "Now all packaged will be built with Debug."
    #       catkin build --cmake-args -DCMAKE_BUILD_TYPE=Debug -DFORCE_DEBUG_BUILD=True
else
    echo "Now caktin build ${pkg} with debug"
    catkin build ${pkg} --cmake-args -DCMAKE_BUILD_TYPE=Debug -DFORCE_DEBUG_BUILD=True
fi
fi
```




## colcon clean 패키지 

```sh
#!/bin/bash
arg_pkg=$1

if [ -z $arg_pkg ]; then
        echo "Please specify the name of the package."
else
    pkg_path=${HOME}/docker_ros2_ws/build/$arg_pkg
    ### 디렉토리 확인
    if [ ! -d $pkg_path ]; then
            echo "$arg_pkg not found. abort clean.."
            exit
    fi

    rm -rf $HOME/docker_ros2_ws/build/$arg_pkg
    if [ $? = 0 ]
    then
            echo "build/$arg_pkg has been deleted."
    fi

    rm -rf $HOME/docker_ros2_ws/install/$arg_pkg
    if [ $? = 0 ]
    then
            echo "install/$arg_pkg has been deleted."
    fi

fi
~     
```