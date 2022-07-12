## 우분투 locale 설정하기 | gazebo 에러발생시
terminate called after throwing an instance of 'terminate called after throwing an instance of 'std::runtime_error'   
std::runtime_error'  
  what():  locale::facet::_S_create_c_locale name not valid  what():    
locale::facet::_S_create_c_locale name not valid  

gazebo실행 시 locale이 제대로 설정이 안 되어 있을 경우에 에러가 발생하면서 실행이 안 됨 

locale 설정을 해준다
```
$ apt-get install locales
$ locale-gen en_US.UTF-8
$ update-locale LANG=en_US.UTF-8
$ reboot
```

