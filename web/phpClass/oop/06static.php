<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <?php 
  include 'includes/06.static.inc.php';

  //class의 static 을 사용하면 오브젝트를 먼저 만들지 않고도 static으로 선언된 프로퍼티나 메소드를 사용할 수 있다
  //class 에서 static 과 none static 으로 카테고리화 해서 사용할 수 있다
  //즉, 클래스안에는 꼭 속하지 않아도 되는 것들을 만들 때 static으로 선언해서 만든다고 이해하면 될 듯
  // 그래서 꼭 클래스를 만들지 않고도 외부에서 접근해서 사용가능하게 끔 하는 것이라고 이해함
  echo Person::$dringkingAge; // 여기서 ::은 static으로 선언된 것에 access하겠다는 의미
  Person::setDringkingAge(18);
  echo Person::$dringkingAge;
  
  echo "<br>";
  //** 오브젝트를 만들고 staic property 받아오기: 동일하게 메소드에서 리턴해주는데 단, staic에서 클래스를 참조 할때는 self:: 를 기억하자  */
  $person1 = new Person("Daniel", "Bule", 28);
  echo $person1->getDa();
  //위에서 setDringkingAge(파라미터)로 주었기 때문에 18로 설정되었고 getDA()메소드를 통해 다시 18로 나오는 것을 알 수 있음
  


  ?>

</body>
</html>