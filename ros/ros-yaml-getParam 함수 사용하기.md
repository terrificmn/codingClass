
ros::NodeHandle 을 이용해서 getParam() 함수를 사용해서 파라미터를 받을 수가 있다.  

1. 먼저 launch file을 사용해야한다. 
2. yaml 파일로 파라미터 셋팅 파일을 만들 수 있고, yaml 파일에서 좀 더 카테고리화(?)해서 사용도 가능하다
3. 역시 catkin_create_pkg 로 패키지를 만들고...


## catkin package 안 에 yaml파일로 설정파일 만들기

param / config 어떤 이름으로든 디렉토리를 하나 만들어 주고, 그 안에 yaml 파일을 만든다  

예: config 디렉토리 안에 dummy_params.yaml, 내용은 아래처럼 
```yaml
param1:
	number1: 20
	number2: 5
	string1: any_string

param2:
	bool1: false
	float1: 1.0
```

카테고리는 param1: 한 후에 그 다음 칸 부터 탭으로 구분해준다   
이런식으로 여러 카테고리를 만들 수 있다. int, string, bool, float 등의 형식으로 사용   


## launch 파일 만들기
launch 디렉토리와 test.launch 파일을 만들어 준다   
```xml
<launch>
	<rosparam file="$(find ros패키지이름)/config/dummy_params.yaml" command="load"/>
	<node name="ros패키지이름" pkg="ros패키지이름" type="ros패키지 노드이름" output="screen"/>
</launch>
```

런치파일을 실행하면 dummy_params.yaml을 불러와서 파마미터를 사용할 수 있게 된다   

> 그냥 rosrun으로 사용할 시에는 디폴트 값으로 사용이 된다  (변수 선언)


## 실제 소스 파일에서 getParam() 함수 사용

```cpp
int main(int argc, char** argv) {
	ros::init(argc, argv, "serve_ros_node");
	ros::NodeHandle nh;
	
	// 변수를 사용하기 위해 디폴트 값으로 선언
	int param_number1 = 0;
	int param_number2 = 0;
	std::string param_str1 = "test";
	bool param_bool1 = false;
	float param_float1 = 0.0;

	nh.getParam("param1/number1", param_number1);
	nh.getParam("param1/number2", param_number2);
	nh.getParam("param1/string1", param_str1);
	nh.getParam("param2/bool1", param_bool1);
	nh.getParam("param2/float1", param_float1);

	//.. 생략
}
```

getParam() 함수는 첫 번째 파마리터에서 yaml파일에서 불러온 내용을 읽게 되고,   
이것을 두 번째 파라미터에 저장해주게 된다 . 이후 저장 된 변수를 이용해서 프로그래밍 하면 된다 

> 즉, 첫 번째 파라미터를 불러오는데 실패하거나 없을 경우에는 기존에 선언되 있는 변수를 그대로 사용하니 문제가 없게 된다 

yaml파일의 파라미터는 카테고리(?) 를 / 로 구분을 하고  "카테고리1/파라미터" 식으로 사용하면 된다   



## 그 외에 런치파일의 param 속성 이용하기
ros_parameter_param_파라미터_관련.md 파일을 확인하자   

yaml파일이 아닌, 그냥 ros 런치파일에서 param 태그로 만들어 두면  
`ros::param::get("/publish_frame_to", paramStr);` 식으로 사용 가능하다   

