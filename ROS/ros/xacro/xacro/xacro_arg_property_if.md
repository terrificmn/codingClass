# xacro 사용
Xacro는 XML Macros 로 XML macro Language라고 할 수 있다.  
XML 파일을 xacro를 사용할 때 arg, property, marco 등 다양한 기능을 사용할 수가 있다.

```xml
<?xml version="1.0" encoding="utf-8"?>
```

### property 설정
```xml
<xacro:property name="my_property"  default="true"/>
```
property는 default값이 있어야 한다  또는 value
> 위의 것은 거의 arg 처럼 사용했는데 원래는 말 그대로 하나의 property 를 지정할 때 쓰는 듯 하다

예제를 보면 아예 통으로 한 property를 지정해줄 때 사용한다 
```xml
<xacro:property name="front_left_origin">
  <origin xyz="0.3 0 0" rpy="0 0 0" />
</xacro:property>

<pr2_wheel name="front_left_wheel">
  <xacro:insert_block name="front_left_origin" />
</pr2_wheel>
```

### arg 설정
```xml
<xacro:arg name="y_position" default="3.141519"/>
```
default 값으로 지정한다  

사용은 `$(arg 변수명)` 처럼 사용한다 

> 일명 rospack기능으로 런치파일에서 사용하듯이 쓸 수 있어서 유용하다.  
반면에 arg 기능이 아니면 `${변수명}` 처럼 사용한다  

```xml
<joint name="laser_sensor_joint" type="fixed">
    <origin xyz="0.1 0.1 0.14" rpy="0 0 $(arg yaw)" />
    <parent ....생략>
    <chlid ..생략>
    <axis xyz="0 0 0">
</joint>
```

### if 문 사용 (비추천.. 아직 잘 모르겠다 ㅜ ㅋㅋ)
"0", "1", "true", "false" 만 가지고 사용이 가능함

```xml
<xacro:property name="my_property"  default="true"/>

<xacro:if value="${my_property == 'true'}" >
    <xacro:arg name="arg_a" default="yes"/>
</xacro:if>

```

unless 도 가능
```xml
<xacro:unless value="$(my_property == 'true'" >
    ....xacro 
</xacro:unless>
```

> if을 이용해서 true, false에 따라서 arg, 또는 property를 사용하려고 했는데   
에러는 발생하지 않지만, 안된다..   그냥 안쓸랜다 ;;;;


### marco도 있는데... 이건 나중에






