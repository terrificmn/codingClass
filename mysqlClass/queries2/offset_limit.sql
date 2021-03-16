-- limit 와 offset
SELECT *
FROM books limit 5; -- 처음부터 5개의 데이터만 가져온다 (한개만 쓰면 그 자체가 limit (처음부터 데이터를 가져온다))

SELECT *
FROM books limit 5, 5; -- 5번째부터 5개의 데이터를 가져온다 (왼쪽이 offset 된다, limit은 5)

SELECT *
FROM books limit 10, 5; -- 10번째부터 5개의 데이터를 가져온다 (왼쪽이 offset 된다, limit은 5)

-- 이를 클라이언트에서 URL을 통해서 보내게 되면 서버쪽 api서버에서 파이썬으로 변수로 받아서 쿼리를 작성할 수 있다
-- query = 'SELECT * FROM books LIMIT {}, {}'.format(offset, limit)


-- 출간년도가 최신순으로, 책 5권을 조회하시오 limit 5
SELECT *
FROM books
ORDER BY released_year DESC LIMIT 5;

-- 그 다음 최신 순5개씩 offset이 5로 바뀜
SELECT *
FROM books
ORDER BY released_year DESC LIMIT 5, 5;

-- 그 다음 최신 순5개씩 offset이 10로 바뀜
SELECT *
FROM books
ORDER BY released_year DESC LIMIT 10, 5;

-- 그 다음 최신 순5개씩 offset이 15로 바뀜
SELECT *
FROM books
ORDER BY released_year DESC LIMIT 15, 5;