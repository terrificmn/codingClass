<?php

class UsersView extends Users {

  public function showUsers($name) {
    //Users 클래스의 메소드 바로 사용
    $results = $this->getUser($name);
    echo "Full name: " .$results[0]['users_firstname']. " " . $results[0]['users_lastname']. "<br>";
    echo "Date of birth: " .$results[0]['users_dateofbirth'];
  }
}