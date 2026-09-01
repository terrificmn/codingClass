# json setting 하기
개인적으로 사용하고 있는 폰트와, 아이콘, Theme 이다. 

이중에서 활성화된 tab 색을 바꾸는게 너무 하고 싶었다.  
왜냐면 코딩하다보면 여러개의 파일들을 열어두게 되는데, 내가 어디에 있는지 파악이 안된다.  

여기에 깃 관련 파일들이 변경되면 tab 의 타이틀 색도 바뀌고, 더 정신이 없는 중에 드디어 찾았다!

먼저 `Crtl + Shift + p` 를 눌러준 다음에 대충 Preference로 치기 시작하면  
Preferences: Open User Settings(JSON) 나오는데 클릭해준다.   
> 물로 메뉴에서 Preferences 로 접근해도 된다.  d

단순하게 "workbench.colorCustomizations": { } 안으로 중첩으로 넣어서  
tab.activeBackground 만 지정해 주면 된다. 대충 tab 까지만 치고 shift + space 를 눌러주면   
자동완성으로 추천을 해주므로 다른 것도 바꿔 줄 수가 있다.  
하지만 다른 것은 필요없고, 현재 활성화된 색만 좀 변경해주고 싶어서 색만 조금 튀는 색으로 변경해줌   

아주 유용하다. 내가 어느 파일을 작업하고 있는지 눈에 확 띈다. 굿!

```json
{
    "workbench.iconTheme": "vscode-icons",
    "editor.fontFamily": "'DaddyTimeMono Nerd Font Mono'",
    "workbench.colorTheme": "Noctis Uva",
    "workbench.colorCustomizations": {
        // "activityBar.background": "#00AA00",
        // "titleBar.activeForeground": "#f11010",
        // "titleBar.inactiveForeground": "#5c2323"
        "tab.activeBackground": "#36014b",
    },
    "window.titleBarStyle": "custom"
}
```

그리고 맨 아래의 window.titleBarStyle 을 커스텀으로 바꾸면 아예 흰 색깔 리눅스 형태의 타이틀 바에서  
vscode 원래 테마 등과 심플하면서 일체성 있게 바뀌게 된다.   



## 그냥 example 
시간 줄이기 위해서 대충 이런식으로 사용하면 될 듯  

- 보라색 테마   
- Noctis Uva
```json
"workbench.colorCustomizations": {
    "titleBar.activeForeground": "#ac6edf",
    "tab.activeBackground": "#4e1564"
},
"window.titleBarStyle": "custom"
```


- 녹색 테마 
- Noctis, Noctis Minimus
```json
"workbench.colorCustomizations": {
    "titleBar.activeForeground": "#44b460",
    "tab.activeBackground": "#1d6137"
},
"window.titleBarStyle": "custom"
```

- 빨간색 테마  
- Noctis Bordo
```json
"workbench.colorCustomizations": {
    "titleBar.activeForeground": "#9b2246",
    "tab.activeBackground": "#52172a"
},
"window.titleBarStyle": "custom"
```
