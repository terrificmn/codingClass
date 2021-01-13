<?php
    $a = 1;
    $b = 5;

    if ($a === $b) {
        echo "They are the same!";
    }
    elseif ($b === 5) {
        echo "Variable 'b' is equal to 5";  //elseif is true, then exit 
    }
    else {
        echo "They are NOT the same!";
    }


    $a = 50;

    switch ($a) {  //variable $a is condition
        case 25:   // this is the value we check for
            echo "Variable is equal to 25!";
        break;  //**always end each statement with a "break"
        case 50:
            echo "Variable is equal to 50!";
        break;
        default:  /// the same as a "else" (if statement)
            echo "None were true!";
        break;
    }  

    // variable has one value, then switch statement is good to use
    // much complex condition, then if, elseif, else statement are good to use
?>