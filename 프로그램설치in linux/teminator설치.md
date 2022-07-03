# 기본 터미널 보다 조금 더 편리한 terminator 사용하기
기존 리눅스의 터미널을 쓰다가 조금 더 편리함이 있는 터미널을 써보자
terminator라는 프로그램인데 이름 부터가 살벌😱

설치를 해보자~ 우분투 기준으로는 apt나 apt-get으로 쉽게 설치가 가능하다

```
$ sudo apt install terminator
```

설치가 완료가 되면 기본 터미널에서 terminator 라고 치면 실행이 되며

GUI 환경에서도 슈퍼키를 누른후(윈도위키) 쉽게 찾을 수 있다 

<img src=0>
<br>


많이 쓰는 주요 기능임

| 키 조합 | 기능 |
| -- | -- |
| Ctrl + Shift + O | 수평으로 터미널 창을 분리해준다 |
| Ctrl + Shift + E | 수직으로 터미널 창을 분리 |
| Ctrl + Shift + W | 활성화 되어 있는 창 끄기 |

<br>

이를 이용해서 터미널(terminator로)에 여러개를 띄워서 
ROS에서 roscore, rosrun을 하기에 제격이다

이런식으로 분할이 된다.

<img src=1>
<br>

<br>

# 나만의 낭만적?인 색깔로 바꿔보기 ㅋㅋ 
기본적으로 활성화 되어 있는 터미널은 빨간색으로 표시가 되는데 

<img src=2>

영화: 터미네이터 이거 때문은 아니겠지?! 🤫


그냥 색 좀 바꿔보고 싶으면 config 파일을 수정해 주면 된다

config 파일을 열어보자
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

```
$ man terminator_config
```
를 살펴 보면 (명령어는 아니지만 매뉴얼을 제공한다. 신기하구먼 🤩) 

여기에서 다양한 속성 및 설정 법을 자세히 알 수 있다.   
여러가지를 설정할 수 있으나 활성화 되었을 때의 타이틀 부분만 색을 바꿔 보았다

[global_config] 아래에 속성 값을 넣어줘서 변경해주면 된다  
아래처럼 "#색깔코드"를 넣어주면 된다

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
위의 title_transmit_bg_color는 맨 위 제목 배경색이고,  
title_transmit_fg_color 는 글자 색깔이 되겠다

[구글에서 color picker로 색깔 알아보기](https://www.google.com/search?q=Colour+picker&sxsrf=ALeKk036SvbVon2m0U9wsVO3aLwAn0wp2A%3A1623225720019&source=hp&ei=d3XAYM63O8qmoAS7jZmgCg&iflsig=AINFCbYAAAAAYMCDiBRqY0jqKT8zWSOi30dHftwIvLfM&oq=Colour+picker&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBAgAEAoyBwgAEIcCEBQyBwgAEIcCEBQyAggAMgIIADICCAAyAggAMgIIADICCAA6BwgjEOoCECdQ1gdY1gdgnwtoAXAAeACAAWGIAWGSAQExmAEAoAECoAEBqgEHZ3dzLXdperABCg&sclient=gws-wiz&ved=0ahUKEwiOz7eDi4rxAhVKE4gKHbtGBqQQ4dUDCAY&uact=5)

끝!