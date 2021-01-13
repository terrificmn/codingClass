<?php

class UsersContr extends Users {
  
  //user class의 setUser를 public으로 하고 index페이지에서(또는 특정 페이지) 직접 호출할 수도 있겠지만
  //다른클래스 UsersContr같은 클래스로 오브젝트를 선언해서 하는 이유는 보안 때문 이다
  //DB와 직접 액세스 하는 것은 User 클래스만 하게 된다 (MVC의 Model역활) 
  
  public function createUser($firstname, $lastname, $dob) {
    $this->setUser($firstname, $lastname, $dob);
  }  
}