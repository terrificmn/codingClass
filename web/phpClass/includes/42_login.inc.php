<?php
if (isset($_POST['login-submit'])) {
  require '42_dbh.inc.php';
  
  $mailuid = $_POST['mailuid'];
  $password = $_POST['pwd'];
  
  if (empty($mailuid) || empty($password)) { //입력이 없다면 에러
    header("Location: ../42_loginsystem.php?error=emptyfields");
    exit();
  } else {
    $sql = "SELECT * FROM loginUsers WHERE uidUsers=? OR emailUsers=?;";  
    //uidUsers컬럼 OR emailUsers컬럼 중에 사용하고 싶은것으로 할 수있게 하기 위해서 or로 검색
    //메일주소로 검색하게 됨 (아이디를 메일로 사용할 수도 있기 때문)
    $stmt = mysqli_stmt_init($conn);
    if (!mysqli_stmt_prepare($stmt, $sql)) { //db오류 있는지 체크
      header("Location: ../42_loginsystem.php?error=sqlerror");
      exit();

    } else {
      mysqli_stmt_bind_param($stmt, "ss", $mailuid, $mailuid); //유저네임이나 메일에서 입력한 메일로 사용하는 지 체크하기 위해서
      mysqli_stmt_execute($stmt); //query실행
      $result = mysqli_stmt_get_result($stmt); //** 중요: db에서 data르 받아오지만 raw데이터로 받아와서 밑의 배열로 다시 받아줘야 함
      if ($row = mysqli_fetch_assoc($result)) {
        $pwdCheck = password_verify($password, $row['pwdUsers']); 
        //password_verify()fn.은 입력받은 패스워드와 db에서 associative배열로 받아온 데이터를 비교해주는 함수 true/false를 리턴
        if ($pwdCheck == false) { // pwd체크
          header("Location: ../42_loginsystem.php?error=wrongpwd");
          exit();
        } else if ($pwdCheck == true) { 
          /*중요: 위의 if문의 ($pwdCheck == false) 조건이 boolean이기 때문에 false 아니면 true 이지만  
          그래서 else조건으로 해도 되지만 else if에 다시 조건을 ($pwdCheck == true)로 한 이유는 혹시 모를 에러를 방지하기 위해서
          혹시라도 boolean이 아닌 string으로 리턴 받았을 때 false가 아니라는 이유만으로 실행되는것을 방지하기 위함
          즉, false만 아니면 다OK를 방지 
          */
          session_start(); //비번이 맞다면 $_SESSION(super global을 사용할 수 있게 session스타트해줌
          /*중요: 세션 변수를 사용하려면 모든 페이지에서 session_start()함수가 호출되어야 한다 
          그래서 모든 페이지에 (헤더로 따로 include/require 해주는게 좋음) 세션스타트 코드를 넣어준다 */
          
          $_SESSION['userId'] = $row['idUsers'];
          $_SESSION['userUid'] = $row['uidUsers'];
          header("Location: ../42_loginsystem.php?login=success");
          exit();

        } else {
          header("Location: ../42_loginsystem.php?error=wrongpwd");
          exit();
        }

      } else {
        header("Location: ../42_loginsystem.php?error=nouser");
        exit();
      }

    }


  }




} else {
  header("Location: ../42_loginsystem.php");
}