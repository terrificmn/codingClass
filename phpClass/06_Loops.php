<?php 
    $a = 1;
    $b = 5;

    while ($a < $b) { //"while loops" will continue while condition is true
        echo "Keep looping this!<br>";
        $a++;
    }

    // while
    // do-while
    // for
    // foreach

    $a = 1;
    while ($a <= 10){
        echo "Loop number " . $a++;
    }

    $a = 1;
    do{   //* the difference between "while" and "do while" is that 
        //"do while" can execute one time if condition is false
        // but "while statement" can't be done if condition is false
        echo "Loop number " . $a++;
    } while ($a <= 10);


    for ($i = 0; $i < 10; $i++) {
        echo "This will loop 10 times!";
    }



    $array = ["Daniel", "Timmy", "Jane"];
/// foreach (loop as array 0,1,2 )
    foreach ($array as $value) {  // using with array
        echo $value;
    }

    $array = [
        "Name" => "Daniel",
        "Eyecolor" => "Blue",
        "Age" => "30"
    ];

    foreach ($array as $key => $value) { 
        echo $key . ": " . $value;
        // first loop = name: Daniel
        // second loop = Eyecolor: Blue
        // third loop = Age: 30
    }