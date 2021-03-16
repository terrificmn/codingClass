SELECT * FROM books;

INSERT INTO books (title, author_fname, author_lname, released_year, stock_quantity, pages)
VALUES ( '10% Happier', 'Dan', 'Harris', 2014, 29, 256),
( 'fake_book', 'Freida', 'Harris', 2001, 287, 428),
( 'Lincoln In The Bardo', 'Georage', 'Saunders', 2017, 543, 234);

SELECT author_lname FROM books;

-- 중복 제거 하기 distinct 
SELECT distinct author_lname from books;

-- full name으로 중복제거해서 유니크하게 데이터 가져오기
SELECT distinct concat(author_fname, ' ', author_lname) as 'Full_name'
FROM books;

SELECT * FROM books;

-- 컬럼은 유지하면서 유니크하게 만들기
SELECT distinct author_fname, author_lname 
FROM books;

-- 정렬하기 ORDER BY 키워드
SELECT * FROM books;

SELECT author_lname FROM books
ORDER by author_lname;

SELECT * FROM books
ORDER by author_lname;

SELECT * FROM books
ORDER BY title;

-- 타이틀 컬럼 내림차순으로 정렬하여 모든 컬럼 조회하시오
SELECT * FROM books
ORDER BY title desc;

-- 출간년도 내림차순으로 정렬하여, 책 이름과 출간년도를 조회하시오 
SELECT title, released_year 
FROM books
ORDER BY released_year DESC;

-- 위의 문제를 오름차순으로 
SELECT title, released_year 
FROM books
ORDER BY released_year ASC;  -- 생략하거나 ASC ascending 을 적어준다

-- 작가의 fname과 lname으로 정렬해서 모두 다 조회하시오.
SELECT * FROM books
ORDER BY author_fname, author_lname;

-- 위의 정렬 컬럼들은, 각각 따로 정렬 조건이 가능하다
SELECT * FROM books
ORDER BY author_fname DESC, author_lname ASC;

