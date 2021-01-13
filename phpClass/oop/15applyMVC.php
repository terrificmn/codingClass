<?php 
include 'includes/class-autoloader.inc.php';
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PDO</title>
</head>
<body>
  <?php
    //오브젝트 생성
    $usersObj = new UsersView();
    $usersObj->showUsers("Daniel");

    /* 출력되는 것 없이 db입력됨
    $usersObj2 = new UsersContr();
    $usersObj2->createUser("Jane", "Doe", "2000-03-07");
    */

  ?>
</body>
</html>