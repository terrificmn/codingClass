<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  

<?php
//http://example.com/article.php?id=11&name=HelloWorld&time=1134
//이런식으로 get방식으로 데이터를 url 넘겨주면서 사용할 수 있는데, url이 길어지고 데이터가 눈에 보이게 된다
//참고: 이페이지에서는 40_reduce_url.php?id=2&name=HelloWorld  이런식으로 테스트하면 됨

$articleId = $_GET['id'];
$articleName = $_GET['name'];

echo "Article ID is: ". $articleId;
echo "<br>";
echo "Article name is: ".$articleName;

/****중요 사용은 원래 /40_reduce_url.php?id=3&name=HelloWorld 이렇게 하나
/****
// 설정파일 현재 파일과 같은 경로에 (기본 최상위 디렉토리)
//파일을 하나 만든다: 이름은 없고 .htaccess 로 만들어 준다 (configuration file임)

//RewriteEngine on  //url을 다시 쓸수 있게 하는 것

//rewritecondition  // true이면 다음 코드를 수행
//RewriteCond %{REQUEST_FILENAME} !-d  (-d는 디렉토리, !-d는 url과 이름이 같은 디렉토리가(it does not have directory) 없는지 확인)
//주소에 /디렉터리를 확인  / 파일명이랑 디렉토리명이 같을 수가 있는데 파일명을 찾아야 하므로 디렉토리 이름이 같더라도 찾지 않게하기위함

//RewriteCond %{REQUEST_FILENAME}\.php -f  (-f는 filename을 의미)(\(백슬러쉬).php 파일이 있는지 확인)

// rule 정의 
/*
RewriteRule ^article/([0-9]+)/([0-9a-zA-Z_-]+) ariticle.php?id=$1&name=$2 [NC,L]
/([0-9]+)숫자만 허용, 여기서 +의 의미는 9까지가 아닌 10, 11 ,12..... 이상의 숫자 허용의 의미
/(슬러쉬)는 다음 regular expression, 
([0-9a-zA-Z_-]+) 는 숫자,소문자영문,대문자영문, (문자열사이의) _(언더스코어),-(대쉬) +는 more 캐릭터의미
article.php?id=$1&name=$2&time=$3 은 url에 get방식으로 데이터를 받을 주소/데이터 인데 $1,$2,$3은 placeholder로서 마치 변수처럼 사용됨
첫번째/(슬러쉬)이후 regular expression은 첫번째 id=$1에 대입되고, 
두번째/(슬러쉬)이후 regular expression은 name=$2에 대입된다
마지막 []는 더 많은 조건을 달고 싶을 때 
[]안의 NC는 stands for none case 이며, 대소문자 구별안하는 것, 이유는 php는 대소문자를 구별하지만 브라우저에서는 구별하지 않으므로
[]안의 L은 RewriteCondition으로 위에 2개를 정의해서 그게 RewriteRule에 적용되는데 
이후 다른 rule을 또 만든다면 위의 condition을 무시하게 된다.
*/
?>
<!--
  RewriteCond %{REQUEST_FILENAME]\.php -f     작동안함 
  RewriteCond %{REQUEST_FILENAME] !-f     이렇게 하니깐 작동함
  이유를 찾아야함

  -->

</body>
</html>

