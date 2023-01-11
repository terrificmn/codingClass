
## Ros time
ROS에서는 ros::Time을 이용해서 시간을 지정할 수가 있는데  현재 시간을 알려면 
```cpp
ros::Time begin_time = ros::Time::now();
```
처럼 사용한다   

ros::Time은 unix epoch time을 사용하는데 

> 컴퓨팅 분야에서 광범위하게 사용되며, 1970년 1월1일 00:00:00 UTC 부터 seconds로 계산한 방법이다. unix time은 unix operating system의 시스템 시간으로 사용된다   - wikipedia
> epoch는 a period of time in history or a person's life를 의미

double형으로 변환은 .toSec() 같은 메소드를 사용해준다 
```cpp
double new_time = begin_time.toSec();
```


ros::Time으로 만들어서 시간 차를 구할 수도 있다. 이는 ros::Duration 클래스를 사용하게 된다  
```cpp
ros::Time time1 = ros::Time::now();
ros.Time.sleep(1.0);
ros::Time time2 = ros::Time::now();

ros::Duration duration_time = time1 - time2;
```

ros Time은 unix time이기 때문에 사람이 읽기에 불편하다   
그래서 변한을 해줄 수가 있는데   
이때 boost 의 posix_time을 사용할 수가 있다  


## 타임 변환 하기 posix_time::ptime 관련
boost::posix_time 을 이용해서 시간 표시하기  


헤더파일 include가 필요하다  
```cpp
#include "boost/date_time/posix_time/posix_time.hpp"
```

아래처럼 만들 수 있다 
```cpp
boost::posix_time::ptime posix_time1;
```

이제 ros Time 으로 만든 것을 toBoost() 메소드를 이용하면 ptime 클래스에 넣을 수가 있다.   
```cpp
boost::posix_time::ptime posix_time1;
ros::Time time1 = ros::Time::now();
posix_time1 = time1.toBoost();
```

이제 시간을 읽을 수 있게 변환하려면 to_iso_extended_string()을 사용하면 된다 (string으로 변환)
```cpp
std::string converted_iso_time;
converted_iso_time = boost::posix_time::to_iso_extended_string(posix_time1);
std::cout << "time: " << converted_iso_time;
```

결과는 
```
time: 2023-01-10T12:30:50.113972
```
이런식으로 나오게 된다 

여기에서 잘 보면 UTC 타임으로 나오는데   

> Coordinated Universal Time   

이것을 각 time zone에 맞춰서 바꿔줄 수 있다   

local_time_adjustor 헤더파일 include가 필요하다  
```cpp
#include "boost/date_time/posix_time/posix_time.hpp"
#include "boost/date_time/local_time_adjustor.hpp"
```

 typedef 로 local_adjustor를 이용해서   만들어준다. 하나의 객체?를 만들어준다
```cpp
typedef boost::date_time::local_adjustor<boost::posix_time::ptime, +9, boost::posix_time::no_dst> kor_time;
```
여기에서 <>안의 형식의 int는 +9은 우리나라 기준

이제 
```cpp
typedef boost::date_time::local_adjustor<boost::posix_time::ptime, +9, boost::posix_time::no_dst> kor_time;

boost::posix_time::ptime posix_time;
boost::posix_time::ptime local_posix_time;

posix_time = ros::Time::now().toBoost();
local_posix_time = kor_time::utc_to_local(posix_time);

std::cout << "time: " << local_posix_time;

```

이렇게 하면 현재 local time과 맞춰서 잘 나오게 된다 

[posix_time utc_example 참고페이지](https://www.boost.org/doc/libs/1_61_0/doc/html/date_time/examples.html#date_time.examples.local_utc_conversion)

[boost date_time/posix_time 참고](https://www.boost.org/doc/libs/1_61_0/doc/html/date_time/posix_time.html)


