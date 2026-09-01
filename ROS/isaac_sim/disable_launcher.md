# disable launcher
omniverse-launcher 프로그램을 실행해서 사용하면 자동적으로 auto로 실행이 되게 프로그램이 되어 있는 듯 하다  

그래서 재부팅시 omniverse가 자동으로 실행이 된다.  

메뉴에서 startup 에 관련된 설정을 찾을 수가 없다.   
숨겨져있는 몇몇의 config 에서도 딱히 설정을 찾을 수가 없었음.  

그냥 실행파일을 실행을 못하게 권한을 변경해 버림
```
sudo chmod -x ./omniverse-launcher-linux.AppImage
```

