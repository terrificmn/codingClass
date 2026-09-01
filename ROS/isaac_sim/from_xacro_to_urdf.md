# xacro to urdf
issac sim에서는 urdf를 인식하므로 xacro 로 되어 있는 파일들을 하나로 urdf 로 만들어 줘야한다   

하지만 보통 simulation을 하기 위해서 런치파일을 실행하고   
거기의 파라미터 값들을 사용하게 되어 해당 xacro 파일에서 그 런치파일의 파라미터를 사용하므로   

수동으로 바꾸려는 xacro 파일의 파라미터들을 하드 코딩을 바꿔준다   

## doosan robotics

예를 들어서 
```xml
  <xacro:property name="cr" value="$(arg color)"/>
  <xacro:property name="gr" value="$(arg gripper)"/>
  
  <xacro:if value="${cr == 'white'}">
     <xacro:include filename="$(find dsr_description)/xacro/macro.a0912.white.xacro" />
  </xacro:if>
  ... 생략
```

색깔을 정할 수 있게 되어 있다. argument color는 이미 런치파일을 실행할 때 white 인지  blue 인지 결정이된다  

그러므로 하드코딩으로 `value="white"` 이런식으로 고정을 시켜준다.  혹은 if문을 빼리거나   


이렇게 한 후에 가장 메인이 되는 해당 모델의 root 모델을 지정해서 변환을 해주면 된다     
> xacro에서는 다른 파일을 계속 include 하기 때문에 



## from xacro to urdf
```
rosrun xacro xacro my_model.urdf.xacro > my_model.urdf
```


