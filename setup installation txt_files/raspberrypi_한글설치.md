# 한글을 설치하자~

```
$sudo apt install ibus ibus-hangul fonts-unfonts-core
```
ibus는 한글 입력기 이고,     
한글이 깨져서 표현될 때 fonts-unfonts-core를 설치하면 해결된다  

이제 ibus 입력기 설정을 해줘야하는데  
preferences에서 iBus 설정을 누른 후에   
영어만 기본으로 되어 있는데 추가를 눌러서 Korean을 추가해준다  

기억이 헛깔리지만.. 재부팅이 필요할 수도 있다.  
ibus 설정을 하려고 하면  
iBus 데몬을 실행되고 있지 않는다는 메세지와 함께 실행을 물어본다  
Yes를 눌러주자  

<img src=0>

그리고 
라즈베리파이의 preferences에 Raspberry Pi Configuration을 들어가서  
Localisation 탭을 선택하고
Keyboard를 선택해준다  
키보드의 Layout을 Korean으로 선택 그리고 
Viriant를 Korean (101/104 key compatible) 로 선택     
OK를 누른다  

<img src=1>

시간도 설정해주는데  
Timezone의 Set Timezone을 선택한 후, ROK를 선택해주면 된다.    

원한다면 Locale도 Language를 ko (Korean)으로 바꿀 수 있지만, 추천하지는 않음  

>왜냐하면 개인적 의견으로는 메세지를 보거나, 
특히 비거깅이 필요할 때 출력되는 에러, 로그등을 봐야할 경우가 있는데
영어로 나온 것을 키워드로 google 등에서 검색해야할 경우가 많기 때문이다.
