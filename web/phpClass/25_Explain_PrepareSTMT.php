<!DOCTYPE html>
<html>
<head>
  <title>사용자 sign-up</title>
</head>
<body>
<!--
<form action="includes/signup.inc.prepare.php" method="POST"> 
  <input type="text" name="first" placeholder="Firstname"><br>
  <input type="text" name="last" placeholder="Lastname"><br>
  <input type="text" name="email" placeholder="E-mail"><br>
  <input type="text" name="uid" placeholder="Username"><br>
  <input type="text" name="pwd" placeholder="Password"><br>
  <button type="submit" name="submit">회원가입</button>
</form>            
-->
<!-- Explaination of SQL injection using mysqli with the prepared statement -->
<?php
   $data = "Admin"; //mysqli_stmt_bind_param()에서 비교할 스트링
  //즉, 입력 폼으로 받은 데이터를 말함 ($_POST 이나 $_GET으로 받은 변수)  
  
  //Created a template
  $sql = "SELECT * FROM users WHERE user_uid=?;";
  /*
  // 여기서 ?는 prepare statement 할 때 변환될 타입을 말한다 
  // 컬럼 당 1개 
  // 밑은 mysqli_stmt_bind_param() 참고
  */
  //Create a prepared statement
  $stmt = mysqli_stmt_init($conn);
  //Prepare the prepared statement
  if (!mysqli_stmt_prepare($stmt, $sql)) {  //mysqli_stmt_prepare함수는 2개 파라미터
    // 1st: mysqli_stmt_init함수로 받은 함수, 2nd는 sql쿼리
    echo "SQL statement failed";
  } else {
  //Bind parameters to the placeholder
    mysqli_stmt_bind_param($stmt, "s", $data);
    /*
    // The letter s mean that the parameter will be a STRING data type.
    // s = String, i = integer, b = BLOB, d = double
    
    // 만약 query에서 WhERE조건으로 더 검색할게 있다면 파라미터를 더 추가해줘야한다
    // *** INSERT문을 한다면 입력 폼으로 받은 각각의 변수들 ($_POST, $_GET으로 받은 값들)
    // 일단 2nd parameter를 "ss", 그리고 비교할 스트링 값을 변수로 더 만들어야함 $data2..등
    
    //예: $sql = "SELECT * FROM users WHERE user_uid=? AND user_first=?;";
    // 이런식으로 2개의 AND로 select하기를 원한다면 "ss" 3개이면 "sss" 이런식으로
    // 그리고 3번째, 4번째 파라미터는 순서대로 2개를 더 넣어야함 $data, $data2
    */

  //Run parameters inside database
    mysqli_stmt_execute($stmt);
    $result = mysqli_stmt_get_result($stmt);

      while ($row = mysqli_fetch_assoc($result)) {
      echo $row['user_uid' . "<br>"];
      }
  }
  /* *** 중요: The difference between mysqli_stmt_get_result and mysqli_stmt_store_result !
    (이하 생략... get result and store result)
    (암튼 둘다 거의 같은 기능(?): 쿼리 결과로 받은 값을 db에서 메모리에 저장(?) 하는 것)  

      get result 는 오직 SELECT쿼리가 성공했다면 결과셋을 받음 (리턴은 TRUE || FALSE)
        ㅡmysqli_fetch_array, fetch_row, , fetch_all, or mysqli_fetch_assoc 등으로 디비 데이터 row값을 사용할 수 있다
        num_rows를 사용하려면 (associative array로 받아와서 사용할 수 있어서 편함)
        $result = mysqli_stmt_get_result(Sstmt)로 받은 다음에 
        $row = mysqli_num_rows($result) 식으로 사용 가능 (mysqli_stmt_num_rows로 하면 데이터 row 갯수를 정확히 못가지고 옴)

        vs
      
      store_result는 SELECT, SHOW, DESCRIBE, EXPLAIN 등의 쿼리의 결과셋을 받음 (리턴은 TRUE || FALSE)
        많은 양의 데이터에는 메모리에 더 부담을 준다고 함
        mysqli_bind_result함수로 $row(값)에 변수로 bind해서 사용하게 되는데 
        사용예: mysqli_stmt_store_result($stmt) 를 한 후 bind를 해서 변수 arguments로 보내줘야한다(호출)
        mysqli_stmt_bind_result($stmt, $userid) (SELECT로 받아온게 userid라고 했을 때 변수로 선언해서 사용할 수 있다)
        mysqli_stmt_num_rows($stmt)로 row가 몇개 있지인지 확인 가능 (예로 SELECT한 데이터가 있는지? 없는지?)
        (그냥 num_rows가 아닌 mysqli_stmt_num_rows로 바로 사용 가능)
        그 다음에 mysqli_stmt_fetch로 해서 사용할 수 있다고 함
      사용예:
      $sql = "SELECT pwdUsers FROM loginUsers WHERE uidUsers = ? AND emailUsers = ?;
      $stmt = mysqli_stmt_init($conn);
      mysqli_stmt_prepare($stmt, $sql)) 
      mysqli_stmt_bind_param($stmt, "sss", $uid, $email);
      mysqli_stmt_execute($stmt);
      mysqli_stmt_store_result($stmt);
      mysqli_stmt_bind_result($stmt, $password);
        if (mysqli_stmt_num_rows($stmt) > 0) { //데이터 row값이 있다면 쿼리에 맞는 데이터가 있는 것
          mysqli_stmt_fetch($stmt);
          echo $password; //위에서 mysqli_stmt_bind_result($stmt, $password) password변수로 해놓았기 때문에 
          //바로 변수를 출력하면 데이터가 나옴
        } else {
            echo "없습니다.";
        }

        
      결론은.. 이런말이 있다고 함
      "Use get_result whenever possible and store_result elsewhere."

  */

  /* 
  *** PDO 방식이 아닌 mysqli를 사용하는 이유***
  In PHP there exists two methods of programming, which are
  "Procedural programming (PP)" and "Object oriented programming (OOP)". 
  In this PHP course we are using PP, and not OOP.
  
  When using PP, it is possible to use MySQLi and Prepared statements. 
  And when using OOP it is possible to use MySQLi, Prepared statements, and PDO. 
  Therefore we cannot use PDO in these lessons here.
  
  HOWEVER, in a few episodes 
  I will show how to get and insert data into a database using prepared statements
*/

?>
<body>
</html>
