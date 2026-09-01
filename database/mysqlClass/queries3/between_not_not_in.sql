

-- 생일(birthdt)이 1999년(포함)과 2021년 사이인 사람의 
-- 데이터만 가져오시오   
SELECT * 
FROM people
WHERE birthdt >= '1980-01-01' and birthdt <= '2021-01-01';

-- 같은 결과
-- BETWEEN 사용
SELECT * 
FROM people
WHERE birthdt between '1980-01-01' and '2021-01-01';


-- 출판년도가 2004년(포함)과 2015년(포함) 사이가 아닌 책들만 
-- 데이터를 가져오시오  -- NOT 사용하기
SELECT * 
FROM books
WHERE released_year NOT between 2004 and 2015;



-- 출판년도가 2017년, 1985년, 2010년, 2014년, 2008년인
-- 데이터를 가져오시오
SELECT *
FROM books
WHERE released_year = 2017 OR
	released_year = 1985 OR
    released_year = 2010 OR
    released_year = 2014 OR
    released_year = 2008;
    
-- 여러개의 데이터를 확인할 때는  IN 을 사용 
-- 파이썬 처럼 사용할 수 있지만 리스트는 없고, () 괄호안에 넣어서 사용
SELECT *
FROM books
WHERE released_year in (2017,1985, 2010, 2014, 2008);


-- 출판년도가 2000년, 2002년, 2004년, 2014년, 2017년이 아닌 데이터만 가져오시오
SELECT *
FROM books
WHERE released_year NOT in (2000, 2002, 2004, 2014, 2017);


-- 출판년도가 2000년 이상이고 홀수년도의 책들만 가져오시오
SELECT *
FROM books
WHERE released_year >= 2000 AND released_year % 2 != 0;


