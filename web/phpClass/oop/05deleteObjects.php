<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <?php 
  include 'includes/05.delete.inc.php';

  $object = new NewClass; // instantiated
  unset($object); //delete object
  echo $object->getProperty(); // access method 
  //*** unset을 했기 때문에 echo getProperty(); 에러가 발생 */
  //
  ?>
</body>
</html>