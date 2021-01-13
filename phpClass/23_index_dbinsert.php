<!DOCTYPE html>
<html>
<head>
  <title>사용자 sign-up sql insert</title>
</head>
<body>
<h1>sql insert</h1>
<form action="includes/signup.inc.php" method="POST"> 
  <input type="text" name="first" placeholder="Firstname"><br>
  <input type="text" name="last" placeholder="Lastname"><br>
  <input type="text" name="email" placeholder="E-mail"><br>
  <input type="text" name="uid" placeholder="Username"><br>
  <input type="text" name="pwd" placeholder="Password"><br>
  <button type="submit" name="submit">회원가입</button>
</form>            

<?php
  //$sql = "INSERT INTO users (user_first, user_last, user_email, user_uid, user_pwd) VALUES ('Daniel', 'Nielsen', 'usermmeu@gmail.com', 'Admins', 'test1234');";
  //INSERT query <html에서 <foam액션에서 inser쿼리 부분을 담당할 페이지로 보내지게 된다

  /* 
  *** PDO 방식이 아닌 mysqli를 사용하는 이유***
  In PHP there exists two methods of programming, which are
  "Procedural programming (PP)" and "Object oriented programming (OOP)". 
  In this PHP course we are using PP, and not OOP.
  
  When using PP, it is possible to use MySQLi and Prepared statements. 
  And when using OOP it is possible to use MySQLi, Prepared statements, and PDO. 
  Therefore we cannot use PDO in these lessons here.
  
  HOWEVER, in a few episodes 
  I will show how to get and insert data into a database using prepared statements
*/

?>
<body>
</html>
