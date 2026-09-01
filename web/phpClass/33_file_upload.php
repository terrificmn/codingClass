<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <form action="33_uploadAction.php" method="POST" enctype="multipart/form-data">
  <!-- "enctype" specifies how the form data should be encoded. 
    multipart/form-data 는 image file, text file all kinds of files avalable
    mdn에서 찾아볼 것 -->
    <input type="file" name="file">
    <button type="submit" name="submit">UPLOAD</button>



  </form>
</body>
</html>