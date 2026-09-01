<?php
$i = 837;
//var_dump()---displays structured information 1 or more expressions that includes its type and value
var_dump(is_int($i));  //is_int() check if it's integer

$f = 100.67;
var_dump(is_int($f));  //return false 'cause it is float
var_dump(is_float($f)); //return true 

$i = 6473581250;
echo number_format($i); // it changes into numbers with comma(,) in the k,m (thousand, milliion,..etc..)

$test1 = '12345';
$test2 = 12345;
echo "\n";


// using function with numbers
if (is_int($test1)) {
  echo '$test1 is an Integer' . "\n";  //\n new line (only see through terminal)
} elseif (is_string($test1)) {
    echo '$test1 is a String' . "\n";
}

if (is_int($test2)) {
  echo '$test2 is an Integer';
}  
