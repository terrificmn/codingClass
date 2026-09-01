## forress 공식 tool

[MASS MOMENT OF INERTIA CALCULATO](https://amesweb.info/inertia/mass-moment-of-inertia-calculator.aspx)  

intertia 는 Fortress를 사용할 때 정말 중요하다. 

주요 wheel link 이거나, caster link 등에만 적용을 했고, gazebo 화면에서 view를 통해 intertia 를 보면    
핑크색으로 표시되는 것이 꽤 크고, 엉망이다.  
>  단순히 계산이 잘 못 되었는지 알았는데, 다른 link 에는 빠져있어서 그랬다.   
로봇이 움직이지 않거나, (cmd_vel 받아질 경우에도)  심한 경우에는 프로그램 강종  


너무 가벼운 mass로 인해 계산 0 이 나와도 gazebo가 에러가 발생하므로 조금 mass를 키워서 적용해준다. 0.1, 0.5, 1 kg 면 적당  

주로 Cylinder, Sphere, Rectangular Plate 선택해서 적용하면 된다.  
>Shpere 는 모든 값을 적용  

```xml
<link name="my_link">
    <pose>0 0 0.045 0 0 0</pose>
    <inertial>
        <mass>1.0</mass>
        <inertia>
            <ixx>0.010833</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>0.010833</iyy>
            <iyz>0</iyz>
            <izz>0.02</izz>
        </inertia>
        </inertial>
        <visual name="visual_my_link">
            <geometry>
            <!-- 생략 -->
        </visual>
</link>
```
> 중간의 ixy, ixz, iyz 는 0 도 괜찮다. xx, yy, zz 가 중요

