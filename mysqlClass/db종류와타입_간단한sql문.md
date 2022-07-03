# RDBMS

데이터베이스의 인덱스: 성능 관련 중요

데이터베이스는 많은 테이블로 이루어져 있다.  
파이썬의 판다스 데이터프레임과 비슷한 것이 데이터베이스의 테이블  

다른점은 컬럼이 있고 인덱스가 없음 (row 인덱스)

<br/>

## db 종류 

관계형 데이터 베이스 RDBMS  
Relational DataBase Management System  

- MySQL (오픈소스에서 -> 오파클에서 인수)  

- MariaDB (기존의 mysql을 다시 오픈소스로 만든 것)  

- Postgre

- Oracle: 사용 RDBMS에서 최고 

- Amazon Aurora 는 MySQL 기반으로 만들어 졌으나  
관계형 데이터 베이스에서 데이터를 더 확장할 수 있게 아마존에서 만든 것  
RDBMS에서 데이터가 폭발적으로 늘어나면 한계가 있는데 이를 보안

<br/>

## db의 type

- Numeric Types   
: Int 와 Double을 주로 많이 사용

- String Types  
: Varchar, (가변케릭터형: A variable-length string)    
Char은 만약에 1024길이로 만든다고 하면    
문자열이 입력되고 남은 길이가 전체 공간이 남아있게 되어  
데이터의 낭비가 있게 되는데  
varchar는 입력된 후 나머지 공간은 없애고 저장한다

- Date Types  
: Datetime, Timestamp


<br/>

## RDBMS의 프로그래밍 언어: SQL  
(Structured Query Language)

> 실무에서는 화면 기획서를 받아서    
백엔드쪽에서는 db로 처리할 부분을 테이블 등을 만들어서 설계 한다

<br/>

기본 create sql     
```sql
CREATE TABLE `my_edu_db`.`tests` (
  `name` VARCHAR(10) NOT NULL PRIMARY KEY,
  `age` INT NULL,
COMMENT = '테스트용 테이블 입니다.';
```

USE `dbname` 을 안하고 . 구분자로 지정할 수도 있음



alter 테이블하기  
```sql
ALTER TABLE `my_edu_db`.`cats` 
CHANGE COLUMN `name` `name` VARCHAR(100) NOT NULL ,
CHANGE COLUMN `age` `age` INT NOT NULL ;    
```


회원 테이블을 만드는데 나이, 주소 컬럼을    
NOT NULL로 만든다고 하면,     
나이 컬럼은 아무것도 입력 안하면 0 으로 들어가게 되고    
주소 컬럼은 아무것도 입력 안하면 '' 빈문자열이 들어가게 됨    

이때 default 를 설정해주면 아무 데이터도 안 넣는다면 기본값으로 설정되게 할 수 있음    
sql로 하면 위와 같다

```sql
`name` VARCHAR(10) NOT NULL default '야옹이'
'age' INT NOT NULL default 5
```

<br/>

*참고*
> 이메일 같은 경우는 이미 unique 하다.   
같은 이메일 계정이 여러개 있을 수는 없기 때문에 PRIMARY KEY로 설정할 수도 있지만   
문자열 이기 때문에 RDBMS 성능이 느리다.   
그래서 id 컬럼을 int (auto_increment) 만들어서 사용하게 된다.    
RDBMS에서는 **숫자**형태로 데이터를 가져오는게 성능이 훨씬 좋다


<br/>


## AWS 로 sql 연습
1. AWS에 RDS 만들기로 Mysql RDBMS를 만듬  
2. AWS의 RDS에 접속하기 위해서 DBtool(software) 중에 하나인 MySQL Workbench SW를 로컬 데스크탑에 설치  
3. MySQL Workbench를 통해서, AWS RDS인 MySQL 에 접속    
이때 MySQL Connections 를 이용해서 AWS로 등록한다.    
HOST명에는 본인계정의 AWS RDS의 endpoint를 적어주고    
port 번호 3306, username등을 입력해 준다.     
비번도 저장해서 사용할 수 있으나, 저장은 안함.  
4. 데이터 베이스를 만들어 봄 `CREATE DATABASE '데이터베이스이름';`  
5. 만들어진 DB안에 테이블을 만들었다 -> `CREATE TABLE '테이블이름';`  
6. 만들어진 테이블안에 데이터를 입력 -> `'INSERT INTO ('컬럼명1', '컬럼명2') VALUES ('홍길동', 10);`  
7. 데이터를 검색/ 가져오기 -> `SELECT * FROM '테이블이름';`  
8. 특정데이터 조건으로 검색 -> `SELECT * FROM WHERE name = '홍길동';`  
9. 검색된 데이터를 수정하기 -> `UPDATE '테이블이름' SET name = '' WHERE age = 10;`  
10. 검색된 데이터 삭제 -> `DELETE FROM cat WHERE age = 12;`  


