```
fetal error: opencv2/core/core.hpp: No such file or directory
```
이런 에러 발생시...

패키지에 아래 내용을 적어주는데
```c
find_package (OpenCV REQUIRED)
find_package (cv_bridge REQUIRED)

include_directories(${OpenCV_INCLUDE_DIRS})
```
OpenCV_INCLUDE_DIRS는 하드코딩으로 하면 /usr/include/opencv4/ 여기쯤 되는 것 같다

그리고 ament_target_dependencies 에도 넣어주자
```c
ament_target_dependencies(executable_name 
  rclcpp 
  OpenCV
..
)
..
```

package.xml에도
```xml
<depend>cv_bridge</depend>
```

파이썬에서 import cv2를 했을 때
No module named 'cv2' 에러가 발생한다면

```
sudo apt-get update
sudo apt-get install python3-opencv
```
로 설치를 해준다

