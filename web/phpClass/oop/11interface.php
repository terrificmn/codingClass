<?php
//Interfaces 를 사용하는 예를 들어놓은 것
//여러 클래스에서 사용할 수 있는 룰(interface)를 만들어서 사용하는 것
// 일단 현재(20.1.4)에 설명할 수 는 없지만 대충 이해

/* 
It seems like many contributors are missing the point of using an INTERFACE. 
An INTERFACE is not specifically provided for abstraction.
That's what a CLASS is used for. Most examples in this article of interfaces could be achieved just as easily using just classes alone.

An INTERFACE is provided so you can describe a set of functions and then hide the final implementation of those functions 
in an implementing class. This allows you to change the IMPLEMENTATION of those functions without changing how you use it.

For example: I have a database. I want to write a class that accesses the data in my database. I define an interface like this:

interface Database {
function listOrders();
function addOrder();
function removeOrder();
...
}

Then let's say we start out using a MySQL database. So we write a class to access the MySQL database:

class MySqlDatabase implements Database {
function listOrders() {...
}
we write these methods as needed to get to the MySQL database tables. 
Then you can write your controller to use the interface as such:

$database = new MySqlDatabase();
foreach ($database->listOrders() as $order) {

Then let's say we decide to migrate to an Oracle database. We could write another class to get to the Oracle database as such:

class OracleDatabase implements Database {
public function listOrders() {...
}

Then - to switch our application to use the Oracle database instead of the MySQL database we only have to change ONE LINE of code:

$database = new OracleDatabase();

all other lines of code, such as:

foreach ($database->listOrders() as $order) {

will remain unchanged. The point is - the INTERFACE describes the methods that we need to access our database. 
It does NOT describe in any way HOW we achieve that. 
That's what the IMPLEMENTing class does. We can IMPLEMENT this interface as many times as we need in as many different ways as we need. 
We can then switch between implementations of the interface without impact to our code 
because the interface defines how we will use it regardless of how it actually works.
*/

interface PaymentInterface { //interface를 만듬
  //크래스에서 사용할 룰 지정 
  //다른클래스에서 서로 다른 메소드 이름을 지을 수 있겠지만(여러사람이 일할 경우) 
  //여기 인터페이스에서 정의된 것 처럼 payNow()이름으로 메소드를 사용하여야 하고
  //아래 3개의 클래스는 그룹화 되어 여기 인터페이스의 블루프린트를 따른다고 생각하면 됨
  public function payNow(); //메소드 payNow를 선언하고 다른 클래스에서 사용할 수 있게 해줌 (inheritance 비슷? implements를 해줌)
}
interface LoginInterface { //interface를 만듬
  public function LoginFirst(); //메소드 payNow를 선언하고 다른 클래스에서 사용할 수 있게 해줌 (inheritance 비슷? implements를 해줌)
}


class Paypal implements PaymentInterface, LoginInterface {
  public function loginFirst() {} //만약 Paypal클래스는 loginFirst를 먼저 사용해야하면 다른 클래스에서는 사용불가? 
  // 그러면 다른 클래스에서도 loginFirst()메소드를 다 만들어 줘야한다
  public function payNow() {}
  public function paymentProcess() { //그래서 지불 방법을 메소드로 만들어 준다
    $this->loginFirst();
    $this->payNow();
  }

}

class BankTransfer implements PaymentInterface, LoginInterface { //PaymentInterFace, LoginInterface 인터페이스를 따름
  public function loginFirst() {} //만약 Paypal클래스는 loginFirst를 먼저 사용해야하면 다른 클래스에서는 사용불가? 
  public function payNow() {}
  public function paymentProcess() { //그래서 지불 방법을 메소드로 만들어 준다
    $this->loginFirst();
    $this->payNow();
  }

}

class Visa implements PaymentInterface {
  public function payNow() {}
  public function paymentProcess() { //그래서 지불 방법을 메소드로 만들어 준다
    $this->payNow();
  }
}

class Cash implements PaymentInterface {
  public function payNow() {}
  public function paymentProcess() { //그래서 지불 방법을 메소드로 만들어 준다
    $this->payNow();
  }
}

class BuyProduct {
  //public function pay(Cash $paymentType) { //메소드를 Cash 클래스의 이용한다고 하면 다른 클래스를 사용하면 에러)
  public function pay(PaymentInterface $paymentType) {
    $paymentType->payNow();

  }
}

//Cash를 이용해서 오브젝트를 생성
$paymentType = new Cash();
//BuyProduct클래스를 이용 오브젝트 생성
$buyProduct = new BuyProduct();
//BuyProduct 클래스의 메소드를 호출하는데 파라미터로 값을 넘겨주는데 받는 값은 Cash로 선언되어 있기에 
//만약 손님이 Paypal, Visa를 사용할 지 모르기때문에 다른것으로 결제(넘겨준다면) 에러가 발생
//위의 3개의 Paypal, Visa, Cash를 다 사용하려면 그 때 인터페이스를 사용한다고 함
$buyProduct->pay($paymentType);

