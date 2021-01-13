<?php
    // --Assignment Operators 
    $num1 += $num2;
    // using += is the same as 
    $num1 = $num1 + $num2;
    // so just a shorthand.
  
    // --Comparison Oprators
    $num1 == $num2; // data type doens't matter
    $num1 === $num2; // data type should be the equal, too.

    $num1 != $num2;  // the same way above
    $num1 !== $num2;

    $num1 <=> $num2; // if two various is the same, result will be 0
    // if left is greater than right, then 1
    // if right is greater than left, then -1


    // --Logical Operators
    $num1 = 5; 
    $num2 = 10;
    $num1 === 5 and $num2 === 10; // both of them have to be true
    // shorthand
    $num1 === 5 && $num2 === 10;

    $num1 = 5;
    $num2 = 10;
    $num1 === 5 or $num2 === 6; // one of them is true, not both of them
    //shorthand
    $num1 === 5 || $num2 === 6;

    // tricky;;;
    $num1 = 5;
    $num2 = 10;
    $num1 === 5 xor $num2 === 6;  // if both of them is the same, then result be false
    // if one of them is true, then result will be true
    // if both of them are false, then this is going to return to be false

    $num1 = 5;
    !$num1 === 6; // 5 is $num1, so this is not true 
    // but ! in front of $num1, just need an opposite result
    // so overall statement will return as true 

    // --Increment/
    $num1 = 5;
    ++$num1; // will output 6 (adding number first, then echo out the number so 6)
    $num1++; // will output 5 (echo out first, then adding number)

    // --Decrement
    $num1 = 5;
    --$num1; // will output 4  (adding minuses first, so subtract one and then echo out)
    $num1--; // will output 5  (echo out first, then one minus)

    // --String Operator
    $a = "My name ";
    $b = "is Daniel!";
    $c = $a . $b;

    $a = "my name ";
    $b = $a . "is Daniel!";
?>