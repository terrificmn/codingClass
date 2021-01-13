<?php

class Test extends Dbh {
  //methods
  public function getUsers() {
    $sql = "SELECT * FROM oopUsers;";
    //상속을 받았으므로 $this->로 접근한다
    //상속받은 부모 Dbh클래스의 connect()메소드를 콜해서 db 연결한다
    $stmt = $this->connect()->query($sql);

    //Dbh 클래스에서 $pdo->setAttributes(로 fetch_assoc으로 해서 fetch()로 하면 됨
    //전체 db table에서 받아온다
    while($row = $stmt->fetch()) {
      echo $row['users_firstname']. '<br>';
    }

  }

  public function getUsersStmt($firstname, $lastname) {
    //prepared statement를 이용해서 처리할 것이기 때문에 placeholder 이용
    $sql = "SELECT * FROM oopUsers WHERE users_firstname = ? AND users_lastname = ?;";
    //prepare 사용
    $stmt = $this->connect()->prepare($sql);
    //위에서 ?표로 처리한 $sql에 순서대로 변수 넘겨준다
    // 파라미터로 받은 값으로 넘겨준다
    //PDO 클래스의 execute 메소드는 ([])안으로 입력
    $stmt->execute([$firstname, $lastname]);
    //fetch row와 associative 이용은 fetchAll
    $names = $stmt->fetchAll();

    foreach ($names as $name) {
      echo $name['users_dateofbirth']. '<br>';
    }
  }

  public function setUsersStmt($firstname, $lastname, $dob) {
    //prepared statement를 이용해서 처리할 것이기 때문에 placeholder 이용
    $sql = "INSERT INTO oopUsers (users_firstname, users_lastname, users_dateofbirth) VALUES (?, ?, ?);";
    $stmt = $this->connect()->prepare($sql);
    //파라미터로 받은 값들을 execute해준다 위의 ?의 prepared statement
    $stmt->execute([$firstname, $lastname, $dob]);


    
  }


}