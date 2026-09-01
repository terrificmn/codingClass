<?php
session_start(); //로그인 상태에서 삭제할 수 있게 하기 위해서 
include_once 'includes/dbh.inc.php';
$sessionid = $_SESSION['id'];

$filename = "uploads/profile".$sessionid."*"; //사진 아이디 가 같은 것은 (*)다 검색
$fileinfo = glob($filename); //패턴에 맞는 예로 * 같은거를 찾아주는 함수 // 확장자를 특정안해도 찾을 수 있다

//print_r($fileinfo); //배열로 들어가 있는것을 확인할 수 있다 
// 배열로 확인하는 이유는 $filename을 세션글로벌로 id를 맞춰서 찾는데
// 예를 들어 1번 id를 찾는데 '1'이 들어간것은 다 찾게된다 (아이디가 1번도 있고 11번도..)
// 예) Array ( [0] => uploads/profile1.jpg, [1] => uploads/profile11.jpg) 이런식으로 
// 나오게 되는데 무조건 첫번째 배열을 선택해 주면 되기 때문에
// 만약 아이디가 많아 져서 비슷한 것 일일이 검색 된다고 하면 로직을 수정하는게 좋을것 같음??

$fileext = explode(".", $fileinfo[0]);  //glob()로 찾은 $fileinfo 에는 배열로 여러개가 들어가 있을 수 있기 때문에..첫번째만 사용
//print_r($fileext); //explode()도 문자열을 split하는데 배열로 들어가진다 
$fileactualext = $fileext[1]; //확장만 사용하기 위해서 새로 변수 할당

$file = "uploads/profile".$sessionid.".".$fileactualext;

if (!unlink($file)) { // delete a file
  echo "File was not deleted!";
} else {
  echo "File was deleted!";
}

$sql = "UPDATE profileimg SET status=1 WHERE userid='$sessionid';";
mysqli_query($conn, $sql);

header("Location: 34_profile_upload.php?deletesuccess");
?>
