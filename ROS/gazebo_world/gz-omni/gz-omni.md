# gz-omni Bridging Gazebo with Isaac Sim

포맷의 차이
gazebo는 SDF를 사용   
XML, URDF 사용 및 robotics에서 많이 사용, Robot Application 을 위해서 만들어짐


USD 는 
Omniverse applicatios에 사용   
애니메이션 등의 scene에 사용. 애니메이션 포함이 가능   
Layered format - 다양한 파일로 scence을 구성   
Scalable (많은 asset을 늘릴 수도 있음)   



Benefits

Rendering systems
-  Omniverse, OGRE, OGRE2
Physics Engines
- ODE, DART, Bullet, PhyxX


## 순서
Start Gazebo Scene   
Start Bridge
Start Isaac Sim
Configure Remaining Points
Start other necessary Modules
Start simulation


## offline Converters (SDF to USD)

SDF 파일로부터 Basic Elements 를 파싱하게 됨 
Link (Pose, Meshes, Collisions, Materials)   
Joint (Limits, Drive)

Sensors 관련해서도 parsing 을 하는데  Camera, Lidar, IMU 등이 되겠다   

===> USD 파일로 파싱이 되는데 (USD files, Materials, Textures)

실행 명령은 
`sdf2usd input output` 가 된다    

반대는   
`usd2sdf input output`   


추후 업데이트 필요
