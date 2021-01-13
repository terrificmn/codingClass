<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Error Handlers</title>
</head>
<body>
  <h1> Sign up- Error handler </h1>
  <form action="includes/signup_error.inc.php" method="POST"> 
  <?php
    if (isset($_GET['first'])) {  //슈퍼글로벌 get으로 first 받아왔다면 value값을 준다
      $first = $_GET['first'];
      echo '<input type="text" name="first" placeholder="Firstname" value="'. $first .'"><br>';
    }
    else {  //받아온것이 없다면 원래 empty input을 보여준다
      echo '<input type="text" name="first" placeholder="Firstname"><br>';
    }

    if (isset($_GET['last'])) {  //슈퍼글로벌 get으로 last 받아왔다면 value값을 준다
      $last = $_GET['last'];
      echo '<input type="text" name="last" placeholder="Lastname" value="'. $last .'"><br>';
    }
    else {  //받아온것이 없다면 원래 empty input (이름 입력창)을 보여준다
      echo '<input type="text" name="last" placeholder="Lastname"><br>';
    }
?>
    <input type="text" name="email" placeholder="E-mail"><br>

<?php
    if (isset($_GET['uid'])) {  //슈퍼글로벌 get으로 uid 받아왔다면 value값을 준다
      $uid = $_GET['uid'];
      echo '<input type="text" name="uid" placeholder="Username" value="'. $uid .'"><br>';
    }
    else {  //받아온것이 없다면 원래 empty input(유저네임 입력창)을 보여준다
      echo '<input type="text" name="uid" placeholder="Username"><br>';
    }
?>
    <input type="text" name="pwd" placeholder="Password"><br><br>    
    <button type="submit" name="submit">Sign up</button>
  </form>
  
  <?php
    
  
  /*
//에러메세지 표시하는 첫번째 방법
//이 방식은 유저한테는 조금 불편한 방식 - why? 에러가 있다면 input에 입력한 내용이 다 지워지므로
  $fullUrl = "http://$_SERVER[HTTP_HOST]$_SERVER[REQUEST_URI]"; //super global $_SERVER
  
  if (strpos($fullUrl, "signup=empty") == true) {  //strpos()이용해서 get방식으로 받은 것이 signup=empty 비교
    echo "<p>You did not fill in all fields!<p>";
    exit(); //조건에 맞으면 조건문 빠져나가게 한다 // 불필요한 다음 코드를 실행방지 목적
  } elseif (strpos($fullUrl, "signup=char") == true) { 
    echo "<p>You uesd invalid characters!<p>";
    exit();
  } elseif (strpos($fullUrl, "signup=invalidemail") == true) { 
    echo "<p>You  used an invalid e-mail!<p>";
    exit();
  } elseif (strpos($fullUrl, "signup=success") == true) { 
    echo "<p>You have been signed up!<p>";
    exit();
  }
*/

// 2번째 방식 get 슈퍼글로벌 변수로 데이터 받아오기. 
// 콤보로 위에 input창을 if문으로 로직을 짜면 훨씬 유저한테 좋은 방식이 될 수 있다. 
// 변수로 할당해서 value로 받은 값을 input태그의 value값에 다시 넣어주는 방식 --굿!
if (!isset($_GET['signup'])) {
  exit();
} else {
  $signupCheck = $_GET['signup']; //$_GET super global : 주소 뒤에 붙은 데이터를 이용해서 비교
  
  if ($signupCheck == "empty") {
    echo "<p>You did not fill in all fields!<p>";
    exit(); //조건에 맞으면 조건문 빠져나가게 한다 // 불필요한 다음 코드를 실행방지 목적
    } 
      elseif ($signupCheck == "char") {
        echo "<p>You uesd invalid characters!<p>";
        exit();
      }   
      elseif ($signupCheck == "invalidemail") { // 이부분관련해서 액션페이지 signup_error.inc.php에서 
        echo "<p>You  used an invalid e-mail!<p>"; //get방식으로 데이터를 더 넘겨준다(first,last,uid)
        exit();
      } 
      elseif ($signupCheck == "success") {
        echo "<p>You have been signed up!<p>";
        exit();
      }
  }



  ?>
</body>
</html>