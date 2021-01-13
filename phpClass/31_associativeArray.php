<?php

$data = array("first"=>"Daniel", "last"=>"Nielsen", "age"=>25); //string 은 "" 
  // 쉽게 생각해서 인덱스를 이해할 수 있는 문자열 형태로 연결시키는 거 같다...
  // 인덱스 방식은 숫자로만 되어 있기에 직관적이지 않지만 문자열로 해놓으면 직관적이 된다는 느낌...
  echo $data["first"];

/* //풀어서 쓰면 이런 느낌... 
  $data["first"] = "Daniel";
  $data["last"] = "Nielsen";
  $data["age"] = 25;
  print_r($data); //data[0] 같은 인덱스 형식이 아닌 [first]=>Daniel 가지고 있는것을 알 수 있다
*/

?>