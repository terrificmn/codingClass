INSERT INTO cats ( name, age ) VALUES ('홍길동', 10);

INSERT INTO cats ( name, age) VALUES ('Jetson', 7);

INSERT INTO cats ( age, name) VALUES (12, 'Victory');

-- Multiple Insert
INSERT INTO cats (name, age)
	VALUES ('Charlie', 10),  -- values()에 여러번 입력해주면 됨
			('Sadie', 3),
            ('Lazy Bear', 1);
            
CREATE TABLE people (
	first_name varchar(20),
    last_name varchar(20),
    age int
);

INSERT INTO people (first_name, last_name, age) VALUES('Tina', 'Belcher', 13),
	('Bob', 'Belcher', 42);
    

-- NULL
INSERT INTO cats (name) VALUEs ('Alabama');
INSERT INTO cats () VALUEs ();  -- null 이 들어가짐

CREATE TABLE cats2 (
	name varchar(100) NOT NULL,
    age int NOT NULL
);

INSERT INTO cats2 (name) VALUES ('Alabama');
INSERT INTO cats2 () VALUES ();

INSERT INTO cats () VALUES ();  




