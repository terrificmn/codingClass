<?php
require "42_loginsystem_header.php";
?>

  <main>
    <div class="wrapper-main">
      <section class="section-default">
        <h1>Signup</h1>
        <?php
          if (isset($_GET['error'])) { //에러일 경우의 $_GET변수로 확인
            // $_GET 변수에 각각 상황에 맞춰서 에러 메세지를 보여준다
            if ($_GET['error'] == "emptyfields") { 
                echo '<p class="signuperror">Fill in all fields!</p>';
            
              } else if ($_GET['error'] == "invalidmailuid")  {
                echo '<p class="signuperror">Invalid username and e-mail!</p>';
            
              } else if ($_GET['error'] == "invalidmail") {
                echo '<p class="signuperror">Invalid e-mail!</p>';
            
              } else if ($_GET['error'] == "invaliduid") {
              echo '<p class="signuperror">Invalid username!</p>';
            
            } else if ($_GET['error'] == "passwordcheck") {
              echo '<p class="signuperror">Your passwords do not match!</p>';
            
            } else if ($_GET['error'] == "usertaken") {
              echo '<p class="signuperror">Username is already taken!</p>';
            }

          } else if ($_GET['signup'] == "success") { //success일 때
              echo '<p class="signupsuccess">Signup successful!</p>';
          }

        ?>
        <form action="includes/42_signup.inc.php" method="POST">
        <?php
          if (isset($_GET['error'])) {

            if ($_GET['error'] == "emptyfields" || $_GET['error'] == "passwordcheck") {
              
              echo '<input type="text" name="uid" value="'.$_GET['uid'].'" placeholder="Username">
              <input type="text" name="mail" value="'.$_GET['mail'].'" placeholder="E-mail">
              <input type="password" name="pwd" placeholder="Password">
              <input type="password" name="pwd-repeat" placeholder="Repeat Password">';


            } else if ($_GET['error'] == "invalidmailuid") { //mail 과 uid가 모두 에러 일때는 인풋 폼을 다시 작성
                echo '<input type="text" name="uid" placeholder="Username">
                <input type="text" name="mail" placeholder="E-mail">
                <input type="password" name="pwd" placeholder="Password">
                <input type="password" name="pwd-repeat" placeholder="Repeat Password">';
            
            } else if ($_GET['error'] == "invalidmail") {
                echo '<input type="text" name="uid" value="'.$_GET['uid'].'" placeholder="Username">
                <input type="text" name="mail" placeholder="E-mail">
                <input type="password" name="pwd" placeholder="Password">
                <input type="password" name="pwd-repeat" placeholder="Repeat Password">';
            
            } else if ($_GET['error'] == "invaliduid" || $_GET['error'] == "usertaken") {
                echo '<input type="text" name="uid" placeholder="Username">
                <input type="text" name="mail" value="'.$_GET['mail'].'" placeholder="E-mail">
                <input type="password" name="pwd" placeholder="Password">
                <input type="password" name="pwd-repeat" placeholder="Repeat Password">';

            } 

          } else {  // $_get변수가 error 가 아닐 떄 // 원래 signup 폼을 띄운다
              echo '<input type="text" name="uid" placeholder="Username">
              <input type="text" name="mail" placeholder="E-mail">
              <input type="password" name="pwd" placeholder="Password">
              <input type="password" name="pwd-repeat" placeholder="Repeat Password">';
          }
        
        ?> <!--
          <input type="text" name="uid" placeholder="Username">
          <input type="text" name="mail" placeholder="E-mail">
          <input type="password" name="pwd" placeholder="Password">
          <input type="password" name="pwd-repeat" placeholder="Repeat Password">
        -->
          <button type="submit" name="signup-submit">Signup</button>
        
        </form>
      </section>
    </div>
  </main>

