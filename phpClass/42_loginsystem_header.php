<?php
session_start();  //모든 페이지에서 세션변수가 잘 작동하도록 스타트 해줌
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Practical Sign-up</title>
</head>
<body>
  <header>
    <nav>
      <ul>
        <li><a href="42_loginsystem.php">Home</a></li>
        <li><a href="#">test1</a></li>
        <li><a href="#">test2</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
    </nav>
    
    <div><!--로그인 창-->
    <?php
    if (isset($_SESSION['userId'])) {
      echo '<form action="includes/42_logout.inc.php" method="POST">
            <button type="submit" name="logout-submit">Logout</button>
            </form>';
    } else {
      echo '<form action="includes/42_login.inc.php" method="POST">
            <input type="text" name="mailuid" placeholder="Username/Email...">
            <input type="password" name="pwd" placeholder="Password...">
            <button type="submit" name="login-submit">Login</button>
            </form>
            <a href="42_signup.php">Signup</a>';
    }
    ?>
        
    </div>
  </header>

</body>
</html>