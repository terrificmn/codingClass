<?php
/*
//array basic 데이터가 많을 때 사용하게 된다
$person = "Daniel";
$people = array("Daniel", "Jane", "John"); //변수에 여러개의 데이터를 넣을 때 array 사용
echo $people[0]; //0부터 시작 
*/

// **배열 입력하는 몇개의 방법 //
// insert data into array //
$data = array(); //empty array 
$data = array("first", "second"); //데이터 순서로 넣어주면 됨
$data[] = "Daniel"; //[]안에 숫자를 안 넣어도 데이터가 들어가짐
$data[] = 15;
array_push($data, "Daniel", 23);  //array_push()함수에는 변수, 차례차례 데이터1, 데이터2, 데이터3.. )

print_r($data); //변수의 정보를 보여줌: 변수에 어떤 value가 들어있는지 보여줌


?>