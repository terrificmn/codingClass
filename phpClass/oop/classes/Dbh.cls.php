<?php
class Dbh {
  // properties
  // 현재 클래스만 사용할 수 있게 private으로 선언  /not public
  private $dbHost = "localhost";
  private $dbUser = "root";
  private $dbPwd = "superocta";
  private $dbName = "phplessons";

  // methods
  // 현재 클래스에서만 접근할 수 있게 protected로 선언
  protected function connect() {
    //mysqli statement를 사용하는 것이 아닌 mysql db를 사용하는 것!!!
    //현재 클래스의 properties 접근하기 위해서는 $this-> 키워드를 사용, properties에는 $을 붙이지 않는다
    $dsn = 'mysql:host=' . $this->dbHost . ';dbname=' .$this->dbName;
    //PDO 클래스를 생성 (파라미터 넘겨주는 것은 $dsn, $유저, $패스워드)
    $pdo = new PDO($dsn, $this->dbUser, $this->dbPwd);
    //optional Parameters
    $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
    return $pdo;
  }

}