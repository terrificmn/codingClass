-- 데이터 인서트시 에러날때의 조건
SELECT * FROM students;
INSERT INTO students (first_name)
VALUE ('Mike');
-- id 6번으로 등록이 됨

SELECT * FROM papers;
INSERT INTO papers (title, grade, student_id)
VALUES ('The Worst Paper', 91, 7);
-- student_id를 7로 넣으려고 하니깐 student_id가 foreign key로 되어 있는데 참조하는 것이 
-- students의 id이기때문에 students id가 7이 없으니깐 에러가 발생하는 것임!
-- 잘못된 데이터가 인서트가 안되도록 방지할 수 있다 (foreign key가 있으면)


-- on delete cascade 란?
SELECT * FROM students;

DELETE FROM students
WHERE id = 1;

SELECT * FROM papers;

-- 테이블을 설계할 때 foreign key 부분에 on delete cascade를 설정했다면
-- 참조하고 있는 students 테이블의 해당 id가 삭제된다면은 
-- papers 테이블의 해당 row도 다 지워지게되는 것
-- 장점도 있지만, 모든 데이터가 지워지므로 배송정보, 상품구매등이 이력이 있는 테이블에는 사용을 안한다
-- 상황에 따라서 사용한다고 함
-- foreign key(student_id) references students(id) on delete cascade
    -- on delete cascade 는 참조한 students의 id가 지워지면 papers의 해당 row도 지워지게 하는 것임