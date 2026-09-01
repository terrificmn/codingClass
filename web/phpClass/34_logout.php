<?php
session_start();

session_unset();
session_destroy();

header("Location: 34_profile_upload.php");
?>