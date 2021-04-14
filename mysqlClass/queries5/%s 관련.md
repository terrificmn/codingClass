 SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '% 'star' %' at line 5


해결책으로 %%를 두번 넣어라, %%%s%% 이런거도 있었고, \% %s \% 역시 안됨
'%#%s%' ESCAPE '#'

해결법은
mysql의 concat() 함수를 사용하는 것, 그 중에 되는 것은 
CONCAT('%', %s, '%') 또는 CONCAT('%%', %s, '%%') 
둘 다 되고 LIKE '%star%' 와 같은 효과를 낸다

```
query = """SELECT * 
                    FROM movie m
                    JOIN rating r
                    ON m.id = r.item_id
                    WHERE m.title like CONCAT('%', %s, '%');"""
```
차이 점 테스트 해볼 것


___

날짜를 표시할 때 
%s 시간표시는 이렇게 되는데 
이게 또 %s mysql param을 사용할 때 또 문제가 된다 
이때는 %s를 %S 대문자로 바꿔서 사용해준다. 

