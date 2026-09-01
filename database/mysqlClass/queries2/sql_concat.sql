show databases;
use my_edu_db;

create table books (
	book_id int not null primary key auto_increment,
    title varchar(100),
    author_fname varchar(100),
    author_lname varchar(100),
    released_year int,
    stock_quantity int,
    pages int
);

select * from books;

-- concat으로 합치기
SELECT concat('hello', '...', 'welcome', '!!');

SELECT concat(author_fname, ' ', author_lname)
from books;

SELECT concat(author_fname, ' ', author_lname) as 'full name' 
from books; 

SELECT author_fname, author_lname FROM books;

SELECT author_fname as 'first', author_lname as 'last'
FROM books;

-- first, last, full name으로 합치기 
-- full name컬럼은 없으므로 as로 만들어 준다: concat을 이용해서 author_fname 과 author_lname을 합친다
SELECT author_fname as 'first', author_lname as 'last', concat(author_fname, ' ', author_lname) as 'full name'
FROM books;

-- concat_ws ('string', 컬럼1, 컬럼2, ...) ---> 컬럼들 사이에 넣어준다
SELECT concat_ws(' : ', title, author_fname, author_lname) FROM books;



SELECT replace(title, ' ', '->') as replaced_title
FROM books;

SELECT author_lname as 'forwards', reverse(author_lname) as 'backwards'
FROM books;

SELECT upper(concat(author_fname, ' ', author_lname)) as 'full name in caps'
FROM books;

SELECT concat(title, ' was released in ', released_year) as 'blurb'
FROM books; 

SELECT title, char_length(title) as 'character count' 
FROM books;

SELECT concat(substring(title, 1, 10), '...') as 'short title',
	concat(author_lname,', ',author_fname) as 'author',
	concat(stock_quantity, ' in stock') as 'quantity'
FROM books 
WHERE (author_lname = 'Gaiman' and stock_quantity = 12) 
	OR (author_lname = 'Eggers' and stock_quantity = 104);







