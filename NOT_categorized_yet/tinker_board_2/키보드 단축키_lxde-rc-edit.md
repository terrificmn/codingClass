tinker board 2는 lxde desktop을 사용하고 있는데  
시작 버튼, 검색 버튼, 또는 터미널 실행 키 등이 단축키로 되어 있지가 않다.  

그래서 마우스가 없다면 키보드 만으로 아무것도 할 수가 없다   

그래서 우분투 처럼 Alt+Ctrl+t 키를 누르면 터미널이 이라도 띄울 수 있게 해보자

먼저 ~/.config/openbox/lxde-rc.xml 파일 열어 수정해준다  

xml 파일인데 keyboard 태그 안에 입력해주면 된다  

```xml
<!-- launch termiantor with Ctrl+Alt+t -->
<keybind key="C-A-t">
	<action name="Execute">
		<command>terminator</command>
	</action>
</keybind>
```

> lxde에서 기본으로 제공하는 lxterminal 로 대신 사용하면 된다.   
command에서 terminator를 사용했는데(따로 설치해야함),

이렇게 하면 적어도 마우스 없어도 최소한 터미널을 열어서 프로그램 등을 실행시킬 수는 있다.  