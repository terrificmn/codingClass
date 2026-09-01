Rocky Linux 9.0을 설치하고 나면  
한글 관련 패키지가 설정이 안되어 있기 때문에 setting에서 키보드에서 한글을 추가해도  
한글이 되지 않는다  

그래서 터미널에서 설치
```
sudo dnf install ibus-hangul
```

이제 로그아웃을 한번 한 다음에  
다시 settings->keyboard에서 Input Sources 를 추가하면  
korean을 검색하면 **Korean(Hangul)**이 나온다  

이제 추가를 한 후에 오른쪽 상단 화면에서 한글 키보드로 바꿔주면 된다   

fcitx-hangul 처럼 따로 설정할 필요가 없어서 편하다  

> Alt right 키로 한글키만 바꿔주면 됨



