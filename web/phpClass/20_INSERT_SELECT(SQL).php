INSERT into posts (subject, content, date) VALUES ('This is the subject', 'This articles worksheet gives good practice with choosing articles that best fit the context of each sentence. An article is a word that comes before a noun.', '2020-11-12 12:08:01);
테이블은 posts
그다음 ()안에는 넣고 싶은 컬럼명이 들어가야하고,
단, id는 auto로 AUTO_INCREMENT로 만들었기 때문에 생략한다.
VALUES ()안에는 실제 data를 컬럼수와 맞게 ''안에 입력한다.


SELECT subject FROM posts;
//posts 테이블에서 subject 컬럼만 가져온다
SELECT * FROM posts;
//posts 테이블에서 모든 컬럼을 가져온다
SELECT * FROM posts where id='1'
//id가 1인 경우에만 posts테이블에서 모든 컬럼을 가져온다
//참고 활용
SELECT * FROM posts WHERE id='1' AND subject='This is the subject';
SELECT * FROM posts WHERE id='1' OR subject='This the subject';
AND를 이용해서 둘만 맞는 경우만 불러오고
OR를 이용해서 둘중에 하나만 맞는 경우에 불러온다


SELECT * FROM posts ORDER BY id ASC;
// ORDER BY 컬럼 ACS (Ascending which means numbers increase like 1, 2, 3)
// 화면에 표시될 때는 top부분에 적은 숫자부터 아래로 오름차순정렬

SELECT * FROM posts ORDER BY id DESC;
// ORDER BY 컬럼 DESC (Descending which means numbers decrease like 3, 2, 1)//
// 화면에 표시될 때는 top부분에 큰 숫자부터 아래로 내림차순정렬
