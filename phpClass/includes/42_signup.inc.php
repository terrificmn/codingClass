<?php
/* *** DB를 테이블 만들 때에 참고할 것은 
idUsers는 int(11)
uidUsers, emailUsers는 TINYTEXT
pwdUsers는 LONGTEXT로 만든다 (사용자가 비번을 길게 조합해서 만들 수 있게 해준다)
*/

if (isset($_POST['signup-submit'])) { //URL이나 부정적인 방법으로 현재 페이지에 접근하는 것을 방지하기 위해서 
  // 버튼이 물리적으로 클릭되어서 현재 페이지가 로드가 되었는지 확인하는 부분, url로 직접 접근하면 에러 핸드러 작동하게 만들어야함
  require '42_dbh.inc.php';

  $username = $_POST['uid'];
  $email = $_POST['mail'];
  $password = $_POST['pwd'];
  $passwordRepeat = $_POST['pwd-repeat'];

  if (empty($username) || empty($email) || empty($password) | empty($passwordRepeat)) {
    header ("Location: ../42_signup.php?error=emptyfields&uid=".$username."&mail=".$email);
    // 입력 안된 상태라면 페이지 이동시키면서 데이터를 넘겨준다. 사용자가 다시 입력하는 번거로움이 없게하기 위해서
    // **중요: 패스워드는 보이게하면 안되기 때문에 url에 넘기지 않는다
    exit(); // 빈칸 입력이라면 아래 코드를 실행하면 안되기에 실행 안되게 exit해준다
  
  //email && username check
  } else if (!filter_var($email, FILTER_VALIDATE_EMAIL) && !preg_match('/^[a-zA-Z0-9]*$/', $username)) { // validate email and username
    header ("Location: ../42_signup.php?error=invalidmailuid");
    // username과 email이 틀렸을 경우에는 url로 정보를 보내지는 않는다 
    exit();
  }
    
    //이메일 체크
    else if (!filter_var($email, FILTER_VALIDATE_EMAIL)) { //filter_var()의 1번째 파라미터는 검사할 스트링, 2번째 파라미터는 이메일 체크 
    //*** 참고로 2번째 파라미터는 미리 정해진 것들 몇개 있어서 상황에 맞게 쓰면 됨-굉장히 많음 
    header ("Location: ../42_signup.php?error=invalidmail&uid=".$username);
    //email 주소가 틀렸다면 email 정보는 url로 넘기지 않는다
    exit();

  } // 유저아이디 허용되는 문자열 체크
    else if (!preg_match('/^[a-zA-Z0-9]*$/', $username)) {  //regular expression으로 필요한 것들만 걸러낸다 (**자세한 공부가 필요함)
      /**참고: 헤깔려서 ㅋㅋ regular expression 에서 ^는 검색의 의미이므로 영문 숫자가 나오면 true를 반환 true이므로 if문을 실행할 것 같지만
      if에 !으로 해놓았으니 false에서 실행하라는 의미니깐 실행을 안함
      즉 영문 숫자는 에러코드를 발생시키지 않고, 한글을 쓰면 preg_match가 false가 되고 if실행이 !로 false에 실행되므로 에러코드 실행됨 */
    header ("Location: ../42_signup.php?error=invaliduid&mail=".$email);
    exit();
    
  }

  else if ($password !== $passwordRepeat) { //패스워드 맞게 입력했는지 검사
    header("Location: ../42_signup.php?error=passwordcheck&uid=".$username."&mail=".$email);
    exit();
  }

  else {
    //*db에서 uid 중복검사

    $sql = "SELECT uidUsers FROM loginUsers WHERE uidUsers=?;"; //?는 placeholder의 역활: 더 있다면 갯수 추가하면 됨, 's'이렇게 쓰면 안됨
    /*sql prepare statement를 사용하는데.. 
    사용자가 고의적으로 db를 망가뜨리려고 할 수 있는데 inputbox에 직접 sql query를 넣는다면 db가 망가질 수 있다고 함
    그래서 prepare statement가 좀 더 안전한 방법이라고 함
    */
    $stmt = mysqli_stmt_init($conn);
    if (!mysqli_stmt_prepare($stmt, $sql)) { //***증요: 에러부터 다루는게 논리적으로 훨씬 좋다
      header("Location: ../42_signup.php?error=sqlerror");
      exit();
    }
    else {
      mysqli_stmt_bind_param($stmt, "s", $username); //sql query에서 ? 사용한 만큼 s사용
      // sting = s, integer = i, boob = b,double = d
      mysqli_stmt_execute($stmt); //db로 실행시킴
      mysqli_stmt_store_result($stmt); //db에서 가져온 데이터를 store시킨다 (transfer) (가져온다)
      $resultCheck = mysqli_stmt_num_rows($stmt); //같은 유저가 있으면 1, 없으면 0
      if ($resultCheck > 0) { //0 이상이면 이미 같은 유저아디가 있다는 에러핸들링 해줌
        header("Location: ../42_signup.php?error=usertaken&mail=".$email);
        exit();
      }
      else { //신규 데이터이면 db에 입력할 준비함 
        $sql = "INSERT INTO loginUsers (uidUsers, emailUsers, pwdUsers) VALUE (?, ?, ?);";
        $stmt = mysqli_stmt_init($conn);
        if (!mysqli_stmt_prepare($stmt, $sql)) { 
          header("Location: ../42_signup.php?error=sqlerror");
          exit();
        }
        else {
          //mysqli_stmt_bind_param($stmt, "sss", $username, $email, $password); 
          //*** 중요: 사용자한테 받은 패스워드를 그대로 db에 입력해주면 해커 또는 악의적인 사용자가 어떤방법으로든 알아낼 수 없게 하기 위해서
          //$password를 해싱 해줘야 한다
          $hashedPwd = password_hash($password, PASSWORD_DEFAULT); 
          // ***중요: PASSWORD_DEFAULT는 BCRYPT로 보안성이 좋다, 하지만 md5, sha256 등의 방법은 outdated 보안에 취약할 수 있다
          mysqli_stmt_bind_param($stmt, "sss", $username, $email, $hashedPwd); //암호화된 password를 넣어준다 그리고 placeholder만큼 s를 써준다
          mysqli_stmt_execute($stmt); //insert query db에 실행
          mysqli_stmt_store_result($stmt);
          header("Location: ../42_signup.php?signup=success");
          exit();
        }
      
      
      }
    
    }



  }
  mysqli_stmt_close($stmt); //**중요: db연결을 닫아 주는것이 리소스면에서 좋다
  mysqli_close($conn);
}
else {
  header("Location: ../42_signup.php");
  
}


//***중요: Pure php code일 떄는 클로징 태그를 닫지 않는다
//php코드 다음에 html등을 넣을 때는 php클로징 태그를 한다 (닫는다)
