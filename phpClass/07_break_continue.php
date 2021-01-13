<?php
    $a = 1;
// - Break statement
    while ($a++) {
        echo $a;   //$a keeps +1 and this means infinite loops --- this is a kind of dangerous loop which I should avoid to
        while ($a >= 10)    {
            break 2;  // break "while statement" upper lever 2
            //*** */ if write a code "break;" ----> it effects only one inside the while statement

        }
    }


// - Continue statement
echo "<br>";

$a = 1;
    while ($a < 10) {
        $a++;
        if ($a === 5) {
            continue; /// continue statement will skip the loop
            // $a reaches 5, then skip the one loop
        }
        echo $a;  // result will be 234678920.
    }