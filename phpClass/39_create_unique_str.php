<?php

/* 1번째 방법
function generateKey() {
  $keyLength = 8;
  $str = "1234567890abcdefghijklmnopqrstuvwxyz()/$";
  $randStr = str_shuffle($str); //str_shuffle() 스트링을 랜덤으로 바꿔준다
  $randStr = substr(str_shuffle($str), 0, $keyLength); //substr() 스트링을 시작점과 끝점으로 자름 
  // 1st param는 스트링, 2번째 스타트(문자열 0번째부터 시작, 즉 처음), 3번째는 끝나는 legnth
  // ***사용 예: 랜덤 문자열은 유저의 패스워드를 바꿔줄 때 사용할 수 있다. 이메일로 랜덤 문자열(바뀐 패스워드) 보내주는 방식

  return $randStr;
}
*/

/* 2번째 방법
function generateKey() {
  //$randStr = uniqid(); //unique id 를 randomly 만들어주는 함수
  //$randStr = uniqid('daniel'); //unique id를 무작위로 만들어 주는데 문자열 파라미터 값으로 시작해서 뒷부분만 바뀜
  $randStr = uniqid('daniel', true); //2nd param 기본값은 false이지만 true주면 .(닷) 이후로 랜덤 문자열이 추가 됨
  return $randStr;
  //***Do not use this example for creating secure data like passwords since it is possible to guess part of the key
  //***Recommend to use it for creating unique URLs or file names 
}
*/
//echo generateKey();

include_once 'includes/dbh.inc.php';

function checkKeys($conn, $randStr) {  //DB에 연결하기 위해서 2개의 파라미터 값을 받는다, $randStr은 랜덤문자열
  $sql = "SELECT * FROM keystring";
  $result = mysqli_query($conn, $sql);

  while ($row = mysqli_fetch_assoc($result)) {
    if ($row['keystringKey'] == $randStr) {
      $keyExists = true;
    break; //***랜덤으로 만들어진 문자열과 데이터베이스에서의 컬럼의 값과 동일하다면 빠져나올 수 있게 한다
    } else {
      $keyExists = false;
    }
  }

  return $keyExists;
}


function generateKey($conn) {
  $keyLength = 1; //원할한 비교를 위해서 1자리로 제한 // 추후 이용할려면 원하는만큼 길이 조절 (8)
  $str = "abcdefg"; //원할한 비교를 위해서 7자리로 // 추후 더 늘려도 된다
  $randStr = substr(str_shuffle($str), 0, $keyLength);
  $checkKey = checkKeys($conn, $randStr);  //checkKeys()로 리턴 받은 값을 checkKey 변수에 준다

  while ($checkKey == true) { // 리턴값이 true이면 $keyExists가 true: db에 컬럼과 랜덤 값이 같은 경우 
    $randStr = substr(str_shuffle($str), 0, $keyLength);
    $checkKey = checkKeys($conn, $randStr);
  }

  return $randStr;
}

echo generateKey($conn); 
//db에 keystringKey컬럼에는 이미 a, b, c가 들어가 있어서 db와 비교후 abc가 아닌 것만 계속 랜덤하게 생성

?>