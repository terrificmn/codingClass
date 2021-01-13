<?php

//***에러는 없고 잘 작동함.  terminal이용해서 $sudo mailq 해보면 sendmail통해 메일이 전송은 되나
// 접속이 거부된다 ㅋㅋ 
// /var/spool/mqueue 디렉토리에 보면 못간 메일이 쌓여만 있다 ㅋㅋ ㅜㅜ


if(isset($_POST['submit'])) {
  //$_POST로 input box에서 쓴 값을 받아오기
  $name = $_POST['name']; 
  $subject = $_POST['subject'];
  $mailFrom = $_POST['mail'];
  $message = $_POST['message'];

  $mailTo = "terrificmn@daum.net"; //**참고: php mail()함수는 senmail을 이용해서 내부메일서버의 smtp를 사용
  //외부 smpt를 사용하려면 예: 다음,네이버,지메일등.. 메일 라이브러리를 사용하면 된다고 함
  
  $txt = "You have received an email from ".$name.".\n\n".$message; //보기편하게 \n\n 2칸 newline
  $headers = "From: ".$mailFrom;

  mail($mailTo, $subject, $txt, $headers); //mail() needs 3 parameters: 1-email to, 2-subject, 3-actual message, 4-additional header
  header("Location: 37_send_email.php?emailsent");

}