<?php
/* methods
by using type declaration, we can throw an error if wrong type is given!
works with:
- class/interface names
- self (used to reference to same class)
- array
- callable
- bool
- float
- int
- string
- iterable
- object
*/


class Person {
  public $name;
  public $eyeColor;
  public $age;

  //declare()가 처음에 쓰였다면 variable type을 지켜야한다
  // declare(strict_types = 1)
public function setName (string $newName) {  //메소드에 string으로 선언 
  $this->name = $newName;
}

public function getName() {
  return $this->name;
}

}