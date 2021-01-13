<?php

// abstract class는 실제 오브젝트를 생성해서 만드는 것이 아니고 
// 특정 클래스에서만 사용할 수 있게 만드는 것

abstract class Visa {
  public function visaPayment() {
    return "Perform a payment";
  }

  //in order to use any abstact method, you should declare class as abstarct class
  //인터페이스와 비슷한 기능으로 abstract 정의할 떄 특정 메소드를 꼭 사용하게 하는 것
  //현재 이 클래스를 상속받는 클래스들은 아래 메소드를 포함시켜야 함: 룰
  //상속받은 클래스에서 아래 메소드를 사용안하면 에러가 남
  abstract public function getPayment();
}