catkin build 를 하려고 하는데 아래와 같은 에러가 발생한다면  

```
The catkin CMake module was not found, but it is required to build a linked
  workspace.  To resolve this, please do one of the following, and try
  building again.
   1. Source the setup.sh file from an existing catkin workspace:
      source SETUP_FILE
   2. Extend another catkin workspace's result (install or devel) space:
      catkin config --extend RESULT_SPACE
   3. Set `catkin_DIR` to the directory containing `catkin-config.cmake`:
      catkin config --cmake-args -Dcatkin_DIR=CATKIN_CMAKE_CONFIG_PATH
   4. Add the catkin source package to your workspace's source space:
      cd SOURCE_SPACE && git clone https://github.com/ros/catkin.git
```

`soure /opt/ros/melodic/setup.bash` 를 안해서 그런 것임
