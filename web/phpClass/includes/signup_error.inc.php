<?php
//include_once 'dbh.inc.php';

if (isset($_POST['submit'])) {
  $first = $_POST['first'];
  $last = $_POST['last'];
  $email = $_POST['email'];
  $uid = $_POST['uid'];
  $pwd = $_POST['pwd'];

  // if문에서 실행하고 else 에서 에러 처리를 한다면  
  // 만약 if 로직 어딘가에서 잘못되어 있는데 실제 에러가 발생했다면 일단 실행이 되어지고 
  // 잘못된 값이 저장/처리 될 수 있으므로... 
  ///***중요: if문 true일때 에러 메세지나 에러 핸들링을 먼저 처리 해주는 습관이 중요하다
  // 그래서 에러나 나면 바로 빠져나갈 수 있게 하자 
    // check if inputs are empty
    
    if (empty($first) || empty($last) || empty($email) || empty($uid) || empty($pwd)) {
      //empty()는 제로가 아니고, 엠티가 아니면 false 리턴함 / 즉 엠티면 true 리턴
      header("Location: ../26_error.php?signup=empty"); //get 메세지로 남길 수 있다
      exit();  
      
    } else {
        //check if input characters are valid
        if (!preg_match("/^[a-zA-Z]*$/", $first) || !preg_match("/^[a-zA-Z]*$/", $last)) {
          //pre_match()함수 정규식을 이용해서 문자인지 확인한다. 대충 시작/^  끝$
          header("Location: ../26_error.php?signup=char");
          exit();
        } else {
            //check if email is valid
            if (!filter_var($email, FILTER_VALIDATE_EMAIL)) { //여기서도 에러가 먼저 일때를 처리 그래서 ! 
            //filter_var() php에서 제공하는 email validate를 쉽게 할 수 있다
            // url에 데이터값을 넘겨준다 
            header("Location: ../26_error.php?signup=invalidemail&first=$last&last=$last&uid=$uid");
            exit();
            } else {
              header("Location: ../26_error.php?signup=success");
              exit();
            }
        }
    }
}
?>