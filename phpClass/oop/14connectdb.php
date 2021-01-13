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
    //Test class로 $testObj 오브젝트 생성
    $testObj = new Test();
    $testObj->getUsers();
  
    echo "<br><br>getUsersStmt method:<br>";

    $testObj->getUsersStmt("Daniel", "Nielsen");

    $testObj->setUsersStmt("Happy", "NewYear", "2021-01-01");
    echo "DB has been updated.";

  ?>
</body>
</html>