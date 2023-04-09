find_library(WIRINGPI_LIBRARIES NAMES wiringPi)
set(WIRINGPI_INCLUDE_DIRS "/usr/local/share/gpio_lib_c_rk3399/wiringPi")
find_path(WIRINGPI_INCLUDE_DIRS NAMES wiringPi.h)

cmake 파일 만든 후 에 복사
 sudo mv FindWiringPi.cmake /usr/share/cmake-3.16/Modules/

 cd /usr/share/cmake-3.16/Modules/
docker_noetic@77e9cb586ca8:/usr/share/cmake-3.16/Modules$ sudo mv FindWiringPi.cmake   WirignPiConfig.cmake
docker_noetic@77e9cb586ca8:/usr/share/cmake-3.16/Modules$ 


CMake Error at /opt/ros/noetic/share/catkin/cmake/catkinConfig.cmake:83 (find_package):
  Could not find a package configuration file provided by "WirignPi" with any
  of the following names:

    WirignPiConfig.cmake
    wirignpi-config.cmake

  Add the installation prefix of "WirignPi" to CMAKE_PREFIX_PATH or set
  "WirignPi_DIR" to a directory containing one of the above files.  If
  "WirignPi" provides a separate development package or SDK, be sure it has
  been installed.

현 상황에서는 이렇게 됨




find_library() 로 했더니 실패



set(WIRINGPI_LIB "/usr/local/share/gpio_lib_c_rk3399/wiringPi")
find_library(WIRINGPI_LIB wiringPi)


WARNING: Target "servo_ros_node" requests linking to directory "/usr/local/share/gpio_lib_c_rk3399".  Targets may link only to libraries.  CMake is dropping the item.

linking 할 때 lib의 디렉토리가 아니고 실제 파일까지 연결이 필요하다는 의미


