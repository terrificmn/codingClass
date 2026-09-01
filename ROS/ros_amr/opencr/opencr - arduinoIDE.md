# arduino IDE 에 opencr 보드 설치

- File -> Preferences   

하단의 Additional boards manager 를 클릭 후    

`https://raw.githubusercontent.com/ROBOTIS-GIT/OpenCR/master/arduino/opencr_release/package_opencr_index.json`   
를 복사해서 넣어준다 . 그리고 OK 버튼

esp32 까지 있다면, 아래처럼 한 줄씩 넣어주게 된다 
```
https://raw.githubusercontent.com/ROBOTIS-GIT/OpenCR/master/arduino/opencr_release/package_opencr_index.json
https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
```


- Tools -> Board: -> Boards Manager   
또는 왼쪽의 두 번째 아이콘 보드 매니저를 클릭

*opencr* 이라고 검색 하면 ROBOTIS 의 OpenCR 이 나온다. install 해준다   

다시 메뉴에서 보면  
Board에서 이제 Opencr Board를 선택할 수 있고,   
포트도 /dev/ttyACM0 으로 선택해주면 된다   

