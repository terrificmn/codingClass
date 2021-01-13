<?php
///*** 2개 이상의 파일 지우기 */

$fileNames = $_POST['filename'];
$removeSpaces = str_replace(" ", "", $fileNames); // str_replace(param1: search, param2: replace, param3: value)
$allFileNames = explode(",", $removeSpaces); //explode()는 배열로 만들어 진다
$countAllNames = count($allFileNames); //count()배열의 수를 센다

for ($i=0; $i < $countAllNames; $i++) {
  if (file_exists("uploads/".$allFileNames[$i]) == false) { //file_exists()는 경로파일이 있는지 boolean return
    header("Location: 35_deletefile.php?deleteerror");
    exit(); //if문을 빠져나가면서 다른 코드는 실행하지 않음
  }
}

for ($i=0; $i < $countAllNames; $i++) {
  $path = "uploads/".$allFileNames[$i];
  if (!unlink($path)) { //파일을 지움, 기존에 파일이 없다면 지울 수가 없어서  if문 실행
    echo "You have an error!";
    exit();
  }

}

/* 단일 파일 지우기
$path = "uploads/cat.jpg";

if (!unlink($path)) { //unlink() 함수는 파라미터는 path를 (파일경로파일명) 넘겨주면 됨, 파일을 지우는 함수 
  //지우지 못하였다면 실행
  echo "You have an error!";
} else {
  echo "You have deleted a file!";
}
*/
?>