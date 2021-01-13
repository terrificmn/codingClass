<?php
/* super global
$GLOBALS
$_POST
$_GET
$_COOKIE
$_SESSION
*/

$x = 5; //global scope

function something() {
  $y = 10; // local scope inside function // it only works for local in the function
  echo $x; // error!!  
  //echo $GLOBALS['x']; // x means $x // echo global variable 
  // not recommended using it all the time, just use it in a special case
}
//echo $x;
something(); // 만약 함수안에 $x를 에코 시킨다면 에러가 난다
// 함수안에서는 밖에서 선언된 변수를 사용할 수 없다
// *** super global: 
// 하지만 GLOBALS['']를 하면 슈퍼글로발이 되어서 함수안에서도 사용이 가능해진다

// **참고: 함수를 호출할 때 파라미터 값을 주고 함수에서도 $x를 파라미터로 받는다면
//        함수안에서도 global scope를 출력할 수 있다
//        예: something($x) ------ function something($x) { echo $x; }

// echo $y; // $y is local scope 
// if you call it outside of a function, it occurs error that has undefined variable.

?>