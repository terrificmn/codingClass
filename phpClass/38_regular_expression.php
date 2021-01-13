<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <?php
  //Here is a string
  $string = "My name is Daniel, Daniel is my name.";
  
  // "/여기 안에 쓰면 regular expression/"  즉, "/안에다가 쓰면 됨  
  //preg_match("/Daniel/", $string); 는 문자열안에 특정 문자열이 있는 확인(/슬래쉬 안에 쓴 문자/)
  /*
  if (preg_match("/Daniel/", $string) { //2개의 파라미터만 줄 수 있다
    echo "It is a match.";
  }
  */
  echo "<h1> 원래 문자열: ".$string."</h1>";
  echo "<h1> preg_match 쓰임새 </h1>";
  if (preg_match("/Daniel/", $string, $array)) { //3번째 파라미터로 배열을 줄 수 있는데 
    print_r($array); //배열이지만 특정문자열 "/Daniel/"은 한번만 찾는다
  }
  echo "<br>";
  echo "<h1> preg_match_all 쓰임새 </h1>";
  if (preg_match_all("/Daniel/", $string, $array)) { //preg_match_all 은 특정 문자열을 여러번이고 찾아서 2차원배열로 리턴한단
    print_r($array);
  }
  
  echo "<br>";
  
  if (preg_match_all("/Da(ni)el/", $string, $array)) { //preg_match_all 은 특정 문자열을 여러번이고 찾아서 2차원배열로 리턴한단
    //특정문자열 슬래쉬 안에 다시 괄호를 넣으면 (ni)도 찾게 된다
    //즉 Daniel을 먼저 찾고 ($string에는 다니엘이 2개)
    // 그다음에 다시 ni를 찾는다 ($string에는 ni도 2개)
    // 그래서 배열엔 아래처럼 된다
    // Array ( [0] => Array ( [0] => Daniel [1] => Daniel ) [1] => Array ( [0] => ni [1] => ni ) ) 
    print_r($array);
  }

  echo "<h1> preg_replace </h1>";
  $string2 = preg_replace("/Daniel/", "John", $string);
  echo $string2;

  echo "<br> preg_match return:<br>";
  //echo preg_match("/(k|q)/", $string); //return true or false // ()안에 |는 or
  //echo preg_match("/[abc]/", $string); // abc가 들어가 있으면 true
  //echo preg_match("/[^abc]/", $string); // abc가 없으면 true (캐릭터 그래도 소문자 abc가 없으면 true, 만약 문자에서 abcd가 있으면 3글자가 아니어서 true)

  //^의 활용 예 (조금 헤깔려서 ㅋ) 만약 특수기호를 !를 안 받는것을 가정한다면...
  //$a="!";
  //echo preg_match("/[^!]/", $a); // !가 있으니깐 false 그 다음에 맞춰서 로직을 짜면 될 듯 예를들어 출력을 "사용해선안되는 어쩌구쩌구 이런식으로..."
  //** ^의 의미는 Start of line 

  //echo preg_match("/[a-z]/", $string); // a부터 z 까지 들어가 있으면 true Lowercase // "/[A-Z]/"는 uppercase
  //echo preg_match("/[a-zA-Z]/", $string); // 범위로 지정하기 소문자대문자 포함
  //echo preg_match("/[0-9]/", $string); // 숫자 포함
  //echo preg_match("/D*/", $string); // D로 시작하는 * 멀티플 단어 
  //echo preg_match_all("/D*/", $string, $array); // preg_match_all()는 배열로 리턴/ D를 포함게 문자가 몇개나 있을??
  //모든 단어를 일일이 찾아서 배열에 넣어서 [0]는 아무것도 안들어가 있고 배열이 38개로 만들어짐 
  //echo preg_match_all("/D.*m/", $string, $array); // D로 시작하고 모든문자 포함(.)이지만 m으로 끝나기 전까지 멀티플 문자(*)
  //echo preg_match_all("/D.+/", $string, $array); //D로 시작하는 모든 문자열(.)이 끝날 때(+) 까지  
  
  $newString = "My 1name2 is Daniel, 1Daniel2 is ^my name";
  //echo preg_match_all("/1.*2/", $newString, $array); //한 배열안에 1로 시작하는 모든 문자열이 2로 끝나는것 한번에 들어감
  //echo preg_match_all("/1.*?2/", $newString, $array); // 1로시작하는 모든문자에서 2로 끝나는 
  //echo preg_match("/D{2}/", $newString); //D로 시작하는 연속으로 쓰여진것을 찾을 때 사용 in a row   
  // /D{2}/이면 D가 연속으로 2번 쓰인것을 찾는다는 의미 즉, DD 없으므로 false return

  //echo preg_match("/D{1,2}/", $newString); //{}안의 ,는 or의미 D로 시작하거나 DD로 연속으로 되거나 
  
  //preg_match_all("/\D{3}/", $newString, $array); // \백스래쉬는 검색기능으로 \D는 none digit으로 3글자 연속인 문자를 찾는것: true 
  // \D{3}의 의미는 연속된 숫자가 아닌 3글자 캐릭터를 찾는것 (스페이스도 포함)
  //  \s는 Character with white space   \S는 none space Character
  //  \d는 digit (number)   \D는 none digit (character)
  //  \w는 word         \W는 none word
  
  //preg_match_all("/\S{3}/", $newString, $array); //스페이스를 포함한 연속된 3개의 캐릭터
  //echo preg_match("/^M/", $newString); //M으로 시작하는 것
  //echo preg_match("/e$/", $newString); //e로 끝나는 것 
  
  echo preg_match("/^M.*e$/", $newString); // M으로 시작하는 .모든 문자열 e로 끝나기 전까지의 모든 문자 (*)여러번 포함
  
  //echo preg_match_all("/\^.*e$/", $newString, $array); // 만약 문자열에 ^로 시작한다면 true 리턴 \(백슬러쉬)는 search의미
  
  
  //print_r($array);
  preg_match('/^[가-힣]{3,12}$/', $newString) 
  //한글만 허용[가-힣]{3,12} 한글은 1글자당 3바이트 
    //여기서 {3은 1글자 부터 12는 4글자까지 검사를 의미} 4글자 까지는 true, 5글자 부터는 false retrun //한글만 허용[가-힣]{3} 한글은 1글자당 3바이트 
    //여기서 {12는 4글자 검사를 의미} 4글자 까지는 true, 5글자 부터는 false retrun   
    //중괄호 사용예  {3} 한글자 , {3,} 한글자 이상, {3,12} 1글자~4글자

/* 각각의 의미들.. 
    Simple regex

Regex quick reference
[abc]     A single character: a, b or c
[^abc]     Any single character but a, b, or c
[a-z]     Any single character in the range a-z
[a-zA-Z]     Any single character in the range a-z or A-Z
^     Start of line
$     End of line
\A     Start of string
\z     End of string
.     Any single character
\s     Any whitespace character
\S     Any non-whitespace character
\d     Any digit
\D     Any non-digit
\w     Any word character (letter, number, underscore)
\W     Any non-word character
\b     Any word boundary character
(...)     Capture everything enclosed
(a|b)     a or b
a?     Zero or one of a
a*     Zero or more of a
a+     One or more of a
a{3}     Exactly 3 of a
a{3,}     3 or more of a
a{3,6}     Between 3 and 6 of a

options: i case insensitive m make dot match newlines x ignore whitespace in regex o perform #{...} substitutions only once
*/
  ?>
</body>
</html>