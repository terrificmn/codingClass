<?php
session_start(); //세션을 먼저 스타트를 해주고
session_unset(); //session variable로 되어있던 것을 unset시킴
session_destroy(); //세션에 등록되어 있던 것을 말그대로 destroy시킴
header("Location: ../42_loginsystem.php");

//순수 php코드는 클로징 태그를 쓰지 않는다 