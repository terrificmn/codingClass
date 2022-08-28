vscode plugin

한글 설치 후에 ESC키를 누르면 바로 영어로 돌아가게 해주는 기능은 VIM 옵션에서 추가해주면 된다   
아래 각 입력에 따라서 다르게 적용가능하나 작동은 하나 한글 키보드가 아예 변경이 되는 문제 발생

Rocky Linux는 기본으로  입력기로 ibus-hangul 을 사용하기 때문에  
ibus를 이용해서 변경하려고 했으나  아래의 방법 처럼 하면 vim 입력모드에서 ESC로 빠져나오면  
한글에서 영어로 바뀌는 것은 잘 작동하나   
이후 한글이 입력이 안됨~ 아예 영문 키보드로 변경되는 듯 

defaultIM을 "hangul" 로 바꾸면 한글 키보드로 바꿔지나 한글 키보드 내에서 영문로 바꾸는 법은 아직 모르겠음  

그래서 일단은 보류. vim 확장팩은 다시 지움.. 시간만 낭비되고 있음;;; 


ibus
```
"vim.autoSwitchInputMethod.enable": true,
"vim.autoSwitchInputMethod.defaultIM": "xkb:us::eng",
"vim.autoSwitchInputMethod.obtainIMCmd": "/usr/bin/ibus engine",
"vim.autoSwitchInputMethod.switchIMCmd": "/usr/bin/ibus engine {im}"
```

xkb-switch
```
"vim.autoSwitchInputMethod.enable": true,
"vim.autoSwitchInputMethod.defaultIM": "us",
"vim.autoSwitchInputMethod.obtainIMCmd": "/usr/local/bin/xkb-switch",
"vim.autoSwitchInputMethod.switchIMCmd": "/usr/local/bin/xkb-switch -s {im}"
```

fcitx
```
"vim.autoSwitchInputMethod.enable": true,
"vim.autoSwitchInputMethod.defaultIM": "1",
"vim.autoSwitchInputMethod.obtainIMCmd": "/usr/bin/fcitx-remote",
"vim.autoSwitchInputMethod.switchIMCmd": "/usr/bin/fcitx-remote -t {im}",
```

일단 추후에 다시 vim 확장팩을 사용할려고 하면   
fcitx 입력기로 변경해보거나 일단 ubuntu에서는 fcitx 설치가 쉬우므로  
Rocky 리눅스에서는 fcitx는 소스 코드로 빌드해야할 듯 하다  


https://github.com/fcitx/fcitx-hangul.git

의존성 패키지

    fcitx
    libhangul
    cmake (make)
    intltool (make)

fcitx는 설치해야하고 libhangul은 설치되어 있을 것임

추후 도전해보자.. 지금은 보류;; 

