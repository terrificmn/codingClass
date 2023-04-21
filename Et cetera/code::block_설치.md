# code::block 설치
우분투의 경우에는 20.04 기준
```
sudo apt install codeblocks
```
무난하게 잘 설치가 된다 


## cbp, layout 파일 만들기   
프로젝트 통째로 열기가 참 힘들다. 프로젝트를 새로 만들때는 상관이 없겠지만   
주로 vscode를 사용하고 싱글보드컴퓨터에서 사용할 예정인데, 기존의 패키지에서 열어야 하는데   
그게 안된다.;;;

그래서 파일 2개를 일단 만들어서 해당 프로젝트 안에 넣어준다   

```
cd ~/my_pkg
touch my_pkg.cbp my_pkg.layout
```

> 파일명은 디렉토리, 또는 패키지(프로젝트) 명으로 해주고, 확장자는 cbp 로 해준다 `{패키지}.cbp`

그리고 나서 하나씩 열어서 수정해준다   
먼저 cbp 파일  
```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<CodeBlocks_project_file>
	<FileVersion major="1" minor="6" />
	<Project>
		<Option title="c++_socket" />
		<Option pch_mode="2" />
		<Option compiler="gcc" />
		<Build>
			<Target title="Debug">
				<Option output="bin/Debug/c++_socket" prefix_auto="1" extension_auto="1" />
				<Option object_output="obj/Debug/" />
				<Option type="1" />
				<Option compiler="gcc" />
				<Compiler>
					<Add option="-g" />
				</Compiler>
			</Target>
			<Target title="Release">
				<Option output="bin/Release/c++_socket" prefix_auto="1" extension_auto="1" />
				<Option object_output="obj/Release/" />
				<Option type="1" />
				<Option compiler="gcc" />
				<Compiler>
					<Add option="-O2" />
				</Compiler>
				<Linker>
					<Add option="-s" />
				</Linker>
			</Target>
		</Build>
		<Compiler>
			<Add option="-Wall" />
		</Compiler>
		<Extensions />
	</Project>
</CodeBlocks_project_file>
```

아래의 태그들만 수정해주면 된다  
```xml
<Project>
    <Option title="my_pkg" />
..생략
    <Build>
        <Option output="bin/Debug/my_pkg" prefix_auto="1" extension_auto="1" />

    ... 생략...
        <Option output="bin/Release/my_pkg" prefix_auto="1" extension_auto="1" />
```

Project 의 Option title 태그 부분을 기존에 있는 패키지로 수정하고   
예를 들어 `my_pkg` 로 수정해준다    




`{패키지}.layout` 예를 들어 my_pkg.layout 으로 만들어 진 파일을 열어서 복사해준다 
따로 수정할 부분은 없다
```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<CodeBlocks_layout_file>
	<FileVersion major="1" minor="0" />
	<ActiveTarget name="Debug" />
</CodeBlocks_layout_file>
```

그 다음에 open 아이콘 (파랑색)으로 해당 디렉토리로 이동해서 열어주는데 위에 만든 cbp 파일을 선택해주면 된다     
(또는 메인화면의 Open an existing project를 눌러준다)


## 파일 추가하기
파일을 추가해줘야 한다. Project 메뉴-> Add file recursively 를 눌러서 해당 패키지 디렉토리를 선택해준다  
여기에서 체크 박스로 추가해야할 파일들을 선택해주면 된다   

> 조금 불편하지만 워낙 램을 적게 잡아먹어서 싱글보드 컴퓨터에 딱 일 듯 하다   






