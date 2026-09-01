<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <?php
  include 'includes/02_person.inc.php'; //클래스 인크르드
    $pet01 = new Pet();
    echo $pet01->owner();  //owner라는 클래스 안의 메소드를 echo함 (오브젝트 안의 펑션)
    // 위의 코드는 에러가 발생됨
    // private으로 선언 되었기 때문에 이 메소드를 사용할 수 없다. 같은 오브젝트 안에서만 사용가능
    // 클래스의 메소드 (펑션)을 public으로 선언하면 클래스 밖에서도 사용이 가능하다
    // 결과는: Hi there! 잘 출력된다
    echo "<br>";

    $person01 = new Person();
    echo $person01->owner(); // owner 메소드를 (메소드는 public)불렀을 때 private property 로 되어 있는데 출력이 되는 이유는
    //오브젝트 안에서 $this를 이용해서 접근했고 오브젝트 안에서 private $first PROPERTY값을 $a 넣어서 리턴했기 때문에 가능

    // 출력: Daniel

    
  
  ?>

</body>
</html>