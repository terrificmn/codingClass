ROS_INFO 예


ROS_INFO macro accepts C-style printf formatting parameters as in this example from "Mastering ROS'":

ROS_INFO("From Client [%s], Server says [%s]", req.in.c_str(), res.out.c_str())

ROS_INFO_STREAM macro accepts C++ style std::iostream formatting as in this example from "A Gentle Introduction to ROS":

ROS_INFO_STREAM("Sending random velocity command: " << " linear=" << msg. linear . x << "angular=" << msg. angular . z)


ROS_INFO_NAMED("my_package", "Info log from my library.");