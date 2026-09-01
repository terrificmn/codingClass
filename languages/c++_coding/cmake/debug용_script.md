# debug shell script
```sh
#!/bin/sh
pkg=$1
catkin build ${pkg} -DCMAKE_BUILD_TYPE=Debug -DFORCE_DEBUG_BUILD=True
```

좀 더 고오급(?) 기능. empty 면 빌드 안함. (왜? 파라미터를 안 넣으면 catkin build 가 되버린다.)
```sh
#!/bin/sh
pkg=$1
if [ -z $pkg ]
then
        echo "Please specify the name of package."
else
        echo "Now caktin build ${pkg} with debug"
        catkin build ${pkg} -DCMAKE_BUILD_TYPE=Debug -DFORCE_DEBUG_BUILD=True
fi
```

빌드 자체를 Release 모드를 하면 디버깅을 할 수 없으로 Debug 모드로 빌드를 해야하지만 함   
하지만 cmake args 가 길다;;;

그래서 vscode , ros 확장팩 조합으로 디버깅 할 때 유용하다.  

