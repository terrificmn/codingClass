# vnc lock
vnc를 사용하다가 실제 컴퓨터에서 스크린 락이 걸리면 풀 수가 없다...  

settings 에서 Power 부분에서  
Dim Screen When Inactive 를 꺼주고   
Blank Screen 도 Never 로 설정   

테스트 진행....





파이어폭스를 사용한다면   

[extensions gnome 사이트 접속](extensions.gnome.org)    

사이트에서 보이는 broswer extension 링크 부분을 눌러서 shell extension을 설치한다   
(Click here to install browser extension)

허용을 해서 설치를 해준다   

파이어 폭스는 없지만 크롬 버전으로 해도 된다  
```
sudo apt install chrome-gnome-shell
```

설치를 하고 나서 다시 위의 extensions.gnome.org 에서   
Allow Locked Remote Desktop 을 검색     

on 버튼을 눌러서 (허용/ 인스토를 해준다)


스크린 락을 걸어도 다시 암호를 입력하면 락이 풀린다  





