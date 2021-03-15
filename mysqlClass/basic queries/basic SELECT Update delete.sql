USE my_edu_db;
CREATE TABLE cat (
	cat_id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name varchar(32),
    breed varchar(32),
    age int
);

INSERT INTO cat (name, breed, age) 
		VALUES ('Ringo', 'Tabby', 4),
				('Cindy', 'Maine Coon', 10),
                ('Dumb', 'Maine Coon', 11),
                ('Egg', 'Persian', 4),
                ('Misty', 'Tabby', 13),
                ('George Michael', 'Ragdoll', 9),
                ('Jackson', 'Sphynx', 7);
        
SELECT * FROM cat;
SELECT name, age FROM cat;
SELECT age, name FROM cat;
SELECT NAME FROM cat;

SELECT * FROM cat WHERE age = 4;

-- 나이가 4살인 고양이의 이름과 종만 가져오세요
SELECT name, breed FROM cat WHERE age = 4;

-- 나이는 4살이고 종은 Persian 인 고양이의 데이터를 가져오세요
SELECT * FROM cat   -- 실무에서는 WHERE 이하를 구분하기 위해서 내려서 작성한다고 함
WHERE age = 4 AND breed = 'Persian';

SELECT * FROM cat 
WHERE age = 4 OR age >= 10;


SELECT * FROM cat;

-- 고양이의 종이 Tabby인 고양이들을 찾아서 그 고양이들의 종을 Shorthair 로 바꾸시오

UPDATE cat SET breed ='Shorthair'
WHERE breed = 'Tabby';

SELECT * FROM cat;

-- 이름이 Jaackson 인 고양이의 데이터를 가져오세요
SELECT * FROM cat WHERE name = 'Jackson';

-- 이름이 Jackson 인 고양이의 이름을 Jack으로 바꾸세요
UPDATE cat SET name = 'Jack' 
	WHERE name = 'Jackson';

SELECT * FROM cat WHERE name = 'Jack';

-- 이름이 Ringo 인 고양이의 종을 British로 바꾸세요
UPDATE cat SET breed = 'British' WHERE name = 'Ringo';
SELECT * FROM cat WHERE name = 'Ringo';

-- 종이 Maine Coon 인 고양이의 나이를 12로 바꾸세요
UPDATE cat SET age = 12 WHERE breed = 'Maine Coon';
SELECT * FROM cat WHERE breed = 'Maine Coon';


--- DELETE 하기
DELETE FROM cat WHERE age = 12;  -- WHERE 조건으로 검색 후에 삭제하는것 중요

SELECT * FROM cat; -- 컬럼의 데이터를 다 삭제

SELECT * FROM cat;