-- 레퍼런스 페이지
-- https://www.tutorialspoint.com/mysql/mysql-date-time-functions.htm

CREATE TABLE people (
	name varchar(100),
    birthdate date,
    birthtime time,
    birthdt datetime
);

INSERT INTO people (name, birthdate, birthtime, birthdt)
VALUES ('Padma', '2000-11-11', '10:07:35', '2000-11-11 10:07:35');

INSERT INTO people	-- 컬럼을 다 insert하는 경우에는 생략가능
VALUES ('Larry', '1988-12-25', '04:10:42', '1988-12-25 04:10:42'); 
-- date 포맷으로 type이 설정되어 있으면 ISO 형식으로 문자열로 넘겨줘도 시간으로 잘 들어가짐

SELECT * FROM people;

-- 현재 날짜 구하기
SELECT curdate();  -- UTC 기준으로 들어가짐  

-- 현재 시간 구하기
SELECT curtime();

-- 현재 날짜 시간 구하기
SELECT now();


DESC people;

INSERT INTO people 
VALUES ('Mike', curdate(), curtime(), now());

SELECT * FROM people;


SELECT name, birthdate
FROM people;

-- day() 함수 사용하기 , 날짜만 리턴
SELECT name, day(birthdate)
FROM people;

-- dayname() 함수 사용하기, 요일
SELECT name, dayname(birthdate)
FROM people;

-- 요일을 숫자로 가져온다  1: Sunday ~ 7: Saturday
SELECT name, dayofweek(birthdate)
FROM people;

-- 1월 1일을 1로 놓고, 몇일째인지를 알려준다
SELECT name, dayofyear(birthdate), birthdate
FROM people;

-- 함수 사용할 때 레퍼런스를 확인하여 사용!  -- time 에다가 년도 관련 함수를 사용하면 정확하게 나오지 않음
SELECT name, dayofyear(birthtime), birthtime
FROM people;

-- 레퍼런스 페이지
-- https://www.tutorialspoint.com/mysql/mysql-date-time-functions.htm

SELECT name, birthdt, Month(birthdt)
FROM people;

SELECT name, birthdt, monthname(birthdt)
FROM people;


SELECT name, birthtime, hour(birthtime)
FROM people;

SELECT name, birthtime, minute(birthtime)
FROM people;

SELECT name, birthtime, second(birthtime)
FROM people;

-- date_format() 에 %을 이용해서 포맷 바꾸기 , %m 등 자세한 것을 레퍼런스 참조
SELECT date_format( birthdt, '%m/%d/%Y')
FROM people;

SELECT date_format( birthdt, '나는 %W 에 태어났다')
FROM people;

SELECT date_format(birthdt,'%Y/%m/%d at %h:%i')
FROM people;

