<?php
spl_autoload_register('myAutoLoader');

/* 기본적으로 파일경로를 최상위 디렉토리에서 클래스를 사용하면 문제없겠지만 다른 sub 디렉토리에서 사용하면 문제가 발생하 것이므로 
function myAutoLoader($className) { 
  
  $path = "classes/"; // directory name
  $extension = ".cls.php";
  $fullPath = $path. $className. $extension;
  
  // error handler
  if (!file_exists($fullPath)) { //file_exists 함수는 file이 있는지 확인해 준다
    return false;
  }
  
  include_once $fullPath; //파일이름으로 해당 클래스 이름을 가진 클래스파일을 include해주기 
  //(단, 클래스명도 대소문자 지키면서 클래스 이름으로만 작성: 예- Person.cls.php)
}

// autoloader.inc.php 파일을 만들어서 다른 파일에서 include 해서 사용할 수 있게 하는 것
// 여기에 class가 정의된 php file을 include할 수도 있겠지만 그러면 클래스가 추가 될 때마다 계속 이 페이지를 수정해야겠지만
// function으로 만들었기 때문에 클래스를 오브젝트로 생성할 때 자동으로 autoload가 될 수 있게 해준다
// 참고***: class 사용할 때도 그렇지만 file명도 클래스 이름만 써줘야지 작동하고 대소문자 구별함
*/

function myAutoLoader ($className) {
  $url = $_SERVER['HTTP_HOST'].$_SERVER['REQUEST_URI'];

  if (strpos($url, 'includes') !== false) {
    $path = '../classes/'; //상위 디렉토리로 변경
  } else {
      $path = 'classes/';
  }
  $extension = ".cls.php";
  require_once $path. $className. $extension;
}