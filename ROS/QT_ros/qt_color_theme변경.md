# qt color theme
예전에 잠깐 vscode에서 썼었던 Dracula theme을 Qt에 설치를 할 수가 있어서 해봄   
아주 쉽다~   

먼저 깃 클론 아무곳에... 중요한 파일은 xml 파일이므로, 추후 지워도 무방
```
git clone https://github.com/dracula/qtcreator.git
```

~/.config 디렉토리에 styles 디렉토리가 있는지 확인 후 없으면 만들어 준다  
그 이후 dracula.xml 파일을 이동시키거나 `cp`로 복사한다


```
mkdir -p  ~/.config/QtProject/qtcreator/styles
cd ~/qtcreator
mv dracula.xml ~/.config/QtProject/qtcreator/styles/
```

> 어차피 -p 옵션이면 없으면 만들고 있으면 에러를 낸다 ㅋㅋ 


## qtcreator 설정
Edit -> Preferences   
Text Editor 탭 클릭 후 이동   

Font & Colors 탭에서 Coor Scheme for Theme 에서 Dracula를 선택해주면 된다   

만약 Dracula가 리스트에서 안 보이면 Qt creator를 껏다가 켜준다   

