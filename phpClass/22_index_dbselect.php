<?php
  include_once 'includes/dbh.inc.php';
?>
<!DOCTYPE html>
<html>
<head>
  <title></title>
</head>
<body>

<?php
  $sql = "SELECT * FROM users;";  //sql query 에서도 ;으로 끝나야 한다
  $result = mysqli_query($conn, $sql);
  // mysqli_query()에서 파라미터값은 dbconnection 과 query이므로
  // 위에서 include된 dbh.inc.php 파일에서 정의된 $conn사용하고 mysqli_connect()사용한 상태
  $resultCheck = mysqli_num_rows($result); // return value가 0이면 데이터가 없는것
  //if 문으로 실제 데이터가 있으면 수행할 수 있게 하기위한 변수$resultCheck이용
  //row 데이터 만큼 숫자로 리턴받는다.

  if ($resultCheck > 0) { //데이터를 못받았다면==0
      while ($row = mysqli_fetch_assoc($result)) { // db에서 받아온 데이터를 하나씩 넣는
      echo $row['user_uid'] . "<br>"; //array이용 출력
      // [0], [1] 이런식으로 사용할 수 도 있지만
      // ['문자열']로도 가능한데 테이블의 컬럼명과 동일하다

    }
  }

?>
<body>
</html>
