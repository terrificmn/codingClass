-- substring
SELECT substring('Hello World', 1, 4);
SELECT substring('Hello World', 7);
SELECT substring('Hello World', -3);
SELECT substring('Hello World', 1, -3);


-- select title within 10 letters to client
SELECT substring(title, 1, 10) as title
FROM books;

SELECT * FROM books;
SELECT substring(title, 1, 10) as title, author_fname, released_year, pages
FROM books;

-- 실무에서 쓰이는 
SELECT concat( substring(title, 1, 10) , '...') as 'short_title'
FROM books;

-- replace('string', '해당 문자열', '바꿀 문자열')
SELECT replace('What the hell', 'hell', '***');
SELECT replace('cheese bread coffee milk', ' ', ',');
SELECT replace('cheese bread coffee milk', ' ', ' and ');

SELECT * FROM books;

SELECT replace(title, 'e', '3')
FROM books;

-- 문자열의 순서를 바꾸는 함수 reverse 함수
SELECT reverse('Hello World');
SELECT reverse(author_fname) FROM books;

-- 문자열 길이를 알려주는 함수 char_length 함수
SELECT char_length('Hello World');

-- 책 제목의 길이를 조회하시오
SELECT char_length(title)
FROM books;

-- 위처럼 조회를 하면 컬럼명이 char_length(title) 로 나오기 때문에 as로 바꿔준다
SELECT char_length(title) as title_length
FROM books;

-- author_lname 의 길이를 구해서
-- 'mike's name length is 4' 
SELECT concat( author_lname, '\'s name length is ', char_length(author_lname)) as 'author\'s name and length'
FROM books;


-- 대문자 소문자 변환 upper() lower() 함수
SELECT upper('hello world');
SELECT lower('HELLO WORLD');

SELECT upper(title) FROM books;