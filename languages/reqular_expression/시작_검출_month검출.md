# regular expression

아래와 같은 문자열이 있을 때 
```
drwxr-xr-x 48 user user 4096 Apr 25 17:59 build
-rw-rw-r--  1 user user 8666 Apr 25 16:54 gazebo.png
April 25 2023
```


Expression 을 이렇게 사용하면 된다. 2개로 그룹화를 시켜서 패턴을 만듬
```
(^d)|(Apr\b)
```
이 된다   


()를 이용해서 group화를 했고,  
^는 시작하는 문자열을 찾아주는 것이고, d 만 한정이다   
month를 검출할 때 Apr\b 는 딱 원하는 3글자를 골라내고 (첫번째는 대문자)   
그리고 \b 는 word boundary로 패턴이 해당 워드(full word) 로만 찾아주고, 다른 워드가 Apr를 포함하는 긴 단어라면  
해당 문자는 match 되지 않게된다   

위의 패턴의 결과는 아래 처럼...   
<font color="red">**d**</font>rwxr-xr-x 48 user user 4096 <font color="red">**Apr**</font> 25 17:59 build   
April 25 2023


또 다른 방법으로는 ([Apr]{3}) 이런식으로 패턴을 할 수 있지만 {number}는  해당 숫자만큼 매칭해준다   
다른점은 Apr이 포함되는 다른 단어도 매칭이 된다는 점 참고   

차이점 비교..   
<font color="red">**d**</font>rwxr-xr-x 48 user user 4096 <font color="red">**Apr**</font> 25 17:59 build   
<font color="red">**Apr**</font>il 25 2023

