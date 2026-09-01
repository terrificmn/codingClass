<?php
//session_start(); // session_start()함수를 호출하면 세션 super global 로 생성된 것을 기억해서 
// 사용할 수 있게 된다
// 세션_스타트()함수는 매 페이지에서 계속 있어야지만 세션을 활용할 수 있으므로
// <head> 부분을 include해서 사용할 수 있게 만들면 쉽게 가능할 수 있음

?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <ul>
    <il><a href="index.php">HOME</a></il>
    <il><a href="session_contact.php">CONTACT</a></il>
  </ul>
  
<?php
//$_SESSION['username'] = 'dani948b';   //for example, let's say there's username: dani948a

echo $_SESSION['username'];

// 로그인이 작동하는 간단한 예
if (!isset($_SESSION['username'])) { // isset()함수는 NULL이 아니고 변수가 정의되었는지 보는 함수
  // true, false return
  echo "You are not logged in!";
  } else {  //위에서 session_start() 와 $_SESSION을 안했다면 로그인이 안됨
  echo "You are logged in!";  
}


?>

</body>
</html>