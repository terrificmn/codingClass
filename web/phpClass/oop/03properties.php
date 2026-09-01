<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <?php
include 'includes/03.person.inc.php';

/*
$name = "Daniel";
$eyeColor = "Blue";
$age = 28;
// 이런 사람이 있다고 예를 들었을 때 또 다른 사람이 필요하다면 
// 아래처럼 사람 02를 만들어서 또 코드를 만들어야 할 것이다
$name02 = "mike";
$eyeColor = "brown";
$age = 30;
// 클래스는 이런 사람의 템플릿을 만든다고 생각해도 될듯
*/

$person1 = new Person(); /*//object선언 //__constructor를 사용할 떄 ()를 사용하기 때문에 ()를 사용하는게 좋다. */
$person1->setName("Daniel"); //메소드에 접근해서 "daniel"이라고 문자열 넘겨주면 메소드에서는 name properties를 변경해 준다

$person2 = new Person();
$person2->setName("Timmy");

echo $person1->name; // name이라는 properties에 접근하기 위해서 사용 $name이라고 하지않음 즉, variable과는 다르다
echo $person2->name; // class를 이용해서 같은 것을 또 다른 오브젝트를 만듬 // 서로 다른것을 알 수 있다


  ?>
</body>
</html>