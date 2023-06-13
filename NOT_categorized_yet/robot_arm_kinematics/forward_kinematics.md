# forward kinematics
Forward Kinematics는 로봇 키네마틱 공식을 통해서 manipulator (로봇팔)의 end-effector 라고 불리는   
가장 마지막의 gripper 부분까지의 거리와 위치를 계산하게 되는 것을 말한다  

여러개의 links 와 joints 에 여러 각도의 자유도를 가지고 있는 로봇팔의 position과 orientation을 찾는 것

## DH parameters
4개의 파라미터가 있음. a, 알파, d, 세타  

a: length of the common normal. Assuming a revolte joint, this is the radius about previous 'Z'   (또는 r)
알파: angle about common normal, from old 'Z' axi to new 'Z' axis   
d: offset along previous 'Z' to the common normal    
theta: angle about previous 'Z', from old 'X' to new 'X'

Denavit-Hartenberg Parameters (DH params)



## set up the axes
Z-axis: Z축은 revolute joint 로 회전을 할 때의 축이 된다   
X-axis: X축은 common normal 이면서 이전의 Z축과 현재의 Z축 간의 가장 짧은 거리가 된다 (orthogonal line)   
Y-asix: Y축은 다른 2개의 축을 구했다면 쉽게 할 수 있는데 right hand rule을 따른다(오른쪽을 총(?)모양을 했을 때의 중지손가락 방향)   


# ros에서는 tf 를 통해서 쉽게 사용할 수가 있다
tf를 이용해서 사용할 수가 있는데 복잡한 kinematics를 알아서 계산해주는 것

[좀 더 정리해보기 다시 보기](https://www.youtube.com/watch?v=_pIyXGRXMWY)
