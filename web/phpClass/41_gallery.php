<?php
$_SESSION['username'] = 'admin';
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="style.css">
  <title>Document</title>
</head>
<body>
  <main>
    <section class="gallery-links">
      <div class="wrapper">
        <h2>Gallery</h2>

      <div class="gallery-container">
        <?php
        include_once 'includes/dbh.inc.php';
        $sql = "SELECT * FROM gallery ORDER BY orderGallery DESC";
        $stmt = mysqli_stmt_init($conn);
        if (!mysqli_stmt_prepare($stmt, $sql)) {
          echo "SQL statement failed!";
        } else {
          mysqli_stmt_execute($stmt);
          $result = mysqli_stmt_get_result($stmt);

          while ($row = mysqli_fetch_assoc($result)) {
            //db에서 받아온 데이터를 넣어준다 사진은 <div>의 css style을 이용해서 넣어준다
            //style.css에서 gallery-container클래스 정의에서 background-color가 있다면 이를 빼줘야지 사진이 올바르게 나옴
            //Css파일을 수정하고도 새로고침 변화가 없을 때는 브라우저의 데이터를 지워준다 (cached web content)
            echo '<a href="#">
            <div style="background-image: url(uploads/gallery/'.$row['imgFullNameGallery'].');"></div>
            <h3>'.$row['titleGallery'].'</h3>
            <p>'.$row['descGallery'].'</p>
            </a>';
            
          }
        }
        
        ?>
      </div>
      
      <?php
      if (isset($_SESSION['username'])) {
        echo '<div class="gallery-upload">
          <form action="includes/gallery-upload.inc.php" method="POST" enctype="multipart/form-data">
            <input type="text" name="filename" placeholder="File name">
            <input type="text" name="filetitle" placeholder="Image title">
            <input type="text" name="filedesc" placeholder="Image description">
            <input type="file" name="file">
            <button type="submit" name="submit">UPLOAD</button>
          </form>
        </div>';
      }
      ?>
    </section>
  </main>
  
</body>
</html>