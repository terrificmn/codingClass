# DB 테이블에, 만약 한 개의 테이블에 모든 컬럼을 만든다면... 

customers 테이블이 있다고 가정을 하자~

이 테이블에 id, name, email, order_at, amount
의 컬럼이 있다고 하면..  
유저는 매번 물건을 살 때마다 name, email, order_at, amount 컬럼에  
이름, 이메일, 물건을 산 시간, 수량등을 적어줘야하는 문제가 생기고
  
또한 물건을 안 사람에게는 order_at, amount NULL 들어가서   
이럴 때 무결성이 깨지게 되는 문제가 발생한다

<br>

# 테이블 정규화
정규화: 테이블을 작게 나눠서 서로 relationship이 생길 수 있게 만들어 주는 작업

이럴 때에 테이블을 2개로 세분화해서 customers, orders 테이블로 나눠준다

이때의 테이블 구성은 아래처럼 된다  
customers 테이블에는 customer를 알 수 있는 유니크한 컬럼을 하나 만들어 줘야 하는데  
이런 역활은 id로 주로 사용한다. 그래서 id 컬럼이 primary key, auto_increment가 되게 만들어주고    
컬럼은 id, name, email 만 있으면 된다.

orders 테이블에도 
order_id (또는 id) 가 primary key가 되고, 
이 컬럼은 order테이블의 고유 유니크한 키가 된다.  
이제 customers 테이블을 참조할 수 있게 foreign key 설정을 해줘야 한다. 
외부키라 불리는 것은 customers_id 로 컬럼을 만들고,    
이제 customers 테이블의 id를 참조하게 된다.  

이제 order_id, customer_id, order_at, amount 컬럼만 있으면 된다.

<br>

customers 테이블 : id, name, email까지
orders 테이블 : customer_id, order_id, order_at, amount


| id | name | email | | customer_id | order_id | order_at | amount |
|--|--|--|--|--|--|--|--|
| 1 | John | john@email.com | | 1 | 100 | 2021-03-17 | 5 |
| 2 | Sara | sara@email.com | | 2 | 110 | 2021-02-15 | 15 |
| 3 | Smith | smith@email.com | | 3 | 1011 | 2021-01-05 | 1 |
| 4 | Joe | joe@email.com | | 4 | 150 | 2021-01-30 | 4 |

<br>

위의 표처럼 

customers의 테이블의 id 는 primary key 이고   
이것을 orders테이블에서 참조하도록 만들었기 때문에 
데이터가 입력이 되면    
customers테이블의 id는 orders테이블의 custmoer_id 값이 같게 된다.  

orders 테이블에서 볼 때 이것은 foreign key가 된다.  
왜냐하면 외부에서 참조하는 키이기 때문이다.   

그래서 2개의 테이블로 join을 하면   
바로 customer_id를 통해서 
order테이블에서도 고객 정보를 알 수 있게 된다,   



