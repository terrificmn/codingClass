<?php 
include 'includes/autoloader.inc.php'; // autoloader.inc.php 파일을 include하면 그 안에 spl_autoload_register함수를 이용해서 
// 클래스 이름이 선언되서 사용될 때 마다 새롭게 class 파일을 include할 필요없이 한번에 클래스 파일들을 자동으로 load할 수 있다
//이제 클래스 선언하기 전에 autoloader.inc.php파일만 인쿠르드 하면 됨
//자세한 설명한 autoloader.inc.php 파일안에서 볼 것
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
$person1 = new Person("Daniel", "black", 28);

echo $person1->getName();

  echo "<br>";

?>
</body>
</html>
