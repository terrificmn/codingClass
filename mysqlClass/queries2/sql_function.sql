

SELECT upper(concat('My favorite author is ', author_fname, " ", author_lname, "!")) as yell
FROM books 
ORDER BY author_lname;

-- 전체 데이터의 갯수 구하기. count()함수
-- books 테이블의 행(row)의 갯수 (데이터의 갯수)
SELECT count(*) FROM books;
SELECT count(*) FROM cats;
SELECT count(*) FROM employees;

SELECT count(author_fname) FROM books;
SELECT count(DISTINCT author_fname) FROM books;  -- unique 한 갯수를 알고 싶을때 (중복)

-- 제목에 the가 들어가 있는 책의 갯수는 몇개인가?
SELECT count(title) FROM books
WHERE title LIKE '%the%';

-- 요약 summarize / aggregate 집계
-- author_lname으로 묶어서 lname과 그 사람의 책의 갯수를 조회하시오

SELECT author_lname, count(*) FROM books  -- distict와 비슷하지만, group by를 사용하면 그룹으로 묶인 것에 대한 추가 질의 가능
GROUP by author_lname;  -- 

SELECT count(*), author_fname, author_lname  FROM books
GROUP by author_fname, author_lname;

-- 년도별로 몇권의 책이 발간되었는가? 년도와 책의 갯수로 조회하시오
SELECT released_year, count(*) FROM books
GROUP by released_year 
ORDER by released_year;  -- 정렬은 마지막에 한다

-- 최소값, 최대값 구하기
-- 가장 최소 연도를 구하기
SELECT min(released_year)
FROM books;

SELECT max(released_year)
FROM books;

-- 페이지가 가장 많은 책은?
SELECT * FROM books;
SELECT max(pages), title, author_fname, author_lname FROM books;

-- subquery 방식으로 위의 문제 해결  (query 안에 SUB쿼리가 들어있는 방식)
SELECT * FROM books
WHERE pages = ( SELECT max(pages) FROM books );

-- 연도가 최대인 연도의 데이터를 모두 조회하시오
SELECT * FROM books
WHERE released_year = (
						SELECT max(released_year) FROM books);
                        
SELECT * FROM books
order by released_year DESC limit 1;

-- 이 테이블의 책을 모두 페이지를 합하면 모두 몇 페이지인가?
 SELECT sum(pages) FROM books;  -- 합계

 SELECT avg(pages) FROM books;  -- 평균 구하기

-- 전체 책의 갯수는?
SELECT count(title) FROM books;

-- 매년마다 몇권씩의 책이 출간 되었는지 조회하시오
SELECT released_year, count(*) as book_cnt FROM books
GROUP by released_year
ORDER by book_cnt desc; -- 그룹화 후 select를 했기때문에 book_cnt로 정렬할 수 있다

-- stock quantity 총 합은?
SELECT sum(stock_quantity) FROM books;

-- 각 작가별로 출간년도의 평균을 구하시오
SELECT author_fname, avg(released_year) as average
FROM books
GROUP by author_fname;

-- 가장 긴 책을 쓴 사람의 full name을 조회하시오
SELECT concat(author_fname, ' ', author_lname) as 'full name', pages
FROM books
WHERE pages = ( SELECT max(pages) FROM books);

SELECT * FROM books;

SELECT released_year as 'year', count(*) as '# books', avg(pages) as 'avg pages'
FROM books
GROUP by released_year
ORDER by released_year; -- SELECT가 되었기 때문에 as year로 만든 것을 사용해도 됨 ORDER by year;


-- 각 작가별로, 최초로 책을 출간한 년도를, 작가 이름과 함께 조회하시오
SELECT concat(author_fname, ' ', author_lname) as 'author',
min(released_year) as 'first_released_year'
FROM books
GROUP by author_fname, author_lname
ORDER by author;
