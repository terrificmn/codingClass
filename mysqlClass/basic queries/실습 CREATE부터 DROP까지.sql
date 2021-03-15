CREATE DATABASE shirts_db;

USE shirts_db;

CREATE TABLE shirts (
	shirt_id int NOT NULL PRIMARY KEY auto_increment,
    article varchar(20),
    color varchar(10),
    shirt_size varchar(3),
    last_worn int
);

DESC shirts;

SELECT * FROM shirts;

SELECT article, color FROM shirts;

-- 팁: sql이 길어질 수록 줄바꿈을 해서 하는 것이 보기 쉽다
SELECT article, color, shirt_size, last_worn 
FROM shirts
WHERE shirt_size = 'M';

-- update shirt_size to 'L' which article is polo shirt
UPDATE shirts SET shirt_size = 'L' 
WHERE article = 'polo shirt';

SELECT * FROM shirts 
WHERE article = 'polo shirt';

UPDATE shirts SET last_worn = 0 
WHERE last_worn = 15;

SELECT * FROM shirts WHERE last_worn = 0;

SELECT * FROM shirts WHERE color = 'White';

UPDATE shirts SET shirt_size = 'XS', color = 'off white' 
WHERE color = 'White shirts';

DELETE FROM shirts WHERE last_worn >= 200;
SELECT * FROM shirts WHERE last_worn >= 199;

DELETE FROM shirts WHERE article = 'tank top';
SELECT * FROM shirts  WHERE article = 'tank top';

DELETE FROM shirts;
SELECT * FROM shirts;

-- 모든 파일을 지운 후에 csv 파일로 불러오기 
-- 단 먼저 Export to csv 를 해야함 ( SELECT * FROM shirts; 를 하면 결과 창에서 할 수 있음)

-- 반대로 불러오기는 Import (마찬가지로 selete문 한번 실행 한 후 (mysql workbench 기준) import 아이콘 선택)
-- 파일 지정 한 후 기존의 table에다가 불러오기 진행하면 됨


DROP TABLE shirts;
