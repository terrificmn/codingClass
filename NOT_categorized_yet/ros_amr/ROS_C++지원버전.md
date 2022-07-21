ROS는 C++11 로 되어 있다는 것은 다 맞는 것은 아님

Melodic 버전은  C++14 까지 지원
ROS2는 C++14 default 라고 함


CMakeLists.txt 파일에 아래처럼 넣어서 사용하는 것도 가능한 듯  
In addition to above-mentioned, you can also use the set_properties macro in CMakeLists to set cpp standards for specific targets only (where you know you need c++17 for example) within a package instead for the whole package as it is done with add_compile_options. Here is an example which applies the c++17 standard for a defined executable:

set_property(TARGET my_executable PROPERTY CXX_STANDARD 17)
set_property(TARGET my_executable PROPERTY CXX_STANDARD_REQUIRED ON)

