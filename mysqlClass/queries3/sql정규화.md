db테이블을 만들 때 

> 예:
id, name, email, order_at, amount
의 컬럼이 있는 테이블이 있다고 하면
유저는 매번 물건을 살 때마다 name, email, order_at, amount 에
이름, 이메일, 산 시간, 수량등을 적어줘야하는 문제가 생기고
또 
물건을 안 사람에게는 order_at, amount NULL 들어가서 
이럴 때 무결성이 깨지게 되는 문제가 발생한다

이 때 테이블을 2개로 세분화해서 쪼개서 
customers, orders 테이블로 나눠서 

customers 테이블에는 customer를 알 수 있는 유니크한 컬럼을 하나 만들게 되고
대개 primary key, auto_increment가 되게 되고
customer_id, order_at, amount

orders 테이블에도 
유니크한 컬럼이 하나 생기게 된다
user_id, name, email 

이렇게 되면 2개의 테이블이 된 것이고 
여기에서 서로 관계를 설정해주게 된다 relationship

이렇게 되면 오더 테이블에는 커스터머에 속해있게 되고 
오더 테이블에는 foreign key를 통해 커스터머의 id을 가리키게 된다

이러면 오더 테이블은 커스터머 테이블에 속해있게 되고 belongsTo 가 되고 
커스터머는 많은 오더를 할 수 있게 되니 hasMany의 관계가 됨

정규화: 테이블을 작게 나눠서 서로 relationship이 생길 수 있게 만들어 주는 작업

<br/>

|||customers| orders ||||
|--|--|--|--|--|--|--|
| id | name | email | | customer_id | order_at | amount |
| 1 | John | john@email.com | | 1 | 2021-03-17 | 5 |
| 2 | Sara | sara@email.com | | 2 | 2021-02-15 | 15 |
| 3 | Smith | smith@email.com | | 3 | 2021-01-05 | 1 |
| 4 | Joe | joe@email.com | | 4 | 2021-01-30 | 4 |

위의 표처럼 
customers의 테이블의 id 는 primary key 이고   
이것을 orders테이블에서 참조해서 custmoer_id 로 가져오게 되는데  
orders테이블에서 볼 때 이것은 foreign key가 된다.  
 왜냐하면 외부에서 참조하는 키이기 때문이다.   
2개의 테이블로 나눠서 관계를 설정하게 되면  
 Order테이블에서도 고객 정보를 알 수 있게 된다,   
 바로 customer_id를 통해서!  


