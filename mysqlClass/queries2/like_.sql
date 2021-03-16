-- 문자열에 포함된 단어 검색 LIKE (py의 str.contains()같은 메소드)
-- 작가의 fname에 da라는 글자가 들어있는 작가의 책 제목과 작가 이름 조회
-- LIKE 는 대/소문자 구별 안함
-- 실무에서 검색기능을 구현할 때 많이 사용, 네이버나 구글의 검색은 좀 더 차원이 높은 검색(형태소 분석까지 함)이지만,
-- 보통 온라인 서비스에서는 LIKE 로 구현이 가능

SELECT title, author_fname, author_lname FROM books
WHERE author_fname LIKE 'da' ;  -- 정확하게 일치하는 것을 찾음

SELECT title, author_fname, author_lname FROM books
WHERE author_fname LIKE '%da%' ;  -- d 앞에 다른 글자가 있어도 되고 없어도 됨 , a 뒤에서 글자가 있어도되고 없어도 된다

SELECT title, author_fname, author_lname FROM books
WHERE author_fname LIKE 'da%' ;  -- da로 시작해야함, 뒤에는 있어도 되고 없어도 됨

SELECT title, author_fname, author_lname FROM books
WHERE author_fname LIKE '%da' ; -- 앞에는 단어가 있어도 되고 없어도 됨, 끝에는 %가 없으므로 da로 끝나야한다


-- LIKE underscore _
-- int형을 찾을 때 사용한다,  언더스코어가 _ 1개 이면 1자리, __ 2개이면 2자리, ___3개이면 3자리로 찾는다
SELECT title, stock_quantity 
FROM books;

SELECT title, stock_quantity
FROM books
WHERE stock_quantity like '__'; -- 언더스코어가 2개 이므로 2자리를 찾는다

-- 실무에서는 전화번호를 찾을 때 사용할 수 있다 
-- 예: (032)123-3607 LIKE '(___)___-____'   -- ___ 3자리 -___ 3자리 - ____4자리

SELECT title FROM books
WHERE title LIKE '\%'; -- escape처리를 해주면 \ 순수 %가 들어간것을 찾는다


SELECT title FROM books
WHERE title LIKE '%\%%';  --  LIKE에서 %를 사용하고 싶으면 이스케이프를 해주고 앞뒤로 %를 써주면 앞뒤상관없이 %가 들어간 것을 찾는다

SELECT title FROM books
WHERE title like '%\_%';  -- LIKE에서 _언더스코어가 포함된 것을 사용하고 싶을 때는 역시 이스케이프를 해줘야한다 \_ 한 후 앞뒤로 %를 사용해주면 됨


-- 제목에 stories가 포함된 데이터를 제목만 조회하시오
SELECT title FROM books
WHERE title LIKE '%stories%';

SELECT * FROM books;

-- 가장 긴 책을 찾아서, 제목과 페이지수를 조회하시오
SELECT  title, pages FROM books
ORDER BY pages DESC LIMIT 1;

-- 가장 최근에 발간된 책 3권을 찾아서, 책의 제목과 발간년도를 조회하되, 다음처럼 하이픈(-)을 붙여서 조회하시오
SELECT concat(title, ' - ', released_year) as summary 
FROM books
ORDER BY released_year DESC limit 3;

-- author_lname에 공백(" ")이 들어있는 사람의, 책 제목과 author_lname을 조회
SELECT title, author_lname 
FROM books
WHERE author_lname LIKE '% %';

-- 가장 stock_quantity가 적은 책 3권의 title, year, stock_quantity를 조회하시오
SELECT title, released_year, stock_quantity 
FROM books
ORDER BY stock_quantity ASC limit 3;

-- 
SELECT title, author_lname 
FROM books
ORDER BY author_lname, title;