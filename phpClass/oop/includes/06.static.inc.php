<?php
class Person {
  // Properties
  public $name;
  public $eyeColor;
  //public $age = "undefinded"; 라고 도 할 수 있겠지만 __construct를 사용할 수 있다
  public $age;
  //private $name02;
  
  // static선언
  public static $dringkingAge = 21;
  
  //** static 은 object를 만들지 않고도 사용할 수 있다 */
  public static function setDringkingAge($newDA) {
    self::$dringkingAge = $newDA; //self::는 static property에 접근하는 키워드
  }

  public function getDA() { //staic을 이용한 property를 리턴하는 방법 
    return self::$dringkingAge; //static에 access하는 방법으로 $this와 비슷한 것이라고 생각하면 될 듯 
    //a keyword that is referenced this class instead of using $this when it comes to static with properties
  }

  public function __construct($name, $eyeColor, $age) {
    $this->name = $name; //last $name variable is not referred to the property ($name)
    //last $name is variable which is later used by an object through the parameter $name (passing data)
    $this->eyeColor = $eyeColor;
    $this->age = $age;
  }


  // Methods
  public function setName($name) {
    $this->name = $name; //$this means specific this class 그리고 $name이라고 하지않고 이미 선언되어 있으므로 name으로 사용(properties)
    $this->privatename = $name;
    // 마지막은 변수로 한 이유는 메소드에서 받는 데이터로 메소드를 호출하면서 넘겨주는 변수
  }

  public function setPrivateName($name) {
    $this->name02 = $name;
    // 마지막은 변수로 한 이유는 메소드에서 받는 데이터로 메소드를 호출하면서 넘겨주는 변수
  }
/*
  public function getName() { //property를 private으로 선언했을 때 이런 메소드를 사용할 수 있다
    //이 메소드는 public이기 때문에 $this 바로 이 클래스에 접근해서 private으로 선언된 name02를 리턴해준다 그러면 밖에서도 사용가능하게 됨
    return $this->name02;

  }
*/


  /*
  public function __destruct() { //destruct가 있으면 when object 만들어 질 때 자동으로 호출된다고 함
추후 배울 예정
  }
  */
}