## sql 특정 컬럼 숫자 +1 시켜주기 (UPDATE 쿼리)

* likehits는 컬럼
likehits = '+1' will not actually add one to a field  
instead it will just assign literal +1 to likehits column value.  
'문자열' 넣어지게 되는 듯  
In order to add 1 try this  

```
UPDATE article 
SET likehits = likehits + 1
WHERE id ='129'
```

However, it looks like likehits column is of type nvarchar,   
if so then try this (assuming likehits column stores only numbers)  

```
UPDATE article 
SET likehits = CAST((CAST(likehits AS INT) + 1) AS nvarchar(64)) 
WHERE id ='129'
```

컬럼 type이 int형 이어서 그냥 +1 해줬더니 무리없이 +1 더해서 수정됨   


