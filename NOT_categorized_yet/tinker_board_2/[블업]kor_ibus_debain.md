# tinker board 2 에서 한글 키보드 설치하기
우분투에서 했던 방식처럼 fcitx-hangul을 설치하려고 했는데 실패했다.  

참고로 fcitx-hangul 외에도 패키지가 많이 필요하지만 그냥 참고로만 알아두자.  
`fcitx fcitx-frontend-gtk2 fcitx-frontend-gtk3 fcitx-hangul` 하지만 다른 패키지가   
더 필요한 듯하다. 한글 키보드를 찾지를 못한다   

그래서 ibus를 사용해서 한글을 설치한다.  

> Rocky Linuxd에서도 ibus를 사용하는데 반갑군 ㅋ

<br />

## ibus 한글 설치
터미널창을 열고 
```
sudo apt install ibus-hangul im-config
```

처음 실행은 im-config를 해준다
```
im-config
```

그러면 창이 열리고 몇번의 확인을 눌러주면 .xinputrc 파일을 생성해준다  

<img src=0>
<br />

<img src=1>
<br />

No를 눌러준다. (Yes를 눌러도 크게 상관없다) 

이제 user configuration을 선택해주는데 default로 하거나 ibus로 선택해준다  
(이것도 크게 상관은 없는 듯하다 - 마지막으로 어차피 설정을 해야하므로....)

<img src=2>
<br />

이렇게 되면 유저의 디렉토리에 .xinputrc 파일이 생성이 된다 

<br />

### 한글 키보드 추가
이제 한글 키보드를 추가해주자. 다시 터미널에 입력
```
ibus-setup
```

<img src=3>
<br />

Input Method에서 Add를 누르고 kor로 검색을 하면 Korean 목록이 나오는데, 이때 Korean을 눌러주면  
Hangul을 선택해서 추가해줄 수 있다

<img src=4>
<br />

이제 오른쪽 하단을 보면 EN 이라고 나와 있는데 이곳을 클릭해주면   
English-English 에서 Korean-Hangul 로 바꿔줄 수 있게 된다.   

<img src=5>
<br />

이렇게 해도 한영키를 눌러도 먹히지 않는다. 하지만 가장 중요한 설정을 추가해줘야한다  
처음에 만들어진 xinputrc 파일을 수정해줘야한다  

<br />

### xinputrc 파일 수정하기
vim 에디터를 사용해도 되지만, tinker board에서는 vim에서 복사 붙여넣기가 잘 안된다.  

> 터미널에서는 Ctrl+Shift+C 이면 복사가 되서 터미널 환경에서도 잘 사용할 수 있는데...  
여기에서는 안 된다. 

그래서 tinker board 데비안에서 제공하는 mousepad를 사용하자.  

gedit 같은 메모장 프로그램이다. vim, mousepad 를 아무거나 사용

```
mousepad .xinputrc
```

이제 맨 아래줄에 복사해서 넣어주자
```
export XIM=ibus
export xmodifiesr="@im=ibus"
export GTK_IM_MODULE=xim
export QT_IM_MODULE=xim
```
요렇게 추가해주고 저장을 해주면 된다.   

이제 로그아웃을 한 다음에, 다시 로그인을 해주면 한/영 이 잘 바뀐다

