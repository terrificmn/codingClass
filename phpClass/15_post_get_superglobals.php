<?php
/* super global
$GLOBALS
$_POST
$_GET
$_COOKIE
$_SESSION
*/

//echo $_GET['name']; //super global // form에서 get 방식을 받을 때 사용
echo $_POST['name'];  //super global // input box의 name을 쓴다

// form에서 post방식으로 넘겨주면 원래 화면에 보여지지 않지만
// super global 을 이용하면 포스트 방식으로 넘어온것도 사용할 수 있다 (출력)
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <form method="POST"> 
  <!-- GET: url에서 정보가 보이는 것 | POST는 안보임 -->
    <input type="hidden" name="name" value="mike">
    <button type="submit">PRESS ME!</button>
  </form>
</body>
</html>