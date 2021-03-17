-- 조건문 case
-- if else처럼 사용할 수 있는데, if는 case when    then else 구조로 사용한다
-- 조건문이 끝나면 end를 써준다
SELECT title, released_year,
	case
		when released_year >= 2000 then 'Modern'
        else '20th Century'
	end as genre
FROM books;


SELECT title, stock_quantity, 
	CASE
		when stock_quantity between 0 and 50
			then '*'
		when stock_quantity between 51 and 100
			then '**'
		else '***'
	end as stock  -- as 로 컬럼명을 만들어주지 않으면 위의 case문처리했던것이 컬럼명이되어서 지저분해짐
FROM books;



-- 1980년 이전에 출판된 책의 제목과 출판년도를 조회
SELECT title, released_year
FROM books
WHERE released_year < 1980;


-- 작가 라스트네임이 Eggers, or Chabon인 사람이 쓴 책의 모든 컬럼을 조회하시오
SELECT * FROM books
WHERE author_lname = 'Eggers' OR author_lname = 'Chabon';


-- 라스트네임이 Lahiri인 사람이 2000년 이후로 출판한 책의 데이터 중 
-- title, author_lname, released_year만 조회하시오
SELECT title, author_lname, released_year 
FROM books
WHERE author_lname = 'Lahiri' AND released_year > 2000;


-- 책 페이지가 100페이지 이상이고 200페이지 이하인 책들의 제목, 페이지를 조회하시오
SELECT title, pages
FROM books
WHERE pages between 100 and 200;


-- lname이 C로 시작하는 작가나, S로 시작하는 작가의 책들에서, title과 lname만 조회하시오
SELECT title, author_lname
FROM books
WHERE author_lname LIKE 'C%' OR author_lname LIKE 'S%';


--  case When then else end 
-- title에 stories가 포함되어 있다면 Short Stories 로 새로운 컬럼을 만들고
-- title이 'Just kids and A Heartbreaking Work' 이면 Memoir 로 해서 
-- 이도저도 아니면 Novel로 해서 컬럼을 Type이란 이름으로 만들어라
SELECT title, author_lname, 
			CASE
				when title LIKE '%stories%'
					then 'Short Stories'
				when title = 'Just kids and A Heartbreaking Work' 
					then 'Memoir'
				else 'Novel'
			END as TYPE
FROM books;            



SELECT * FROM books;


-- 작가별로 책을 1권 썼으면 1book, 책을 2권 이상 썼으면, 
-- 해당 권수에 books를 붙여서 다음처럼 나오게 하시오
SELECT title, author_lname ,
	case 
		when count(*) = 1 
			then
				concat(count(*), ' book') 
		when count(*) >= 2
			then
				concat(count(*), ' books')
	end as COUNT
FROM books
GROUP by author_lname
ORDER by author_lname; 


SELECT
replace(title, substring(title, char_length(title)-7, 6), 'Short Stories')
FROM books
WHERE title LIKE '%stories%';