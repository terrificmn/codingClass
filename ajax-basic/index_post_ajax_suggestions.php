<?php
    $existingNames = array("Daniel", "Dennis", "Danny", "Jane");

    if (isset($_POST['suggestion'])) {
        $name = $_POST['suggestion']; //jquery로 넘어온 두 번째 파라미터 suggestion

        if (!empty($name)) {
            foreach ($existingNames as $existingName ) { //array 수 만큼 반복
                if (strpos($existingName, $name) !== false) {
                    echo $existingName;
                    echo "<br>";
                }
            }

        }
        
    }