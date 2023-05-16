# Wheeled mobile robots
Wheeled mobile robots 에는 Holonomic (omnidirectional) 또는 nonholonomic 방식이 있다.   


Holonomic: omniwheels 또는 mecanum wheels 가 있다. 옆으로 이동이 가능하다 

Nonholonomic: 자동차, 전통적 방식의 휠 등이 있고, 옆으로 움직일 수가 없다


## Kinematic model
4바퀴의 mecanum 의 모바일 로봇 kinematic model  

![이미지](./img/mecanum_kenematic.png)

𝑢 는 휠의 driving 속도의 대한 vector  
𝑟 은 휠의 radius   
𝑙 과 𝑤 은 샷시 (chassis)의 dimensions   
𝑙 은 휠베이스라고 생각하면 되고, front휠의 중점에서 rear휠의 중점까지 거리   
𝑤 정면에서 봤을 때 휠과 휠 사이의 거리    
𝛾 는 슬라이딩을(free sliding occurs) 하는 각도   
free sliding은 diagonal 움직임. 즉, 대각선으로 움직이는 것을 의미하는 듯 하다   


![이미지](./img/mecanum_robot.png)

## 파이썬 코드로 키네마틱을 function으로 구현

```
    ┏    ┓       ┏             ┓   
    ┃ u1 ┃       ┃ -l - w 1 -1 ┃ ┏     ┓    
    ┃ u2 ┃       ┃ 1 + w  1  1 ┃ ┃ wbz ┃   
u = ┃ u3 ┃ = 1/r ┃ l + w  l -1 ┃ ┃ ubx ┃   
    ┃ u4 ┃       ┃ l - w  1  1 ┃ ┃ uby ┃   
    ┖    ┚       ┖             ┚ ┖     ┚   
```

```py
def twist2wheels(wz, vx, vy):
    l = 0.500/2
    r = 0.254/2
    w = 0.548/2
    H = np.array([[-l-w, 1, -1],
                  [ l+w, 1,  1],
                  [ l+w, 1, -1],
                  [-l-w, 1,  1]]) / r
    twist = np.array([wz, vx, vy])
    twist.shape = (3,1)
    u = np.dot(H, twist)
    return u.flatten().tolist()

# numpy등이 필요
import rospy, numpy as np
from std_msgs.msg import Float32MultiArray

rospy.init_node('make_turn', anonymous=True)
pub = rospy.Publisher('wheel_speed', Float32MultiArray, queue_size=10)
rospy.sleep(1)

u = twist2wheels(wz=1.5, vx=1, vy=0)
msg = Float32MultiArray(data=u)
pub.publish(msg)
rospy.sleep(1)
stop = [0,0,0,0]
msg = Float32MultiArray(data=stop)
pub.publish(msg)

```

예제에 사용된 로봇의 휠 지름은 254mm, 위의 그림을 참고하자..

> l, r, w를 2로 나눈것은 위의 그림을 보면 더 이해가 쉽다.  
robot의 휠베이스라고 할 수 있는 robot's length 부분의 길이를 사용을 하는데   
로봇 kinematic model을 보게 되면 *l* 의 움직임은 로봇 중심에서 휠 중심까지의    
움직임이니깐 robot's length (마치 휠베이스)에서 2를 나눠주게 되고,    
이는 w와, radius와도 같은 방식이니깐 다들 반절을 사용해서 나눠준다   

처음 np.array()로 만든 H 는 2차원 배열로 만들어 준다.   
각각의 배열에 3개씩 요소가 들어가게 된다. row:4, column:3   

twist 같은 경우에는 배열로 만든 후에 shape메소드를 통해서 3x1 짜리 2차원 배열로 만들어 준다   
이유는 wz, vx, vy 를 H array에 (공식에 의해) 곱해줘야 하기 때문 -- 이유는 H가 2차원 배열이어서 똑같이 만들어 주고   
twist 2차원 배열의 요소[0], [1], [2] 이 각각 H [0], [1], [2]에 곱해주게 된다.   

예를들어 [ [-l-w, 1, -1], ...생략 ] 과 [ [wz], [vx], [vy] ] 를 곱하게 됨 

 파이썬에서는 이 부분이 np.dot(H, twist)로 해결한다. H, twsit 요소를 각각 곱해주고 2차원 배열 요소끼리는 다 더해준다   

 마지막으로 2차원 배열을 리스트로 바꿔주게 된다. ( np.flatten().tolist() )


리턴 값으로 4개 바퀴의 속도인 u가 나오게 된다. (4개 요소 값)   



## 파이썬 interpreter 사용
터미널에서 `python3` 를 입력한 하면 interpreter프로그램이 의해 한줄씩 입력해서 테스트 해볼 수가 있다    

아래는 위의 함수를 적용해본 예시, 각각 print()함수로 값을 출력해 볼 수가 있다 
```py
Type "help", "copyright", "credits" or "license" for more information.
>>> import rospy, numpy as np
>>> from std_msgs.msg import Float32MultiArray
>>> l = 0.500/2
>>> r = 0.254/2
>>> w = 0.548/2
>>> H = np.array([ [-l-w, 1, -1], [ l+w, 1, 1], [ l+w, 1, -1], [-l-w, 1, 1] ]) /r
>>> print(H)
[[-4.12598425  7.87401575 -7.87401575]
 [ 4.12598425  7.87401575  7.87401575]
 [ 4.12598425  7.87401575 -7.87401575]
 [-4.12598425  7.87401575  7.87401575]]
>>> wz = 1.5
>>> vx = 1
>>> vy = 0
>>> twist = np.array([wz, vx, vy])
>>> print(twist)
[1.5 1.  0. ]
>>> twist.shape = (3,1)
>>> print(twist)
[[1.5]
 [1. ]
 [0. ]]
>>> u = np.dot(H, twist)
>>> print(u)
[[ 1.68503937]
 [14.06299213]
 [14.06299213]
 [ 1.68503937]]
>>> u.flatten().tolist()
[1.6850393700787407, 14.062992125984252, 14.062992125984252, 1.6850393700787407]
>>> 

```

