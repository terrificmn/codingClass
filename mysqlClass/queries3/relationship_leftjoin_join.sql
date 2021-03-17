CREATE TABLE reviewers (
	id int primary key not null auto_increment,
    first_name varchar(20),
    last_name varchar(20) 
);


CREATE TABLE series (
	id int primary key not null	auto_increment,
    title varchar(100),
    released_year year(4),
    genre varchar(50)
);



CREATE TABLE reviews (
	id int primary key not null auto_increment,
    rating int,
	series_id int,
    reviewer_id int,
    foreign key(series_id) references series(id),
    foreign key(reviewer_id) references reviewers(id)
);

DESC series;

SELECT * FROM series;
SELECT * FROM reviews;
SELECT * FROM reviewers;

SELECT s.title
FROM series s
JOIN reviews rv
	on s.id = rv.reviewer_id;
    

SELECT s.title, avg(rv.rating) as avg_rating
FROM series s
JOIN reviews rv
	on s.id = rv.reviewer_id
GROUP by s.title
ORDER by avg_rating asc;

SELECT * FROM reviews;


SELECT rver.first_name, rver.last_name, rv.rating
FROM reviewers rver
JOIN reviews rv
	on rver.id = rv.reviewer_id
GROUP by rver.first_name
ORDER by rv.rating DESC;


-- WHERE 할 때  =null 이 아니라 is null 로 해야한다 
-- 아닐때는 not null
SELECT *
FROM series s
LEFT JOIN reviews rv
	on s.id = rv.series_id
WHERE rv.rating is null;  

-- round(float_type컬럼, 몇자리)
SELECT series.genre, round(avg(reviews.rating),1) as avg_rating
FROM series
JOIN reviews
	on reviews.series_id = series.id
GROUP by series.genre
ORDER by avg_rating DESC;



SELeCt * 
FROM reviews;

SELECT rver.first_name, rver.last_name,
	rv.rating, count(rv.rating) as count, 
    min(rv.rating) as min, max(rv.rating) as max
	-- ifnull(round(rv.rating, 1),0) 
FROM reviewers rver
LEFT JOIN reviews rv
	on rv.reviewer_id = rver.id
WHERE rv.rating is not null
GROUP by rver.id;



-- 3개 join 하기, 물고 물리는 것 같지만  reviews에는  reviewer_id 와 series_id가 있어서 (공통)
-- 서로 join이 된다 
SELECT s.title, round(rv.rating,1), 
	concat(rver.first_name, ' ', rver.last_name)
FROM series s
JOIN reviews rv
	on s.id = rv.series_id
JOIN reviewers rver
	on rv.reviewer_id = rver.id
ORDER by s.title;



    
    
    
    
    
    
    
    
    
    