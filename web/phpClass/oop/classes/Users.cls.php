<?php
// ** mvc 모델 model, view, and control
class Users extends Dbh {
  
  // db 액세스하기 때문에 protected 로 정의 (이 클래스를 직접 오브젝트로 쓰지는 않는다 mvc중 model에 해당)
  // only handles running sql through DB 여기서는 실행만 
  // only interact with databases through this class
  protected function getUser($name) {
    $sql = "SELECT * FROM oopUsers WHERE users_firstname = ?;";
    $stmt = $this->connect()->prepare($sql);
    $stmt->execute([$name]);

    $results = $stmt->fetchAll();
    return $results;

  }

  //입력하기 위해서 파라미터를 넘겨주어야 함 (각각의 컬럼이 되겠음)
  protected function setUser($firstname, $lastname, $dob) {
    //prepared statement를 이용해서 처리할 것이기 때문에 placeholder 이용
    $sql = "INSERT INTO oopUsers (users_firstname, users_lastname, users_dateofbirth) VALUES (?, ?, ?);";
    $stmt = $this->connect()->prepare($sql);
    //파라미터로 받은 값들을 execute해준다 위의 ?의 prepared statement
    $stmt->execute([$firstname, $lastname, $dob]);

  }
}