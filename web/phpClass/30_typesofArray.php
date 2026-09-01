<?php
  //Indexed arrays
  $data = array("Daniel", "John", "Jane");
  echo $data[0]; // 인덱스 순서대로 하나씩 배열로 들어가진다

  //Associative arrays //데이터에 이름을 지어서 배열로 만들 수 있다
  $data = array("first" => "Daniel", "last" => "Nielen", "age" = 25);

  //Multidimensional arrays
  $data = array(array("Daniel", "Nielsen"), "John", "Jane");
  // 배열안에 또 다른 배열이 들어가 있는 배열
  // data 첫번째 배열에 또 다른 배열이 들어가 있는데 data는 daniel, Nielsen이 들어가 있다
  //즉, data[0] ------> array[0]는 Daniel
  //            ------> array[1]는 Nielsen
  //    data[1] --> John
  //    data[2] --> Jane


?>
