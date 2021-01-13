<?php
//private is kind of simular to variable in the object
//but remember that it's not the same thing.

class Person { //class start with uppercase
  //private $first = "Daniel";
  protected $first = "Daniel"; //현재 클래스에서만 사용하거나 extends 해서 사용하는 클래스만 허용하는 선언, 즉, 클래스 밖에서 접근 가능
  private $last = "Nielsen"; //클래스 안에서만 접근가능 : private
  private $age = "28";

  public function owner() {
    $a = $this->first; //$this는 여기 오브젝트를 말함, 즉 Person이라는 object
    //$this 키워드는  현재 클래스의 property를 액세스 하게 해줌 (reference to something within the same class)
    // ->표시는 포인트를 지정해주는 의미
    // first인데 $first가 아닌 이유는 property 이기 떄문
    //위에서 변수와 비슷하다고 했지만 다른 이유가 여기에 있음
    // private으로 선언할 때 변수처럼 $사인을 써서 $first라고 했지만
    // 선언할 때만 그렇게 하게 되는 것이고 정확히 이것은 변수가 아니고 프로퍼티 Property
    // 그렇기 때문에 $싸인을 안쓰고 first라고 지정하는 것이라고 함
    return $a;
  }
}
/* //일반적 클래스 선언
class Pet { 
  //private function owner() { //private 메소드(function)은 only available inside Object
  public function owner() { //public은 오브젝트 밖에서도 사용할 수 있다
    $a = "Hi there!";
    return $a;
  }
}*/

class Pet extends Person { //*** extends 다른클래스명 ---  inheritance 게승을(상속) 받을 수 있다
  //즉 Person이라는 클래스의 property, method를 다 사용할 수 있다
  public function owner() {
    $a = $this->first; //상속을 받았기 때문에 Person 클래스의 property를 사용할 수 있다
    // **하지만 Person class의 property가 private 으로 오브젝트 내에서만 사용하게 선언해서 에러가 발생한다
    //Undefined property: Pet::$first 이런식으로 에러 발생
    //이를 해결하려면 Person클래스의 프로퍼티를 protected 로 선언해주면 Person클래스 안에서와
    // extends해서 사용하는 다른 클래스에서도 사용이 가능해진다

    return $a;
  }
}

