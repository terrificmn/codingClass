<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hashing</title>
</head>
<body>
<?php
/*
echo "test123";
echo "<br>";
echo password_hash("test123", PASSWORD_DEFAULT); //BCRYPT hashing algorithm (디폴트)
// 파타미터 2개, 1첫번째는 바꾸려는 data, 2번째는 암호화 방식인데 PASSWORD_DEFAULT로 하면됨
//password를 바꾼다 (hashing) 암호화랑 비슷한듯
// echo 결과값
// test123
// $2y$10$azuj/QAwLl2Dj4K9ICTVqeTGqn6a0iGnmtBg5H8obWJ0iYIpOVg.u 
// DB의 패스워드 컬럼을 varchar를 최소한 60 해야함!
*/

$input = "test123"; //인풋으로 받은 암호
$hashedPwdIndb = password_hash("test123", PASSWORD_DEFAULT); //DB에 hashing 해서 넣을 값을 암호화해줌

echo password_verify($input, $hashedPwdIndb); //2개의 파라미터: 원본과 hashed data
// 2개를 비교해서 2개가 맞는다면 1 리턴(true)
// 로그인 시스템에서 이런식으로 서로 비교해서 처리할 수 있게한다

//**참고
// 암호화가 되면 원래 어떤 데이터 였는지 알지못하고 de-hash로만 비교해서 맞춰볼 수만 있다. 암호가 뭐였는지는 모름
// You won't be able to see the password once we de-hash it because it is designed to be
// as safe as possible. This means that even you as the website owner should not be able to read
// other users passwords.


?>
</body>
</html>
