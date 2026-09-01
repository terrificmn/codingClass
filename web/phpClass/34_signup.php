<?php
include_once 'includes/dbh.inc.php';

$first = $_POST['first'];
$last = $_POST['last'];
$uid = $_POST['uid'];
$pwd = $_POST['pwd'];

$sql = "INSERT into user (first, last, username, password) 
VALUES ('$first', '$last', '$uid', '$pwd');";
mysqli_query($conn, $sql); //db에 insertation

$sql = "SELECT * FROM user WHERE username='$uid' AND first='$first';";
$result = mysqli_query($conn, $sql);  //사용자가 바로 전 사인업을 한 후 그 입력한 아이디와 이름으로 검색해옴

if (mysqli_num_rows($result) > 0) { //정상적으로 입력해서 sign-up했다면 데이터가 있음
  while ($row = mysqli_fetch_assoc($result)) {
    $userid = $row['id']; //관련된 profileimg테이블에 userid를 넣어주기위해서 변수 생성
    $sql = "INSERT INTO profileimg (userid, status) VALUES ('$userid', 1);"; //profileimg테이블에 아이디와, 상태를
    //넣는데 status 1값은 프로필사진 올린게 없다는 것으로 정함: 1 사진올린것 있음, 0은 없음
    mysqli_query($conn, $sql); //sql쿼리 실행(insert문 실행)
    header("Location: 34_profile_upload.php");
  }
} else {
  echo "You have an error!";
}

?>