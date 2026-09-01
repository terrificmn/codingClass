<?php
//***검색해서 지우기 //
//편의상 html없이 바로 지우는 코드
//파일 확인 한 후 한번만 실행할 것 (새로고침 금물!)
//(참고) 고양이, 강아지 사진은 Downloads/ 폴더에 있음: 필요할 경우 uploads/디렉토리에 복사 사용하면 됨 


$path = "uploads/cat*"; //*표시는 모든문자열 포함 uploads/디렉토리의cat으로 시작하는 모든 파일을 의미
//**참고: input box의 값을 $_POST슈퍼글로벌로 받아와서 진행해도 될 것 같음

$fileinfo = glob($path); //glob()는 find a file in the path($path) // 배열로 생성됨
$fileactualname = $fileinfo[0]; //첫번째것을 지우기 위해서 [0]배열 이용


if (!unlink($fileactualname)) {
  echo "You have an error!";
} else {
  echo "You have deleted a 1 file.";
}

//결과: cat1.jpg만 지워짐
//주의! 새로고침을 막 하면 금방 다 지워짐
?>
