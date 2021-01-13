<?php

$x = 100;
//$x를 newCalc 함수보다 먼저 정의해도 함수는 어디서는 호출가능하다.
function newCalc($x) {  // x변수가 밖에서 정의되었기 때문에 파라미터를 $x로 넘긴다
   // ***important:one function does one thing!
// function's supported to be used multiful times and many places in the website
  $newnr = $x * 0.75;
  echo "Here is 75% of what you wrote: ".$newnr;
}

newCalc($x); //
echo "<br>";

$a = 10;
newCalc($a); // a변수에 할당하고 함수를 호출해도 가능하다