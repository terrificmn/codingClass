# 로봇 모델 만들기

Gazebo 에서 만들었던 building model 에 로봇 모델을 쓰기 위해서 
rviz를 이용해서 로봇 모델을 만들었다.

xml을 사용해서 하는데 예전에도 xml이 궁금하기는 했고 들어보기도 했으나  
이번에 처음 접해 보았다~

서버 사이드와 프론트에서는 JSON을 이용해서 통신을 하는데 XML은 이제 잘 쓰이지 않는다고 
들었는데~   
로봇에서는 XML만 쓰이는 것은 아니겠지만 이것도 좀 궁금했다.  
질문 한다는 것을 깜빡 ㅋㅋ

어쨌든 urdf 라는 것으로 사용이 되는데   
이 안에 link 태그들이 있고 그리고 이 link들을 joint 태그로 연결해준다

joint를 해줄 때 부모 parent link, 자식 child link 가 생기게 되게   
그 두 개를 joint에서 잘 연결 시켜주면 되는데  
막상 이해를 했던 것 같아서 실행을 하면 생각했던 거와 다르게 되어서 이 부분이 많이 헛깔렸다

이게 어떻게 보면 세세한 수치에도 많이 바뀌고, local origin 좌표와도 신경을 써야하고 
xyz축 

<img src=0>
<br>

roll, pitch, yaw 도 있었다
<img src=1>
<br>

[참고 사이트: https://www.grc.nasa.gov/www/k-12/airplane/rotations.html](https://www.grc.nasa.gov/www/k-12/airplane/rotations.html)


> 다행인 것은 예전에 비행기 시뮬레이터 게임을 한적이 있었는데 
비행기에도 roll, pitch, yaw 란 개념이 있어서 이 부분은 이해가 쉽게 갔다.
이미지를 찾는데 roll, pitch로 검색하니 역시 비행기가 따악!

<br>

# 차근차근 무작정 따라 해보기

그래서 좀 더 제대로 해보기 위해서 무작정 하는 것보다는 튜토리얼을 하나씩 해보기로 결정

공식 페이지 였던 거 같은데 
스타워즈 R2-D2 만들기가 있어서 하나씩 해보면서 해보았더니~ 나만의 모델이 완성이 되었다 ㅋㅋ

[공식 urdf 튜토리얼 보기](http://wiki.ros.org/urdf/Tutorials/Building%20a%20Visual%20Robot%20Model%20with%20URDF%20from%20Scratch#CA-022f86e3d8621ed9ed9ea5046df7194ceaf597cc_4)

물론 복사 붙여넣기 한 것은 아니였고
처음부터 link를 하나씩 써가면서 두 개의 링크를 joint를 했더니
도움이 많이 되었다

아래는 내가 사용한 코드 예제
```xml
<?xml version="1.0" ?>
<robot name="firstmodel">

  <material name="blue">
    <color rgba="0 0 0.8 1"/>
  </material>

  <material name="white">
    <color rgba="1 1 1 1"/>
  </material>

  <material name="black">
    <color rgba="0 0 0 1"/>
  </material>

  <link name="base_link">
    <visual>
      <geometry>
        <cylinder length="0.6" radius="0.2"/>
      </geometry>
      <material name="blue"/>
    </visual>
  </link>

  <link name="right_leg">
    <visual>
      <geometry>
        <box size="0.6 0.1 0.2"/>
      </geometry>
      <origin rpy="0 1.57075 0" xyx="0 0 -0.3"/>
      <material name="white"/>
    </visual>
  </link>

  <joint name="base_to_right_leg" type="fixed">
    <parent link="base_link"/>
    <child link="right_leg"/>
    <origin xyz="0 -0.22 -0.05"/>
  </joint>
```
material 태그로 색을 미리 지정해줘서 각 link에서 쉽게 사용할 수 있게 해준다

base_link인 몸통은 cylinder로 만들고 right_leg는 joint base_to_right_leg로 연결이 되어 진다  
몸통의 크기는 0.2 인데 오른쪽 다리가 origin좌표는 rpy에서 p 즉 pitch 부분이 90도 세워져있게 만들었고  
(1.57075 는 완전 한바퀴를 도는 3.14의 절반)

그리고 joint에서 붙는 부분이 중요한데 xyz에서 y축으로 -0.22 이동해서 오른쪽으로 이동이 되어서 원형 몸통에 다리가 붙는 코드가 완성이 됨

아 그리고 역시 name을 지정할 떄에도 뭔가 link1, link2, joint1 이라고 하기 보다
쉽게 이해할 수 있게 문자열로 줬더니 더 좋았다.  
(물론 너무 길어진다는 단점도 있다 ㅋㅋ)

어쨋든.. 그래서 계속 집중해서 하다보니~ 이제 좀 이해가 되었고
어느정도 원하는 로봇 모델을 만들어 볼 수 있었다

물론~ 아주 beginner 이기는 하다 ㅋㅋㅋ 😛
그래도 한 걸음 한 걸음 나아가면 되는 것이지 뭐 ㅋㅋ

<img src=2>
<br>

<img src=3>
<br>

<img src=4>
<br>

아쉽게도 gazebo 시뮬레이터를 실행해서 내가 그 전에 만든 빌딩 (학교건물 4층) 안에
로봇모델을 넣는 것에는 실패했지만 (나름 심혈을 기울인 ㅋㅋ)

<img src=5>
<br>

교수님께 들은바로는 
urdf를 spawn을 이용해서 전환해줘서 launch 파일에서 작동되게하는 힌트를 얻었다

주말을 이용해서 한번 해볼 계획~

아...하하ㅏㅏㅏㅏ하하하 신난다;;😱
