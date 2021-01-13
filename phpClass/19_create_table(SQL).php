<?php
echo "Hello World";

//*** sql query --php 아님 주의 */
//phpmyadmin 에서 만들거나
//mysql -u root -p 으로 로그인해서 직접 만들거나 할 수 있다

create database phplessons;
// phplessons은 databasename

create table posts (
	id int(11) not null PRIMARY KEY AUTO_INCREMENT,
// integer(11bite? 설명 찾아봐야함)
// not null 허용안함
// primary key 지정해서 같은 값을 못갖게 한다 (좀더 설명을 찾아봐야할 듯..)
// 자동으로 1씩 카운트

	subject varchar(128) not null,
// varchar(128자 까지 허용)

	content varchar(1000) not null,
// **참고: varchar 대신에 text 가능
// or you can set it to TEXT instead of varchar() if you want to get rid of the character limit
// the difference is that text saves the data as binary instead of text

  date datetime not null
// datetime 은 () 필요없음
// year 부터 ms(밀리세컨드)까지 에: 2020-11-12 12:10:05
);

?>
