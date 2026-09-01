
UPDATE posts
SET subject='This is a test', content='This is the content.'
WHERE id='1';

//uppercase or lowercase doens't matter but it's nice to write in the uppercase letter.
// SET 이후에는 바꾸고 싶은 컬럼을 바꿔주면 된다
//***중요****
//WHERE 조건으로 특정을 안해주면 모든 컬럼을 바꿔버리게 된다.


DELETE FROM posts
WHERE id='1';
// posts 테이블
//***중요***
// WHERE 조건에 맞는 것만 지울 수 있게 하자
