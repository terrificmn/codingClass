-- DB 권한 / 유저 생성해서 특정DB만 다룰 수 있게 권한을 주기 

-- 'streamlit'@'%' 이 유저가 되고, streamlit  ,   뒤에가 비번이 된다
CREATE USER 'streamlit'@'%' identified by 'yh123456789';

# my_edu_db 데이터베이스의 테이블을 사용할 수 있는 모든 (all) 권한을 줌 to 'streamlit'유저에게
grant all on my_edu_db.* to 'streamlit'@'%';