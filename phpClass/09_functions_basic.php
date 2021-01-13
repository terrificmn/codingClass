<?php
// how to call function 
// ex) echo personInfo("Daniel", 28); // 1st string parameter: "Daniel", 
// 2nd parameter: 28 integer

// Why we build our own functions:
// Reusable and easier to use
// Better optimization
// Load code before needing it.
// Easy to use.
// function will be loaded first. no matter where it is coded in the top of bottom

// - 1. Internal Function (built-in)
/// how to use it on google
$a = "Hello world!";
str_replace("world", "Daniel", $a);

//echo $a;

$a = "hi";
str_repeat($greeting, 3);


// usrer-defined functions
// function : first letter should start with regular letter
// then second word is good to start with capital letter
// e.g: calcAdd();
// do not name it as built-in function's name

function calcAdd($num1, $num2) {
  $value = $num1 + $num2;
  return $value;
}
// only available inside function
//recommendation:
// so call function, then echo out outside of function

echo calcAdd(2, 4); //like this

