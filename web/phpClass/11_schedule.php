<?php
  $dayofweek = date('w'); // function 관련한 website 참고 
  // https://www.w3schools.com/php/func_date_date.asp
    switch ($dayofweek) {
      case 1:
        echo "It it Monday!";
      break;
      case 2:
        echo "It it Monday!";
      break;
      case 3:
        echo "It it Tuesday!";
      break;
      case 4:
        echo "It it Wednesday!";
      break;
      case 5:
        echo "It it Thursday!";
      break;
      case 6:
        echo "It it Saturday!";
      break;
      case 0:
        echo "<h1>It it Sunday!</h1>";  //코드안에 html tag를 넣어도 된다
      break;

    }
 ?>