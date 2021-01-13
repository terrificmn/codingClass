<?php
class Person {
  // Properties
  public $name;
  public $eyeColor;
  public $age;

  // Methods
  public function setName($name) {
    $this->name = $name; //$this means specific this class 그리고 $name이라고 하지않고 이미 선언되어 있으므로 name으로 사용(properties)
    // 마지막은 변수로 한 이유는 메소드에서 받는 데이터로 메소드를 호출하면서 넘겨주는 변수
  }
}