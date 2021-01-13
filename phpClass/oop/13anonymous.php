<?php
//regular class
 
include_once "classes/SimpleClass.cls.php";

$obj = new SimpleClass();
$obj->helloWorld();

// Anonymous class 메모리에 저장시키지 않음. class가 오브젝트로 만들어진다음에 바로 지움

$newObj = new class() { //anonymous class 생성하는 키워드는 class() 이고 constructor가 있다면 ()붙인다. 없다면 ()생략 가능. 
  //클래스를 객체로 생성하면 메소드를 정의하거나 하는 것들은 기존 클래스와 같음 (컨스트럭터, 메소드, 프로퍼티, 스태틱.. 등..)
  //하지만 객체로 생성되고 클래스는 메모리에서 삭제. 왜냐하면 이코드는 여기에서 한번 실행되고 말기 떄문
  // 다른곳에서는 쓰일 필요가 없을 경우 사용한다. 오브젝트는 만들어 졌지만, 클래스는 delete됨
    public function helloWorld() {
    echo "<br>-Anonymous class. Hello World!";
  }
};  //;붙여줘야함

$newObj->helloWorld();
