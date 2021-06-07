# 기본 터미널 보다 조금 더 편리한(?) terminator 사용하기

설치
```
$ sudo apt install terminator
```

설치가 완료가 되면 
기본 터미널에서 terminator 라고 치면 실행이 되며

슈퍼키를 누른 후에 terminator로 검색해도 된다

Ctrl + Shift + o 는 수평으로 터미널 창을 분리해준다
Ctrl + Shift + e 는 수직으로 터미널 창을 분리
Ctrl + Shift + w 는 활동화되어 있는 창 끄기

기본적으로 활성화 되어 있는 터미널은 빨간색으로 표시가 되는데 이를 바꾸고 싶으면
config 파일을 수정해 주면 된다

```
$ vi ~/.config/terminator/config
```

기본적으로 
```
[global_config]
[keybindings]
[layouts]
  [[default]]
    [[[child1]]]
      parent = window0
      type = Terminal
    [[[window0]]]
      parent = ""
      type = Window
[plugins]
[profiles]
  [[default]]
```
이런식으로 되어 있는데

`$ man terminator_config` 를 살펴 보면 (명령어는 아니지만 매뉴얼을 제공) 
다양한 속성 및 설정 법을 자세히 알 수 있다.   
여러가지를 설정할 수 있으나 활성화 되었을 때의 타이틀 부분만 색을 바꿔 보았다

[global_config] 아래에 속성 값을 넣어줘서 변경해주면 된다

```
[global_config]
  title_transmit_bg_color = "#EFFF0d"
  title_transmit_fg_color = "#0730b5"
[keybindings]
[layouts]
...
..생략 ...
...
```
위의 타이틀bg_color는 타이틀의 백 그라운드 색  
타이틀fg_coclor 는 타이틀의 글자 색깔이 되겠다
