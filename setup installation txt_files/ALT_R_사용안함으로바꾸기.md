키보드를 바꿨는데 여기에는 한영키 자체가 없고 오른쪽 ALT로 같이 사용하게 되어 있음  
그런데 제조사에는 오른쪽 alt키는 사용안되고 한글키로만 사용되는 것이라고 설명되어 있었으나 역시나 리눅스에서는 안 먹힌다.

먼저 리눅스 자체 셋팅을 들어가서 Region & Language 를 들어가면
INPUT 소스를 설정할 수 있는데 여기에서  Korean (Hangul)의 설정 톱니바퀴 모양을 클릭해서 한글 토글 키를 추가해주는데 ADD를 클릭하고 오른쪽 alt를 눌러주면
이제 오른쪽알트키는 한글전환용으로 사용됨

하지만 문제가 있는게,,
브라우저에서도 문제가 없지만 vscode를 사용할 때 안됨;;
오른쪽알트키를 누르면 메뉴가 선택이 되버림;; settings.json으로 바꿔보라고 하는 인터넷 의견이 많았지만 거의다 메뉴를 숨기는 설정이거나, 메뉴가 선택이 안되게 하는 것인데
결론은 한영 전환 자체가 안되서 실패

그러면 답은 shift+space 로 한영전환을 할 것인가? 하다가
uim이라는 프로그램을 변환해 줄 수 있다고 해서 찾아봤음
( A multilingual input method library )

우분투에서는 
```
$ sudo apt install uim
```

하지만 나는 우분투 유저가 아님;; centOS 인데 일단 yum으로는 없다고 나온다;;
다행히 rpm으로 구할 수 있었음
참고 다운로드
https://rpms.remirepo.net/rpmphp/zoom.php?rpm=uim

34버전만 다운로드 되었던것 같음

특정유저와 특정그룹이 없다고 나오는데;; 그냥 무시함;
```
$xmodmap
```
실행해보면 요렇게 나옴
xmodmap:  up to 4 keys per modifier, (keycodes in parentheses):

shift       Shift_L (0x32),  Shift_R (0x3e)
lock        Caps_Lock (0x42)
control     Control_L (0x25),  Control_R (0x69)
mod1        Alt_L (0x40),  Alt_R (0x6c),  Meta_L (0xcd)
mod2        Num_Lock (0x4d)
mod3      
mod4        Super_L (0x85),  Super_R (0x86),  Super_L (0xce),  Hyper_L (0xcf)
mod5        ISO_Level3_Shift (0x5c),  Mode_switch (0xcb)

그래서 mod1에 등록되어 있는 Alt_R을 삭제시키고 한영키를 등록시키는 작업을 하는 것

본론으로 들어가서 다음은 키 맵핑을 하기
```
$ xmodmap -e 'remove mod1 = Alt_R'
$ xmodmap -e 'keycode 108 = Hangul'
$ xmodmap -pke > ~/.Xmodmap
```
-e가 실행모드인데, 먼저 오른쪽 Alt_R 모드를 지우는 실행
그리고 keycode 108 = Hangul로 한영키를 등록
그리고 마지막 줄은 -pke는  keymap를 출력해주는 것 이라고 함. 이것을 Xmodmap으로 저장
참고
>   -e expression                execute string
    -pm                          print modifier map
    -pke                         print keymap table as expressions


```
xmodmap -pm
```
을 해보면 이제 
mod1        Alt_L (0x40),  Meta_L (0xcd)

Alt_R이 사라져있다. 한영키는 보이지 않지만, 
~ 디렉토리로 이동해서 .Xmodmap 파일을 열어보면
`keycode 108 = Hangul NoSymbol Hangul`
요렇게 등록이 되어 있어서 작동을 하는 것 같다

어쨋든 쓸때 없이 여기저기 봤는데,...;;
처음 설치할 때 mock유저와 mockbuild가 없다는 워닝이 나왔지만 다행히 vscode에서 잘 작동 된다. 오른쪽 알트키를 눌러도 이제는 한영 전환만 되고 메뉴는 팝업되지 않음!! 굿!!

재부팅시에도 적용시키기 위해서 홈디렉토리의 내유저디렉토리에 있는 .bashrc 파일 수정해주기
```
$cd ~
$ vi .bashrc
```
파일이 열리면 아래코드를 입력 후 저장 :wq
```
xmodmap -e 'keycode 108 = Hangul'
xmodmap -pke > ~/.Xmodmap
```
그리고 
``` 
source .bashrc
```
한번 실행시켜주면 잘 작동한다!

참고로..
Alt_R' 은 이미 제거가 되서 그런지 몰라도 .bashrc 파일에 넣으면 재부팅시에
에러가 나면서 안됨. 그래서 넣을 필요는 없는듯..

참고블로그
https://velog.io/@unihit/ubuntu%EC%97%90%EC%84%9C-vscode-%ED%95%9C%EC%98%81%ED%82%A4%EB%A1%9C-%EB%B3%80%ED%99%98%EC%9D%B4-%EB%90%98%EC%A7%80-%EC%95%8A%EC%9D%84-%EB%95%8C
