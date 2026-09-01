use my_edu_db;

create TABLE customers (
	id int auto_increment primary key,
    first_name varchar(100),
    last_name varchar(100),
    email varchar(100)
);

CREATE TABLE orders (
	id int auto_increment primary key,
    order_date date,
    amount decimal(8, 2),
    customer_id int,
    foreign key (customer_id) references customers(id)
);

SELECT * FROM orders;
SELECT * FROM customers;

-- dataframe에서 했던 merge와 같은 것이 sql에서는 join 이다
-- 공통되는 같은 컬럼으로 합치는게 가능하다

-- inner Join
-- Left join  (a 와 b가 있으면 a의 모든것과 b의 겹치는 부분을 select하고 겹치치않는 나머지 b는 버린다
-- Right join




