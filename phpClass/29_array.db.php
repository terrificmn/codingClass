<?php
include_once "includes/dbh.inc.php";
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>

<?php
$sql = "SELECT * FROM data";
$result = mysqli_query($conn, $sql);
$datas = array();
if(mysqli_num_rows($result) > 0) { //쿼리로 받아온 결과에 데이터가 하나라도 있다면 true
  while($row = mysqli_fetch_assoc($result)) {
    $datas[] = $row;  //datas 배열에 array()로 배열이 더 들어가지게 된다
  }
}

/*
print_r($datas);  //변수 형태랑 value값이 보여진다 결과 값: Array([0] => Array([id]=>1[text]=>Hi) .....

결과는 multi-dimesional array 다차원배열 2차원배열 
배열 0 에 또 배열 array [id] value, [text] value
배열 1 에 또 배열 array [id] value, [text] value
배열 2 에 또 배열 array [id] value, [text] value 
.... 이런식으로..
*/

/*
foreach ($datas as $data) { //이런식으로 하면 datas에 있는 첫번째 배열에 있는 내용은 2번째 배열만 가지고 있음
  echo $data;
}
*/

// foreach파라미터는 첫번째는 가져올 원래 변수, 두번째는 새로운 변수로 컬럼 데이터를 넣어주게 된다
foreach ($datas[0] as $data) {  // 첫번째 배열에서 가지고 있는 값만 보여줌 
  print_r($data);
  //echo $data;  // [0]에는 [id]와 [text] 2개가 또 배열로 들어가져 있어서 출력은 1Hi로 나오게 된다
}

echo "<br>";

foreach ($datas as $data) {  
   echo $data['text']." ";  //[text]배열에 있는것을 보여주게 됨 (즉,text 컬럼)
}

?>

</body>
</html>
