# ros custom message 만들기
std_msgs 등은 그냥 써도 되는 듯 하다.

예 Header

예를 들어 std_msgs의 Header을 사용하려고 하면 Header.msg 를 사용하는데   

자신의 프로젝트에 사용할 msg 디렉토리 안에 my_msg.msg 를 만들 때 그냥 Header header 식으로 사용하면 된다.
```
Header header
```
이렇게 사용하면 되고   
> 아마도 std_msgs 는 생략을 해도 되는지 모르겠다.

CMakeLists.txt 파일에서 
```
find_package(catkin REQUIRED COMPONENTS
    message_generation
    message_runtime
    std_msgs
)

add_message_files(
  FILES
  my_msg.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
)
```
이 정도만 사용하면 된다. 

package.xml 에는 
```xml
  <buildtool_depend>catkin</buildtool_depend>
  <build_depend>message_generation</build_depend>
  <build_depend>std_msgs</build_depend>
  <build_export_depend>std_msgs</build_export_depend>
  <exec_depend>message_runtime</exec_depend>
  <exec_depend>std_msgs</exec_depend>
```


## 다른 type을 사용할 경우
모두 다 그런 것 인지는 모르겠지만, geometry_msgs 의 경우에는 커스텀 메세지안에 특정 메세지 타입까지 적어야 한다. 

만약 Pose 메세지를 만들고 싶을 때는 
my_msg.msg에 
```
geometry_msgs/Pose pose
int32 my_id
```

이런식으로 지정을 해야지, geometry_msgs를 정확히 찾아준다. 메세지 타입을 안 적을 경우   

```
Did you forget to specify generate_messages?(dependencies...) 
```
이런식으로 에러가 발생하며, 자신의 프로젝트에서 해당 (예를들어) Pose 메세지를 찾으려고 하고 찾지 못하고 에러가 발생한다.

나머지 CMakeLists.txt 파일을 기존과 같이 하면 된다.
find_package(), generate_messages() 에 geometry_msgs 를 꼭 추가해준다.

```
find_package(catkin REQUIRED COMPONENTS
    message_generation
    message_runtime
    std_msgs
    geometry_msgs
)

add_message_files(
  FILES
  my_msg.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
  geometry_msgs
)
```


package.xml
```xml
  <buildtool_depend>catkin</buildtool_depend>
  <build_depend>message_generation</build_depend>
  <build_depend>std_msgs</build_depend>
  <build_depend>geometry_msgs</build_depend>
  <build_export_depend>std_msgs</build_export_depend>
  <exec_depend>message_runtime</exec_depend>
  <exec_depend>std_msgs</exec_depend>
  <exec_depend>geometry_msgs</exec_depend>
```