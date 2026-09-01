<?php
  declare(strict_types = 1);
  include 'includes/class-autoloader.inc.php';
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <form action="includes/09_calc.inc.php" method="POST">
    <p>My own calculator </p>
    <input type="number" name="num1" placeholder="first number">
    <select name="oper">
      <option value="add">Addition</option>
      <option value="sub">Subtraction</option>
      <option value="div">Division</option>
      <option value="mul">Multiplication</option>
    </select>
    <input type="number" name="num2" placeholder="second number">
    <button type="submit" name="submit">계산</button>
  </form>
</body>
</html>