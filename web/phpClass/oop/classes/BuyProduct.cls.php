<?php

// extends 받기 (inheritance from Visa class)
class BuyProduct extends Visa {
/*
  public function thisisnofunc() {
    #상속받은 abstract class Visa에서 getPayment() 메소드를 사용하게 인터페이스를 정의했기에 getPayment가 없으면 에러가 발생
    #에러 확인하려면 아래 getPayment()를 주석처리 // 물론 오브젝트에서 호출할 때도 이름을 좀 바꿔줘야함
    #주석처리하기 귀찮고 오브젝트에서 호출하는것도 좀 바꿔줘야하니 귀찮;;;
    #결과
    // 요래 나옴
    //Fatal error: Class BuyProduct contains 1 abstract method and must therefore be declared abstract or 
    //implement the remaining methods (Visa::getPayment) 
    
  }
*/
  public function getPayment() {
    //$this 키워드는 현재 이 클래스를 접근하기도 하지만 상속받은 Visa class(abstract임)에 접근할 수 도 있다
    return $this->visaPayment(); ///Visa class의 메소드
  }
  
}