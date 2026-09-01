<?php
session_start();
include_once 'includes/dbh.inc.php' //db connection

  /* 사진 프로파일 업로드에 필요한 2개의 데이터베이스가 필요하다
    1.첫번째 user테이블 컬럼은 id, first, last, username, password필요
    id는 int(11) not null PRIMARY KEY AUTO_INCREMENT
    나머지는 varchar(256)으로 만들면 됨
    
    2. 두번째 profileimg테이블
    CREATE TABLE profileimg (
      id int(11) not null PRIMARY KEY AUTO_INCREMENT,
      userid int(11) not null,
      status int(11) not null
    );
  */
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

  $sql = "SELECT * FROM user";
  $result = mysqli_query($conn, $sql);
  if (mysqli_num_rows($result) > 0) {
    while ($row = mysqli_fetch_assoc($result)) {
      $id = $row['id']; //profileimg 테이블에 있는 아이디와 비교하기 위해서 
      $sqlImg = "SELECT * FROM profileimg WHERE userid='$id'"; //새로운 쿼리를 만들고 id로 검색해서 받아온다
      $resultImg = mysqli_query($conn, $sqlImg);  //결과는 새로운 변수 resultImg에 넣어준다
      while ($rowImg = mysqli_fetch_assoc($resultImg)) { //profile이미지가 있는지 확인하여 있다면 loop문 진행
        echo "<div>";
          if ($rowImg['status'] == 0) { //사진이 있는것은 0으로 약속
            //echo "<img src='uploads/profile".$id.".jpg'>"; //프로파일 이미지가 있으면 사진을 띄워준다
            //위의 코드는 만약 사진을 업데이트하면 새로고침 하기전에는 그 업데이트 전 파일을 계속 보여준다

            $filename = "uploads/profile".$id."*"; //사진 아이디 가 같은 것은 (*)다 검색
            $fileinfo = glob($filename); //패턴에 맞는 예로 * 같은거를 찾아주는 함수 // 확장자를 특정안해도 찾을 수 있다
            $fileext = explode(".", $fileinfo[0]);  //glob()로 찾은 $fileinfo 에는 배열로 여러개가 들어가 있을 수 있기 때문에..첫번째만 사용
            $fileactualext = $fileext[1]; //확장자만 사용하기 위해서 새로 변수 할당
            
            echo "<img src='uploads/profile".$id.".".$fileactualext."?".mt_rand().">"; 
            //mt_rand() 무작위 숫자를 붙여준다
            //무작위 숫자를 붙이는 이유는: 만약 사진을 업데이트하면 브라우저는 파일이름이 같기 때문에 같은파일을 인식한다
            //새로고침을 몇번하면 해결되지만, 사진 업데이트 후 바로 바뀌게 할려면 무작위 숫자를 넣어줘서 
            //브라우저가 다른 파일명으로 인식하게 만드는 것
          } else { // 컬럼 status가 0이 아니면 기본 이미지를 띄워준다
            echo "<img src='uploads/profiledefault.png' width='150' height='150'>";
          }
          echo "<p>".$row['username']."</p>";
        echo "</div>";
      }
    } 
  } else { //db에서 뽑안온 것이 없다면 실행. 즉, db에 입력된 데이터가 없는 경우
    echo "There are no users yet. ";
  }


  if (isset($_SESSION['id'])) {
    if ($_SESSION['id'] == 1) {
      echo "You are logged in as user #1";
    }
    echo "<form action='34_login.php' method='POST' enctype='multipart/form-data'>
            <input type='file' name='file'>
            <button type='submit' name='submit'>UPLOAD</button>
          </form>";
    echo "<form action='34_delete.php' method='POST'>
          <button type='submit' name='submit'>DELETE profile image</button>
          </form>";      
  } else { //로그인 안한 경우
    echo "You are not logged in";
    echo "<form action='34_signup.php' method='POST'>
            <input type='text' name='first' placeholder='First name'>
            <input type='text' name='last' placeholder='Last name'>
            <input type='text' name='uid' placeholder='Username'>
            <input type='password' name='pwd' placeholder='Password'>
            <button type='submit' name='submitSignup'>SIGN UP</button>
          </form>";
  }

?>
  <p>Login as user!</p>
  <form action="34_login.php" method="POST">  
    <button type="submit" name="submitLogin">Login</button>
  </form>

  <p>Loginout as user!</p>
  <form action="34_logout.php" method="POST">  
    <button type="submit" name="submitLogout">Logout</button>
  </form>
</body>
</html>