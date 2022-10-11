signal.h 을 이용해서 SIGINT를 custom으로 만들 수 있는데  

```cpp
#include <ros/ros.h>
#include <signal.h>
void mySigintHandler(int sig)
{
  // Do some custom action.
  // For example, publish a stop message to some other nodes.
  
  // All the default sigint handler does is call shutdown()
  ros::shutdown();
}
int main(int argc, char** argv)
{
  ros::init(argc, argv, "my_node_name", ros::init_options::NoSigintHandler);
  ros::NodeHandle nh;
  // Override the default ros sigint handler.
  // This must be set after the first NodeHandle is created.
  signal(SIGINT, mySigintHandler);
  
  //...
  ros::spin();
  return 0;
}
```


기본 ros sigint handler를 설정해 줄 수가 있는데   

ros::shutdown()이(기본) 실행 되기 전에 다른 작업을 수행할 수 있게 한다   




