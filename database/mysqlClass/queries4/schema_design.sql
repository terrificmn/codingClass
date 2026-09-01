CREATE TABLE users (
	id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username varchar(20) NOT NULL,
    email varchar(100),
    created_at timestamp default now() -- default를 옵션을 넣어서 바로 DB에 들어갈 수 있게 한다
    -- DB에 insert문이 실행되는 순간에 시간이 기본값으로 들어갈 수 있게 하는 것!
);

CREATE TABLE photos (
	id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    image_url varchar(200) NOT NULL,
    user_id int NOT NULL,
    created_at timestamp default now(),
    updated_at timestamp default now() on update now(),  
    foreign key (user_id) references users(id)
);


CREATE TABLE comments (
	id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    comment_text varchar(256) NOT NULL, -- 256글자까지 제한
    user_id int NOT NULL,
    photo_id int NOT NULL,
    created_at timestamp default now(),
    updated_at timestamp default now() on update now(),  
    -- 디폴트값으로 현재시간이 들어가게 하고, 여기서 중요한 것은 update 쿼리가 실행될 때에도 now()가 들어갈 수 있게 한다
	foreign key (user_id) references users(id),
    foreign key (photo_id) references photos(id)
);

-- 좋아요 버튼은 한사람이 한번만 누를 수 있음 
-- id auto_increment로 만들면 버튼을 누를때마다 계속 id가 생성된다
-- 계속 쌓이게 되면, 나중에 유저가 버튼을 취소하면 또 일일이 삭제 쿼리도 만들어야 한다
-- 이런 문제가 있어서, 2개의 foreign key조합으로 unique한 컬럼을 만든다
-- 이렇게 되면 1개 입력 ok, 더 이상 입력하려고하면 중복때문에 에러 발생하게 된다
CREATE TABLE likes (
	-- id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    
    -- id 로 Primary Key를 생성하지 말고 
    -- user_id 와 photo_id도 유일한 id이므로 이 두개를 이용해서 primary key키를 만든다
    user_id int NOT NULL,
    photo_id int NOT NULL,
    created_at timestamp default now(),
    primary key(user_id, photo_id),  -- !!! 중요!!
    foreign key (user_id) references users(id),
	foreign key (photo_id) references photos(id)
);


CREATE TABLE tags (
	id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    -- unique 으로 만들어주기
    tag_name varchar(100) unique,  -- unique를 넣어주면 중복없는 고유의 값이 된다 
    -- 왜냐하면 tag name도 한개만 존재해야해서 그렇다
    -- 근데 왜? primary key로 안하는 것은 숫자가 db에서 처리하는 훨씬 빠르기 때문이다!
    created_at timestamp default now()
);

-- like와 마찬가지로 한번만 하면 되게 때문에 follower와 followee를 두 개를 사용해서 unique하게 만들어 준다
CREATE TABLE follows (
    follower_id int NOT NULL,
    followee_id int NOT NULL,
    created_at timestamp default now(),
    primary key(follower_id, followee_id),
    foreign key (follower_id) references users(id),
    foreign key (followee_id) references users(id)
);

CREATE TABLE photo_tags (
	photo_id int NOT NULL,
    tag_id int NOT NULL,
    primary key(photo_id, tag_id),
    foreign key (photo_id) references photos(id),
    foreign key (tag_id) references tags(id)
);



-- --------------------------------

SELECT * FROM users;
-- 회원가입한지 가장 오래된 회원 5명을 찾으시오
SELECT * 
FROM users
ORDER by created_at ASC LIMIT 5;


-- 회원가입을 가장 많이 한 요일을 2개 알고 싶다. 어떤 요일과 어떤 요일일까?
SELECT dayname(max(created_at)) as 'the most day people joined', count(*) as count
FROM users
GROUP by dayofweek(created_at)
ORDER by 'the most day people joined' DESC limit 2;


-- 회원가입을하고나서, 사진을 한번도 올리지 않은 inactive 한 회원의 유저네임을 가져오시오
-- 판다스 데이터 프레임의 merge와 비슷하다 (merge도 on파라미터로 공통적인 컬럼을 묶는다)
SELECT users.username as 'inactive users'
FROM users
LEFT JOIN photos
	on photos.user_id = users.id
WHERE photos.id is null;


-- 가장 좋아요를 많이 받은 사진은 어떤 사진인지 찾아서, 그 사진 올린 사람의 이름과 
-- 좋아요 수를 조회하시오

SELECT users.username, 
count(*) as 'count'
FROM photos
JOIN likes
	on likes.photo_id = photos.id
JOIN users
	on users.id = photos.user_id
GROUP by photos.id
ORDER by 'count' DESC;


-- 이 서비스는, 한명의 유저당, 평균 몇개의 사진을 올리는가?
SELECT (SELECT count(*) FROM photos) / (SELECt count(*) FROM users)
as 'photos per user';


-- 가장 많이 나온 해시태그 5개를 찾아서, 그 해시태그의 이름과 갯수를 조회하시오
-- tags 와 photo_tags 테이블이 2개가 있음

SELECT tags.tag_name, count(tag_name) as count
FROM tags
JOIN photo_tags
	on photo_tags.tag_id = tags.id
GROUP by tags.tag_name
ORDER by count DESC LIMIT 5
;

DESC photo_tags;
SELECT * FROM tags;
