<?php
//참고: 파일명 dbh which stands for database handler
//참고: dbh.inc 파일명에 inc가 들어가는 이유는 include했다고 알아보기 편하게 네이밍 tip

$dbServername = "localhost"; //local에서 서버를 테스트 하고 있으므로..
$dbUsername = "root"; // 현재 mariadb 에서 root 유저만 만들어 놓음
$dbPassword = "superocta"; // sql root계정 비번 : 새로운 계정을 만드는것도 나쁘지 않을 듯
//$dbName = "loginsystem"; // 로그인 관련 연습은 loginsystem database로 연결
$dbName = "phplessons"; //array 강좌에서는 phplessons database로 연결

$conn = mysqli_connect($dbServername, $dbUsername, $dbPassword, $dbName);
// mysqli_connect의 파라미터 순서가 서버네임, 유저네임, 패스워드, 디비네임
// $conn변수는 connection


?>