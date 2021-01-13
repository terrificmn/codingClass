<?php
// Scope Resolution Operator (::)

// Here is the first class example
class FirstClass {
  //properties
  const SCOPE = ":: is Scope Resolution Operator";
  const EXAMPLE = "You can't change this!"; //상수, 변수랑 비슷하지만 한번 선언되면 바꿀 수 없는 것
  static $variable = "This is variable";
  // 대문자로 상수 이름을 만들면 나중에 기억하기 쉽다
  // const를 사용하는 예:
  // 변수로 사용하면 복잡하게 사용하다보면 프로그램 내에 어디선가 다른값으로 바뀌어져 있을 때, 어디인지 찾기 어려울 수 잇다 (복잡해져있다는 가정)
  // 바뀌지 않는 값으로 사용하는 것을 상수로 선언해서 사용하면 혹시라도 실수로 값을 바뀌는 것을 했을 때
  // 에러가 나면서 (바뀌지 않으므로) 실수한 부분을 바로잡을 수 있다

  //methods
  public static function test () {
    $testing = "This is a test!";
    return $testing;
  }

}

echo FirstClass::SCOPE."<br>"; 
echo FirstClass::$variable."<br>"; 

$a = FirstClass::EXAMPLE; //static으로 선언되것을 접근할 때는 ::(scope resolution operator라고 부름) 으로 하며 뒤에 property를 쓰면 됨

echo $a;

$b = FirstClass::test();
echo $b;


// Here is the Second class example
// inheritance classes
class SecondClass extends FirstClass {
  //properties
  public static $staticProperty = "A static property!";

  //methods
  public static function test2 () {
    echo parent::EXAMPLE; //parent의 static을 접근하는 것 ::(더블콜론) 키워드parent로 부모 class에 접근
    // 여기서 부모는 FirstClass임
    
    echo self::$staticProperty;
    // 일반적으로는 $this-> 이런식으로 접근하지만
    // static property에 접근할 때는 self::$staticProperty으로 할 수 있다 
  }
}

$c = SecondClass::test2();
echo $c;