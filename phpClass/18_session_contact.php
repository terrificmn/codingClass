<?php
session_start();
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>

<?php
echo $_SESSION['username'];

// session_test.php 파일에서 세션을 super global 로 만들어서 
// session_contact.php 현재 페이지에서도 
// 생성된 세션을 이용해서 위처럼 'username'을 출력할 수 있다
// 단, 세션 스타트 함수를 처음에 호출해야지 사용이 가능하다. 사용안하면 에러 발생/ 
/* 실제 로그인 시스템에서 적용한다면..
    아이디를 데이터베이스에서 비교한 후 맞으면 세션을 부여하고
    그 세션을 로그인해야지만 볼 수 있는 페이지에서는 if등을 해서 맞으면
    페이지를 볼 수 있게 만들면 될 듯함

?>


</body>
</html>


