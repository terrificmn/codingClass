<?php
session_start(); 
include_once 'includes/dbh.inc.php';
$id = $_SESSION['id'];

if(isset($_POST['submitLogin'])) {
  $_SESSION['id'] = 1;
  header("Location: 34_profile_upload.php");
}

if (isset($_POST['submit'])) {
  $file = $_FILES['file']; //super global $_FLIES['이름']

  //print_r($file); // $file 변수 확인해보면 배열이 어떻게 되어 있는지 알 수 있다
  
  $fileName = $_FILES['file']['name'];  //$file을 print_r()로 확인해보면 accociative array로 되어 있고 [name],
  //[type], [size]등이 있는 것을 알 수 있다

  //You could also have set it equal to $file['name'] instead.
  //it is up to you, but you want to do it.
  //so it would look like this: $fileName = $file['name'];
  
  $fileTmpName = $_FILES['file']['tmp_name'];
  $fileSize = $_FILES['file']['size'];
  $fileError = $_FILES['file']['error'];
  $fileType = $_FILES['file']['type'];

  $fileExt = explode('.', $fileName); //explode() can split string value. 1st parameter will be the start from 2nd param
  $fileActualExt = strtolower(end($fileExt)); //strtolower(): lowecase로 만듬, end()함수는 마지막 데이터를 뽑아옴
  
  $allowed = array('jpg', 'jpeg', 'png');

  if(in_array($fileActualExt, $allowed)) { // in_array()는 check if a value exists in an array 
    if ($fileError === 0) {
      if ($fileSize < 1000000) { //1,000,000bytes == 1,000kb == 1mb
        //$fileNameNew = uniqid('', true).".".$fileActualExt; //uniqid()이용해서 무작위로 이름은 만듬 
        //파라미터2번째 true는 무작위 스트링을 더 길게 해줌 (23 캐릭터)
        // 새로운 이름과 확장자를 이어준다
        $fileNameNew = "profile".$id.".".$fileActualExt;  //24_profile_upload.php에서 사용하려면
        // 프로파일 이미지를 만들어 줘야하는데 형식은 중간에 id가 들어가게 만든다 
        $fileDestination = 'uploads/'.$fileNameNew;
        move_uploaded_file($fileTmpName, $fileDestination); //move_uploaded_file()함수를 이용해서 템프파일명 저장할 dir에 이동 저장시킨다
        ///**저장할 디렉토리의 권한을 바꿔줘야한다 예: 757  other users가 쓰기 기능이 되어야 저장이 된다 */
        $sql = "UPDATE profileimg SET status=0 WHERE userid='$id';"; //profileimg테이블의 status의 0으로 업데이트
        // 0은 사진을 올린게 있다고 약속한 값
        mysqli_query($conn, $sql);

        //header("Location: 33_file_upload.php?uploadsuccess"); //33_file_upload.php 사용할 때
        header("Location: 34_profile_upload.php?uploadsuccess"); //34강좌 사용할 때

      } else {
        echo "Your file is too big!";
      }
    } else {
      echo "There was an error upoading your file!";
    }
  } else {
      echo "You cannot upload files of this type!";
  }

  

}

?>