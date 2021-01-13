<?php
/* SUPER GLOBALS
$_COOKIE  // save info in the user-side  (client/browser)
$_SESSION // save info in the server-side (server)
*/

setcookie("name", "Daniel", time() + 86400);

$_SESSION['name'] = "Daniel";  
// 로그인 에서 session 생성 - 데이터베이스에 가져온 정보로 생성을 한다

// 쿠키 셋팅, time()함수는 현재시간이므로 + 86400m 의미는 하루 뒤에 폐기된다)
// 시간 제한 없이 바로 없앨려면 time() -1 로 하면 된다. 
// (negative 어떤 수가 오더라도 현재시간이 지난 시간이 되므로 expired

// 쿠키는 상대적으로 덜 위험한 정보를 저장 (예: 쇼핑할때 관심있는 목록이라던가..)
// 세션은 아이디, 패스워드등의 정보 저장

// 세션은 브라우저를 닫으면 세션은 종료 된다
// 쿠키는 expire 되기 전까지 종료되지 않음
?>