```cpp
ros::Time stamp = ros::Time::now();
std::stringstream ss;
ss << stamp.sec << "." << stamp.nsec;
std::cout << ss.str() << std::endl;
```
참고