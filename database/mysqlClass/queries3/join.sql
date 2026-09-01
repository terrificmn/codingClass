CREATE table students(
	id int auto_increment primary key,
    first_name varchar(100)
);

CREATE table papers (
	title varchar(100),
    grade int,
    student_id int,
    -- foreign key (설정)
    foreign key(student_id) references students(id) on delete cascade
    -- on delete cascade 는 참조한 students의 id가 지워지면 papers의 해당 row도 지워지게 하는 것임
);



INSERT INTO students (first_name) VALUES 
('Caleb'), ('Samantha'), ('Raj'), ('Carlos'), ('Lisa');

INSERT INTO papers (student_id, title, grade ) VALUES
(1, 'My First Book Report', 60),
(1, 'My Second Book Report', 75),
(2, 'Russian Lit Through The Ages', 94),
(2, 'De Montaigne and The Art of The Essay', 98),
(4, 'Borges and Magical Realism', 89);


SELECT * FROM students;
SELECT * FROM papers;


-- JOIN하기 
-- FROM 참조할테이블 JOIN foreign key가 있는 테이블
-- on 에는 참조하는 테이블 컬럼과 = foreign key 컬럼을 정해주는데 이때 꼭 테이블명을 적어준다
-- 그리고 select하는 부분에도 꼭 테이블명을 적어줘야 한다
SELECT students.first_name, papers.title, papers.grade
FROM students 
JOIN papers
	on students.id = papers.student_id;  -- 연결고리를 설정 
    
-- 테이블명을 별칭으로 활용할 수 있는데  FROM과 JOIN에 테이블명을 적을 때 한칸옆에 적어주면
-- ON 부분과 SELECT부분에서도 그 별칭을 사용할 수 있게 된다
SELECT s.first_name, p.title, p.grade
FROM students s
JOIN papers p
	on s.id = p.student_id  -- 연결고리를 설정 
ORDER by p.grade DESC;


-- left join
-- 말 그대로 왼쪽에 있는 테이블에 join하고 조인되는 오른쪽에 있는 b테이블에는 내용이 없다면 NULL로 채워짐
SELECT *
FROM students s
LEFT JOIN papers p
	on s.id = p.student_id;
    

-- NULL 값이 것을 특정한 값으로 바꾸기
SELECT s.first_name, ifnull(p.title, 'missing'), ifnull(p.grade, 0)
FROM students s
LEFT JOIN papers p
	on s.id = p.student_id;
    

--  학생별로 조인해서 grade의 평균값을 표시하라, (null 값이 있음)
SELECT s.first_name, ifnull(avg(p.grade), 0) as AVERAGE
FROM students s
left join papers p
	on s.id = p.student_id
GROUP by s.first_name
-- having 은 group by를 한 후에 가능하다
having average >= 85
ORDER by AVERAGE DESC;


SELECT s.first_name, ifnull(avg(p.grade), 0) as average, 
	case 
		when ifnull(avg(p.grade), 0) = 0 then  --  이 부분을 주의해야하는데 옆에 있는 (오른쪽에 있는 테이블의 컬럼을 가져왔을 때는 
			'fail'					-- as average로 했었더라도 테이블명을 다 적어줘야한다, 물론 다른곳에서는 사용할 수 있음
        else
			'passed'
	end as passing_status
FROM students s 
LEFT JOIN papers p
	ON s.id = p.student_id
GROUP by s.first_name
ORDER by average DESC;


