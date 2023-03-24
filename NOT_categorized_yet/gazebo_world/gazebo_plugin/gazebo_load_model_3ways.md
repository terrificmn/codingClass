# gazebo load model
gazebo plugin hello world.cpp와 model_push.cpp 파일에 이은 model 불러오기 

model_push는 일단 화면에 띄워주고 앞으로 움직일 수 있게 해주는 plugin 이고   

factory.cpp 예제 파일에서는 좀 더 다양한 방법으로 model을 불러올 수 있게 된다 

일단 하는 방법은 전체적으로 비슷하다  소스파일 만들기, cmake, 컴파일된 shared plugin으로 world파일 만들기  


## 소스파일 부터
방법에는   
첫 번째, 파일로 직접 불러오는 것 (모델 파일을 만들어야 한다 )  
두 번째, string으로 직접 모델 파일을 sdf 파일 스트링을 넣어줘서 만든다   
마지막은, message를 만들고 퍼블리쉬 해서 가제보에서 띄워주는 방식   

```cpp
#include <ignition/math/Pose3.hh>
#include "gazebo/physics/physics.hh"
#include "gazebo/common/common.hh"
#include "gazebo/gazebo.hh"

namespace gazebo
{
class Factory : public WorldPlugin
{
    public: void Load(physics::WorldPtr _parent, sdf::ElementPtr /*_sdf*/)
    {
        // Option 1: Insert model from file via function call.
        // The filename must be in the GAZEBO_MODEL_PATH environment variable.
        // GAZEBO_MODEL_PATH로 환경변수가 되어 있어야 하고, 그 경로의 특정 모델 불러오기
        _parent->InsertModelFile("model://box");

        // Option 2: Insert model from string via function call.
        // Insert a sphere model from string
        // string으로 모델 불러오기 (직접 모델 sdf 파일을 적어준다)
        sdf::SDF sphereSDF;
        sphereSDF.SetFromString(
            "<sdf version ='1.4'>\
                <model name ='sphere'>\
                    <pose>1 0 0 0 0 0</pose>\
                    <link name ='link'>\
                    <pose>0 0 .5 0 0 0</pose>\
                    <collision name ='collision'>\
                        <geometry>\
                        <sphere><radius>0.5</radius></sphere>\
                        </geometry>\
                    </collision>\
                    <visual name ='visual'>\
                        <geometry>\
                        <sphere><radius>0.5</radius></sphere>\
                        </geometry>\
                    </visual>\
                    </link>\
                </model>\
            </sdf>");
        // Demonstrate using a custom model name.
        sdf::ElementPtr model = sphereSDF.Root()->GetElement("model");
        model->GetAttribute("name")->SetFromString("unique_sphere");
        _parent->InsertModelSDF(sphereSDF);

        // Option 3: Insert model from file via message passing.
        // 네트워크로 통신을 하면서 msg를 보내서 모델을 불러오는 방법. 가장 좋은 방법일 듯
        {
        // Create a new transport node
        transport::NodePtr node(new transport::Node());

        // Initialize the node with the world name
        node->Init(_parent->Name());

        // Create a publisher on the ~/factory topic
        transport::PublisherPtr factoryPub =
        node->Advertise<msgs::Factory>("~/factory");

        // Create the message
        msgs::Factory msg;

        // Model file to load
        msg.set_sdf_filename("model://cylinder");

        // Pose to initialize the model to
        msgs::Set(msg.mutable_pose(),
            ignition::math::Pose3d(
                ignition::math::Vector3d(1, -2, 0),
                ignition::math::Quaterniond(0, 0, 0)));

        // Send the message
        factoryPub->Publish(msg);
        }
    }
};

// Register this plugin with the simulator
GZ_REGISTER_WORLD_PLUGIN(Factory)
}
```

설명은 주석을 참고하자


## so 파일로 컴파일, CMakelists.txt
CMakelists.txt에 추가
```c
add_library(factory_load_gazebo SHARED src/factory.cpp)
target_link_libraries(factory_load_gazebo ${GAZEBO_LIBRARIES}) 
```
처음에 오는 이름이 so파일의 이름이 된다 

> 나머지 함수들은 gazebo_hello_world.md 를 참고하거나 예제 패키지를 확인

## 빌드

```
cd ~/gazebo_plugin_tutorial/build
cmake ..
make
```

(build가 없다면 만든다)

빌드가 완료되면 `libfactory_load_gazebo.so` 파일이 만들어진다


## model 파일 만들기
앞선 예제와 다른 점은 모델을 만들어야 한다   
왜냐하면 첫 번째, 3번째 방법으로 각각 모델을 불러오기 때문

models 디렉토리를 만들고, 각각 모델의 이름으로 디렉토리를 만든다 

```
cd  ~/gazebo_plugin_tutorial
mkdir -p models/box models/cylinder
```

> 또는 vscode, 파일 등으로 쉽게 만들자

각 model은 각각 model.config, model.sdf 파일이 있는데   
config에서는 모델 이름과, author, description 등을 지정, 실제 sdf 파일에서는 모델이 정의 됨 (xml)

### box 모델
box 디렉토리로 이동해서 model.config 만듬.
```xml
<?xml version='1.0'?>
<model>
    <name>box</name>
    <version>1.0</version>
    <sdf >model.sdf</sdf>

    <author>
        <name>tutorial_me</name>
        <email>mildsm@gmail.com</email>
    </author>

    <description>
        A simple Box.
    </description>
</model>
```

그리고 model.sdf 만듬
```xml
<?xml version='1.0'?>
<sdf version ='1.6'>
    <model name ='box'>
        <pose>1 3 0 0 0 0</pose>
        <link name ='link'>
        <pose>0 0 .5 0 0 0</pose>
        <collision name ='collision'>
            <geometry>
            <box><size>1 1 1</size></box>
            </geometry>
        </collision>
        <visual name ='visual'>
            <geometry>
            <box><size>1 1 1</size></box>
            </geometry>
        </visual>
        </link>
    </model>
</sdf>
```

### cylinder 모델 만들기
cylinder 디렉토리로 이동해서 model.config 만듬.
```xml
<?xml version='1.0'?>
<model>
    <name>cylinder</name>
    <version>1.0</version>
    <sdf >model.sdf</sdf>

    <author>
        <name>tutorial_me</name>
        <email>mildsm@gmail.com</email>
    </author>

    <description>
        A simple Cylinder.
    </description>
</model>
```

그리고 model.sdf 만듬
```xml
<?xml version='1.0'?>
<sdf version ='1.6'>
    <model name ='cylinder'>
        <pose>1 2 0 0 0 0</pose>
        <link name ='link'>
        <pose>0 0 .5 0 0 0</pose>
        <collision name ='collision'>
            <geometry>
            <cylinder><radius>0.5</radius><length>1</length></cylinder>
            </geometry>
        </collision>
        <visual name='visual'>
            <geometry>
            <cylinder><radius>0.5</radius><length>1</length></cylinder>
            </geometry>
        </visual>
        </link>
    </model>
</sdf>
```


## world 파일 만들기

최종 world파일을 만든다  
```xml
<?xml version="1.0"?>
<sdf version="1.4">
    <world name="default">
        <include>
        <uri>model://ground_plane</uri>
        </include>

        <include>
        <uri>model://sun</uri>
        </include>

        <plugin name="factory" filename="libfactory_load_gazebo.so"/>
    </world>
</sdf>
```

일반적으로 world 파일 안에 model 들이 꽉꽉 들어차게 되는데, 모델이 없는 대신에 plugin을 이용해서  
`libfactory_load_gazebo.so` 실행될 수 있게 해준다   


## gazebo 실행
gazebo에서 일단 환경변수로 model, plugin 위치를 알 수 있어야 하기 때문에 export를 먼저 한다 

```
cd ~/gazebo_plugin_tutorial
export GAZEBO_MODEL_PATH=`pwd`/models:$GAZEBO_MODEL_PATH
export GAEBO_PLUGIN_PATH=`pwd`/build:$GAZEBO_PLUGIN_PATH
```

실행
```
gazebo world/factory.world 
```

> `pwd` 현재 위치를 출력해서 그 값을 사용 (` 가 필요)

