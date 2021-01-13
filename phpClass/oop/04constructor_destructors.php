<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <?php
include 'includes/04.person.inc.php';

$person1 = new Person("Daniel", "Blue", 28); //__construct를 호출해서 3가지 문자열(파라미터)를 넘겨주면 지정된 properties에 넣어주게 된다
//destruct는 처음으로 객체를 만들면서 __construct()이 실행되고 __destruct()도 실행되는 것을 기억! (클래스 안에서 코딩하고 밖에서는 호출하지는 않는다)
echo $person1->name; //echo person1의 객체의 name property 출력하기 // 위의 construct에 의해 각 properties에 파라미터로 데이터가 넘어감
echo $person1->eyeColor;
$person1->setName("John"); // 여기서 메소드를 호출해서 직접 바꿔주면 위의 constructor를 만든것과 다른 결과를 볼 수 있다
echo $person1->name;

$person1->setPrivateName("Mike"); //메소드를 호출해서 "Mike" 넘겨준다
echo $person1->getName(); //private propety를 리턴받아서 출력 // Private으로 선언된 것은 class밖에서는 사용 못하지만 리턴값으로 사용할 수 있다.
// echo $person1->name02; //직접 접근하면 에러 발생한다 name02는 private 선언
