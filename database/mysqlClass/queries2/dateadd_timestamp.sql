-- 레퍼런스 페이지
-- https://www.tutorialspoint.com/mysql/mysql-date-time-functions.htm

-- 날짜 연산

-- 현재와의 날짜 차이 구하기 
SELECT datediff(now(), birthdate)
FROM people;

--  date_add() 와 파라미터로 INTERVAL 1 MONTH 주기 , 한달뒤의 날짜를 구해준다
SELECT birthdt, date_add(birthdt, INTERVAL 1 MONTH)
FROM people;

SELECT birthdt, date_add(birthdt, INTERVAL 24 SECOND)
FROM people;

SELECT birthdt, date_add(birthdt, INTERVAL 100 DAY)
FROM people;

-- date_add()함수를 안 사용하고도 + - 로 같은 결과를 얻을 수 있다
SELECT birthdt, birthdt + INTERVAL 100 DAY
FROM people;

-- 마이너스도 가능
SELECT birthdt, birthdt - INTERVAL 100 DAY
FROM people;

-- INTERVAL을 여러개 넣을 수 있음
SELECT birthdt, birthdt + INTERVAL 15 MONTH + INTERVAL 15 DAY + INTERVAL 3 HOUR
FROM people;


CREATE TABLE comments (
	content varchar(100),
    created_at timestamp default now() -- 입력할때 default를 설정해두면 Insert를 할 때 바로 시간이 입력되게 할 수 있다
);

INSERT INTO comments (content)
VALUES('야 진짜 재미있는 기사네');

SELECT * FROM comments;
INSERT INTO comments (content)
VALUES('이 물건은 가격이 비싸네'),
	('정말 재미 없는 영화를 봤다.');
    
SELECT * FROM comments
ORDER by created_at DESC;

-- 실무 끝판왕, 글을 수정할 수 도 있다
-- updated 될 때 바로 업데이트 시간이 자동으로 들어가게 하는 것 defult now() on update now()
CREATE TABLE comments2 (
	id int PRIMARY KEY NOT NULL auto_increment,
	content varchar(200),
	created_at timestamp default now(),
    updated_at timestamp default now() on update now() 
);

DROP TABLE comments2;

INSERT INTO comments2 (content)
VALUES('이 물건은 가격이 싸네'),
	('정말 재미 있는 공연을 봤네.');
    
SELECT * FROM comments2;

UPDATE comments2 SET content = '바꿔바꿔' WHERE id = 2;  -- updated_at 컬럼이 수정했을 때 시간이 들어가는것 확인
SELECT * FROM comments2;
