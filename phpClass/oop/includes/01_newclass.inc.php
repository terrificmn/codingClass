<?php

class NewClass { // start with upper-case
  //Properties and Methods gose here
  public $info = "This is some info";
}
$object = new NewClass;
var_dump($object);
// 클래스 안에 아무 내요이 없을 때
//결과는 object(NewClass)#1 (0) { } 으로 아무것도 없는 상태로 출력된다
// public으로 변수를 선언하면 다른 결과물이 나온다
// {} 안에  {["info"]=> string(17) "This is some info"} 로 출력된다
//
