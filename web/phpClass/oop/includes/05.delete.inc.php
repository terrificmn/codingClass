<?php
class NewClass {
  //Properties and Metheods goes here
  public $data = "I am a property.";
  public function __construct() {
    echo "This class has been instantiated. <br>";
  }

  public function setNewProperty($newdata) {
    $this->data = $newdata;
  }

  public function getProperty() {
    return $this->data;
  }

  public function __destruct() {
    echo "<br> This is the end of the class!";
  }

}