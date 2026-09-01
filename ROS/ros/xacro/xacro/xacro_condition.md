# if statement

`xacro:marco` 를 이용해서 if 문을 사용하 ㄹ수 가 이쓴ㄴ데  
xacro:property를 등록을 해주고   


```xml
<xacro:if value="${values}">
```

문자열은 

```xml
<xacro:if value="${values == '111'}">
    <!-- 내용 -->
</xacro:if>
```

숫자는 
```xml
<xacro:if value="${values == 1 }">
    <!-- 내용 -->
</xacro:if>
```

if 를 다 사용하고나서 block을 닫아야 한다 
```xml

```

그 밖에 else 경우

```xml
<xacro:unless value="${reflect}">
    <!-- 할 내용 -->
</xacro:unless>
```




