# python-mysql %s 에러 관련
mysql.connector 라이브러리를 사용하다가 %s 변환(?) 에러 발생!

```
SQL syntax; check the manual that corresponds to your MySQL server version
for the right syntax to use near '% 'star' %' at line 5
```

파이썬에서 mysql-connector를 이용해서 DB와 연결을 해서     
cursor를 사용하게 되는데 파라미터 변수에 튜플로 쿼리에 넣을   
데이터를 넣어서 안전하게 쿼리문에 들어갈 데이터를 바꿔주는데     
prepare statement 비슷한 기능인거 같은데..   
어쨋든 DB에 안전하게 데이터를 편하게도 사용할 수 있는 기능인 듯하다.    

```py
query = """SELECT * 
        FROM movie m
        WHERE title like '%%s%';"""
param = (title, )
cursor.execute(query, param)
```

그런데 SQL 쿼리문으로 LIKE 같은 키워드를 사용해서 검색을 하려고 할 때    
중간에 오는 실제 데이터로 바뀔 %s 가 문제가 된다     
문자열 사이에 **LIKE '%검색할-단어%'** 이런식으로 사용하는데 이부분에서     
에러가 발생한다.     

여기저기 검색해보니..  
해결책으로 %%를 두번 넣어라, %%%s%% 이런거도 있었고,
\% %s \% 역시 안됨  
'%#%s%' ESCAPE '#'

<br/>

해결법은  
mysql의 concat() 함수를 사용하는 것, 그 중에 되는 것은   
CONCAT('%', %s, '%') 또는 CONCAT('%%', %s, '%%')   
둘 다 되고 LIKE '%검색할문자열%' 와 같은 효과를 낸다.  

```py
query = """SELECT * 
        FROM movie m
        JOIN rating r
        ON m.id = r.item_id
        WHERE m.title like CONCAT('%', %s, '%');"""
```


# mysql의 DATE_FORMAT() 함수 사용 시 %s 초 관련 에러
위의 것과 약간 비슷하면서도 다른 에러인데   
DB에서 쿼리로 셀렉트문으로 받아오면 그 다음에      
시간데이터를 for문 등을 사용해서 ISO포맷으로 바꿔줘야지   
JSON 등으로 내보낼 때 에러없이 보낼 수가 있는데   
만약 db에서 받은 시간데이터를 변환없이 보내게 되면 에러가 발생하게 된다  

```py
query = """select name, description, num_of_servings, 
        DATE_FORMAT(created_at, '%Y-%m-%d %H:%i:%s') as created_at, 
        DATE_FORMAT(updated_at, '%Y-%m-%d %H:%i:%s') as updated_at
        from recipe Where id = %s;"""
param = (id, )
cursor.execute(query, param)
```

요런식으로 실행할 때 바꿔야할 format 파라미터로 id 변수 한개를 매칭 시켜서  
%s는 1개만 사용하려는 의도 였는데..  
(DATE_FORMAT()의 %s 까지 인지를 해서   
"너 id 값 하나만 줬자나, 한 개 더 내놔~!" 하고 에러를 발생시키는 것임.  
그래서..  

계속 원래 %s 데이터로 바꿀 파라미터가 부족하다는 에러가 발생하는 것    


<br/>

이거는 버그 비슷한 것? 아마도 충돌이라고 하는 게 맞는거 같다..

어쨋든 해결책은 초(seconde) 변환에 %s 대신에 **%S** 를 사용하면   
정말 간단하게 해결된다. ㅋㅋㅋ ㅡㅡㅋ

```py
query = """select name, description, num_of_servings, 
        DATE_FORMAT(created_at, '%Y-%m-%d %H:%i:%S') as created_at, 
        DATE_FORMAT(updated_at, '%Y-%m-%d %H:%i:%S') as updated_at
        from recipe Where id = %s;"""

```
코드는 이런식인데..  


이것도 해결하려고 이거저거 다 갖다 써봤는데 다 안되고;;  

또는 %s (second)를 사용 하지말고, 다른 포맷을 사용해도 된다.   
