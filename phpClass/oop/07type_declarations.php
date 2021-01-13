<?php
declare(strict_types = 1); //변수도 type에 따라서 만들어져야한다 . *원래 php는 type에서 자동으로 맞춰주지만 strict types = 1하면 type도 맞춰야한다
include 'includes/07_type.inc.php';
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <?php
  
  $person1 = new Person();

  try {
    //$person1->setName(2); //Error!: Argument 1 passed to Person::setName() must be of the type string, int given
    //라고 에러가 난다  // 위에서 declare를 strict으로 선언했고 method setName의 파라미터는 sring으로 선언 되있기 때문
    $person1->setName("Mike"); //type declare를 했으니깐 맞는 변수로 넘겨주어야 한다!!!!
    //위에서type declare가 안되어 있다면 php에서는 파라미터로 넘어가는 부분은 자동적으로 바꿔주기 때문에 
    //파라미터 변수가 string으로 선언 되어 있어도 숫자를 넘겨주면 숫자로 표현해 준다
    echo $person1->getName();
  } catch (TypeError $e) {
      echo "Error!: " . $e->getMessage();
  }
  ?>
</body>
</html>