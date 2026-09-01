# vscode 쓸만한 확장팩 
vscode 쓸만한 확장팩 

<br/>

## Bracket Pair Colorizer
하나는 Bracket Pair Colorizer 라는 것인데 자주 사용되는 () 소괄호 [] 대괄호 {} 중괄호 등을  
동일한 색깔로 매칭을 시켜주는 기능을 해준다  

하지만 vscode - extensions 에서 검색을 해보면 Deprecated 되었다고 나오는데  
그 이유는 vscode 기능으로 통합되었기 때문!  

<img src=0>

그래서 기본 사용이 가능할 것(?)으로 보이는데   
Bracket Pair Colorizer 기능을 사용하려면  

> 새로 vscode를 설치하면 바로 되는지는 확인을 못해 봄

vscode 메뉴에서 File -> Preferences -> Settings 를 눌러서 진입!  

이제 나오는 화면에서 오른쪽 상단의 JSON 보기 아이콘을 눌러준다  

>꼭 JSON으로 추가하지 않아도 설정에서 스크롤을 내리다보면 Text Editor 섹션에   
Bracket Pair Colorization: Enabled 체크하는 부분도 있어서 체크해서 쉽게 설정 가능함

<img src=1>

이제 익숙한(?) JSON 형식에 맞춰서 복사 붙여넣기!
```json
{
    ..생략...
    "editor.bracketPairColorization.enabled": true, 
    "editor.guides.bracketPairs": true
}
```
(중간에 추가해서 넣을 때 ,를 넣어주세요)  


1. editor.bracketPairColorization.enabled 는 기능 자체 켜기   
2. editor.guides.bracketPairs 는 블럭 간에 선으로 연결시켜서 보여준다.  
어느 블럭에 포함되어 있는지 확인할 때 유용

이제 코드에서 볼 때 편하게 colorful(?)하게 볼 수 있다  

<img src=2>

이런식으로 활용하게 됨~  

> 괄호 색깔, 블럭 간에 선으로 연결되서 볼 수 있고, 글자 색은 변하지 않습니다. (다른 테마를 설치해야함)

<br/>

## indent-rainbow 
indent-rainbow 확장팩은 탭 간격을 색으로 표시해주는 기능을 한다  
이번에는 extensions 에서 직접 다운 설치를 해줘야 한다  

vscode 왼쪽화면에서 extensions 아이콘을 클릭 한 후에  
**indent** 라고 검색  

<img src=3>

설치가 완료되면 탭으로 간격을 띄울 때 색깔로 탭 간격이 표시가 된다  
탭 간격을 볼 때 괜찮은 것 같다  
단점은 조금 화려한 정도   

화면에서 이런 식으로 볼 수가 있다   
<img src=4>

<br/>

## etc
그 밖에 자신의 쓰고 있는 언어, 프레임워크 관련해서 많은 확장팩들이 있으므로   
검색하면 사용하면 될 듯~

현재 쓰고 있는 것들은  
ROS, DotENV, C/C++ 등등.. 있다.  
