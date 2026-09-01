<?php
    //include 'test.php';  //links to the file
        // the same location: only file name
        // different location: 'directory name/test.php'
        // include statement doesn't fail but warn a msg if there's no file.
        // it doesn't stop running website
    //include_once 'test.php';
        // if test.php has included once somewhere, then it's not going to include the file
         
    //require 'test.php';
        //test.php file require (alike "include statement")
        // if file is missing or has a problem, then whole site fail so. uses something important
        // it's gonna stop the website.
    //require_once 'test.php';
        // it's the same fashion of include_once
        // check if test.php file already includes
    ?>
<!DOCTYPE Html>
<html lang="en">
    <head>
        <meta charset="uft-8">
        <title>include</title>
    </head>
    <body>
        <?php
            include 'test.php';
            echo $a;
        ?>
    <body>
</html>