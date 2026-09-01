## cartographer constraint lua 파일 추가하기

1. proto 파일 지정을 해줘야지 options_ 를 사용할 수가 있음   
constraint_builder_options.proto   
해당 pb.cc 파일 cartographer 디렉토리에 없다. 
> 따로 protoc 로 cc 파일을 만들 필요는 없고, colcon build 를 해주면 pb.cc 파일도 만들어 준다.   
단, 해당 파일은 빌드 시에 install 디렉토리 이하 cartographer 이하 include 에서 찾을 수 있다.   

1-1. 여기까지하면 proto 파일 및 클래스가 생기므로 해당 변수 내용을 불러 올 수가 있으나 다행히 default 값 0 으로 지정되는 듯 하다.  


2. 해당 변수를 사용하려면 lua 파일에서 읽어와야 하므로ㅜ 그렇지 않으면 0 값으로 밖에 사용 못함   
lua 파일에 변수를 넣어준다.   
단, 변수만 넣어주면 읽어오는 과정에서 count가 맞지 않아서 사용할 수가 없다. count 관련 에러가 나는 듯 하다. 
pose_graph.lua 에 넣어줄 수가 있는데, constraint 이하에 만들어 줬다.  


3. 중요. 해당 lua 파일을 dictionary 를 만들면서 해당 값을 읽어오게 해야하는 듯하다.   
그래서 lau 파일을 읽어서 proto관련 클래스에 options_ 에 set 해준다. (protobuf 사용법 처럼 해당 변수 이름을 함수로 사용-getter 함수처럼 사용됨)   
constraint_builder.cc  파일에서 추가한다.   


4. 이제 사용할 ros 패키지(amrslam)에서 lua 변수를 override 해서 사용하면 된다.   
lua파일에서 POSE_GRAPH.constraint_builder.지정한변수이름 = 10.0



### trajectory_options
trajectory_options 은 protobuf 를 사용하지는 않으므로 lua 파일 및 lua dictionary 에서 불러오게 하면(set) 하면   
쉽게 사용 가능함  
