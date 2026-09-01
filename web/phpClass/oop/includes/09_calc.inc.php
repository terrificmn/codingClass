<?php
  declare (strict_types = 1);
  include 'class-autoloader.inc.php';

  $oper = $_POST['oper'];
  $num1 = $_POST['num1'];
  $num2 = $_POST['num2'];

  $calc = new Calc ($oper, (int)$num1, (int)$num2); //***중요: strict_types = 1로 선언했기 때문에 int면 맞춰줘야한다
  //(int)$variable은 int type convert

  try {
    echo $calc->calculator();
  } catch (TypeError $e) {
      echo "Error occured!" .$e->getMessage();
  }