# fedora 설치 화면 들어가지 않을 경우
아마도 노트북에서 Nvidia 외장 그래픽을 사용하는 경우에 그런 듯 하다.  
데스크탑에서는 nvidia로 해본적이 없어서;;; 잘 모르겠음   

usb 부팅이 정상적으로 만들어졌지만, 뭔가 콘솔화면에 로그만 찍힌 후 아무런 반응이 없을 경우에  

usb로 부팅을 한 후에 처음 Grub 메뉴에서   
Start Fedora-Workstation-Live 38 화면에서 *e* 키를 눌러서 command를 수정

대충 quiet rhgb 다음에 nouveau.modeset=0 를 입력해주면 된다.

이런 식으로 넣어준다. 마지막 줄에 넣어주면되면 initrdefi 줄은 나둔다.
```
linuxefi /images/pxeboot/vmlinuz root=live:CDLABEL=Fedora-WS-Live-3\8-1-6 rd.live.image quiet rhgb nouveau.modeset=0
initrdefi /images/....
```

이 상태에서 ctrl+x 를 눌러서 부팅을 해주면 설치화면이 잘 실행이 된다.

이 모드는 GPU를 disable 하면서 CPU (인텔 내장 그래픽 위주 인 듯 함) 로 사용할 수 있게 해준다. 

이후 rpmfusion 리포지터리를 이용해서 nvidia 드라이버를 설치해주면 위의 옵션이 없이도 부팅이 가능하다.

> nvidia 드라이버가 설치가 안 된다면 위의 옵션을 부팅 할 때마다 넣어줘야 한다. grub 업데이트를 해서 고정시킬 수도 있지만   
nvidia 드라이버를 설치하자




