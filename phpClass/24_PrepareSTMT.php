<!DOCTYPE html>
<html>
<head>
  <title>SQL PREPARE STATEMENT sign-up</title>
</head>
<body>

<form action="includes/24_signup.inc.prepare.php" method="POST"> 
  <input type="text" name="first" placeholder="Firstname"><br>
  <input type="text" name="last" placeholder="Lastname"><br>
  <input type="text" name="email" placeholder="E-mail"><br>
  <input type="text" name="uid" placeholder="Username"><br>
  <input type="text" name="pwd" placeholder="Password"><br>
  <button type="submit" name="submit">회원가입</button>
</form>            

<!-- Explaination of SQL injection using mysqli with the prepared statement 
***자세한 설명은 25번 강좌 확인 필수!!! (25_Explain_PrepareSTMT.php 파일 참고)
// When doing Procedural PHP programming, you should always use Prepared Statement 
// because it is safer.

-->
<?php
 // 실제 코드는 입력 form 넘어가는 includes/signup.inc.prepare.php 참고
?>
<body>
</html>
