-- 중복 처리할 수 있는 unique id 부여

CREATE TABLE cats3 (
	cat_id int NOT NULL PRIMARY KEY, -- primary key 데이터를 구분할 수 있는 unique 한 키 -- auto_increment
    name varchar(100) NOT NULL,
    age int
    -- primary key (cat_id) == 같은표현
);

INSERT INTO cats3 (cat_id, name, age) VALUES( 2, '고양스', 11);

-- 위의 문제점은 cat_id 를 확인해서 없는 int형태로 값을 insert 해야 들어가짐

-- 결론부터 말하면 auto_increment 를 사용해서 자동으로 생성하게 할 수 있다

CREATE TABLE cats4 (
	cat_id int NOT NULL PRIMARY KEY auto_increment , 
    name varchar(100),
    age int
);

INSERT INTO cats4 (name, age) VALUES( '너구리', 3);


-- not null 사용 예
CREATE TABLE employees (
	id int NOT NULL PRIMARY KEY auto_increment,
    last_name varchar(255) NOT NULL,
    first_name varchar(255) NOT NULL,
    middle_name varchar(255),
    age int NOT NULL,
    current_status varchar(255) NOT NULL default 'employed'
);

INSERT INTO employees (last_name, first_name, age) -- middel_name 은 null 허용이므로 안써도 됨
	VALUES (
			'Mike', 'Jordan', 22
	);
	
INSERT INTO employees (last_name, first_name, middle_name, age) -- middel_name 은 null 허용이므로 안써도 됨
	VALUES (
			'Mike', 'Jordan', 'middle', 22
	);

INSERT INTO employees (last_name, first_name, middle_name, age, current_status) 
	VALUES (
			'Mike', 'Jordan', 'middle', 22, 'hello'
	);

INSERT INTO employees (last_name, first_name, middle_name, age, current_status) 
	VALUES (
			'Mike', 'Jordan', NULL, 22, NULL
	);   -- NULL 허용안함이므로 NULL이 들어가면 sql가 실행되지 못함

-- NULL 값이 입력값으로 들어오면 쿼리가 실행되지 못함에 유의!




