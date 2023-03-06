# The list of servers.
gazebo를 실행했을 때   
[Err] [REST.cc:205] Error in REST request


~/.ignition/fuel/config.yaml 파일을 열어서 url주소를 바꿔준다  

> old ignitionfuel domain으로 되어 있어서 그렇다


아래의 내용 중에 https://api.ignitionfuel.org 를 https://api.ignitionrobotics.org 로 바꾼다
```
servers:
  -
    name: osrf
    url: https://api.ignitionfuel.org
```

이것 처럼
```
url: https://api.ignitionrobotics.org
```