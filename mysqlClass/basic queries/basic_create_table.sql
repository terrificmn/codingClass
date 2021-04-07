-- CREATE TABLE cats (
-- 	name VARCHAR(100),
--     age INT
-- );

-- catsSELECT * FROM cats;

-- SHOW tables;

-- DESC cats;
-- SHOW columns from tweets; -- column 보기
 
-- CREATE TABLE pastries (
-- 	name varchar(50),
--     quantity int
-- );

<<<<<<< HEAD
-- SELECT * FROM pastries;
=======
-- SELECT * FROM pastries;


CREATE TABLE user (
	id int unsigned NOT NULL primary key auto_increment,
    username varchar(80) NOT NULL unique,
    email varchar(200) NOT NULL unique,
    password varchar(200), 
    is_active boolean,

    -- 시간 자동으로 입력하게 하기 type은 timestamp default 값으로 now()함수 사용
    created_at timestamp default now(),
    updated_at timestamp default now()
);
>>>>>>> 4b3b6209295bf350cf8e4e4ed1f0780a49a85eb9
