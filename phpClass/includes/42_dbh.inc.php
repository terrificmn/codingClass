<?php

$servername = "localhost";
$dbUsername = "root";
$dbPassword = "superocta";
$dbName = "phplessons";

$conn = mysqli_connect($servername, $dbUsername, $dbPassword, $dbName);

if (!$conn) {
  die ("Connection failed: ".mysqli_connect_error()); //db접속이 안되면 die()를 작동시키면서 
  //mysqli_connect_error()로 에러메세지 나오게함
  //예: 비번을 잘못 입력했을 때는 아래처럼 나온다
  //Connection failed: Access denied for user 'root'@'localhost' (using password: YES)

}
