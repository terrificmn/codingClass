<?php
  include_once 'dbh.inc.php';  //DB접속 당당할 페이지
//**참고**/
// 경로는 signup.icn.php파일이 로드된 곳이 현재 디렉토리이다
// 원래는 23_index_dbinsert.php 에서 form 액션을 includes/signup.inc.php파일로 지정했는데
// 그러면 현재 페이지 signup.inc.php 기준으로 같은 디렉토리에 있는 dbh.inc.php를 포함하는 것
// 그래서 경로는 그냥 현재경로

//$sql = "INSERT INTO users (user_first, user_last, user_email, user_uid, user_pwd) VALUES ('Daniel', 'Nielsen', 'usermmeu@gmail.com', 'Admins', 'test1234');";
//위의 방식대로 들어가지지만 form에서 post 방식으로 가져온 것을 처리해야하기 때문에 변수를 만들어 사용
//super glbal을 이용

$first = mysqli_real_escape_string($conn, $_POST['first']);
// mysqli_real_escape_string() 함수는 코드로 입력된것을 스트링으로 바꾸는 함수
// 1st parameter: db connection, 2nd parameter: value(from input box, etc)
// post변수로 받은것을 바로 사용하는 것은 데이터베이스를 망칠 수 있으므로 주의
// 이것보다 더 좋은 것은 prepare statement 방식이 있다고 함
$last = mysqli_real_escape_string($conn, $_POST['last']);
$email = mysqli_real_escape_string($conn, $_POST['email']);
$uid = mysqli_real_escape_string($conn, $_POST['uid']);
$pwd = mysqli_real_escape_string($conn, $_POST['pwd']);
// e.g. input box에 Values ('user_name'); 라고 넣는다면
// Values (\'user_name\'); 이런식으로 바뀌게 된다
// 이렇게 해서 db에서 에러를 미리 잡을 수 있다 (protect database)
// 하지만 prepare statement를 사용하면 더 편하게 사용할 수 있다

// *** 중요: now we have sql injection using mysqli with prepare statement //
//자세한 주석은 25_Expain_PrepareSTMT.php 참고할 것!!!!!

//Created a template
$sql = "INSERT INTO users (user_first, user_last, user_email, user_uid, user_pwd) VALUES (?, ?, ?, ?, ?);";
//Create a prepared statement
$stmt = mysqli_stmt_init($conn);
//Prepare the prepared statement
if (!mysqli_stmt_prepare($stmt, $sql)) {
  echo "SQL error";
} else {
  //Bind parameters to the placeholder
  mysqli_stmt_bind_param($stmt, "sssss", $first, $last, $email, $uid, $pwd);
  // 5개의 컬럼 값을 확인하는 것이기때문에 s 5개, 그리고 폼에서 입력받은 5개 데이터
    
  //Run parameters inside database
  mysqli_stmt_execute($stmt);
}


header("Location: ../23_index_dbinsert.php?signup=success"); //페이지변경해주는 함수
?>
