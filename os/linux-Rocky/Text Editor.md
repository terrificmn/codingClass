# Text Editor
geditor를 많이 사용했으나, fedora 40? 즈음 해서 gnome text editor를 사용하게 되는데  
command line 으로 실행 할 경우에는  
`gnome-text-editor` 로 실행을 하면 된다. 


## 스펠링 체크
gnome-test-editor를 사용하다 보면 spell checking 으로 인해서 빨간색 밑줄이 생기는데  
이는 일단 영어는 스펠링 체크를 하는데 한글에 대한 것은 없어서 그렇다. 

hunspell 이라는 패키지를 사용해서 스펠링 체크를 하는 듯 한데  
```
dnf list hunspell\*
```

로 해보면 install 되어 있는 패키지와 설치할 수 있는 패키지를 알려준다. 조금 시간이 걸림  

이 중에 hunspell-ko.noarch  있는데 설치하면 된다 
```
sudo dnf install hunspell-ko-0.7.0-19.fc40.noarch 
```

> hunspell-ko 후 탭으로 자동 완성


그놈 에디터로 문서를 열고 마우스 오른쪽 버튼을 눌러서 Language 선택 -> Korean -> Korean (South Korea)를 선택하면 된다.

이렇게 해주면 무조건 한글은 밑줄이 생기는 것이 없어진다.  
단 외래어는 무조건 빨간색이 생기는 듯 하다.  




