<?php
if (isset($_POST['submit'])) {
  $newFileName = $_POST['filename'];

  if (empty($newFileName)) { //if there's no input from filename input box, then it sets gallery as default
    $newFileName = "gallery";
  } else {  // filename이 엠티가 아니면 소문자로 만들어주고 스페이스가 있다면 -(대쉬)로 바꿔준다 --나중에 작업하기 편해진다
    $newFileName = strtolower(str_replace(" ", "-", $newFileName));
  }

  $imageTitle = $_POST['filetitle'];
  $imageDesc = $_POST['filedesc'];
  
  $file = $_FILES['file'];

  //print_r($file); // $_FILES[]; super global로 받아온 변수 file의 배열 상태를 볼 수 있다
  //Associative arrays을 이용해서 변수 할당
  $fileName = $file['name'];
  $fileType = $file['type'];
  $fileTempName = $file['tmp_name'];
  $fileError = $file['error'];
  $fileSize = $file['size'];

  $fileExt = explode(".", $fileName); // .이후로 확장자를 구분해서 확장자만 저장, explode()fn.은 배열로 나눠어서 됨
  $fileActualExt = strtolower(end($fileExt)); //end() 함수는 배열의 마지막을 구분해줌 $fileExt는 0,1로 되어있는데 거기서 마지막 배열 

  $allowed = array("jpg", "jpeg", "png");

  if (in_array($fileActualExt, $allowed)) { //in_array() fn.은 배열을 체크: param1은 찾을문자열, param2는 배열(이중에서 찾음)
    if ($fileError === 0) { //file 에러가 있는지 확인 0이면 에러가 없는 것
      if ($fileSize < 2000000) { //file size check
          //** 파일저장 코딩시작 */
          $imageFullName = $newFileName . "." .uniqid("", true)."." .$fileActualExt; 
          // db에서 파일이름이 겹치는것을 방지하기 위해서 파일네임 뒤에 uniqid()로 랜덤문자열을 더해주고 마지막으로 실제 확장자로 만들어준다
          //uniqid() fn.은 첫번째 파라미터는 prefix인데,""면 없는것이고, 2번째 파라미터는 true면 더 많으 랜덤 문자열을 만든다 ().찍고 더 만듬)
          //에: reach라는 파일명으로 업로드 하면 reach.5fbbcf24c99939.02087304.png 이렇게 만들어짐
          $fileDestination = '../uploads/gallery/'.$imageFullName; //현재 includes디렉토리 안 이므로 한번 상위디렉토리로 올라가야함
          
          include_once "dbh.inc.php";

          if (empty($imageTitle) || empty($imageDesc)) { //로직은 에러 먼저처리하는게 좋다고 함
            header("Location: ../41_gallery.php?upload=empty");
            exit(); //script exit
          } else {
            $sql = "SELECT * FROM gallery;";
            $stmt = mysqli_stmt_init($conn); //24_Explain_PrepareSTMT.php와 25_PreparesSTMT.php 참고
            if (!mysqli_stmt_prepare($stmt, $sql)) {
              echo "SQL statement failed!";
            } else { //sql 실행
              mysqli_stmt_execute($stmt);
              $result = mysqli_stmt_get_result($stmt);
              $rowCount = mysqli_num_rows($result);
              $setImageOrder = $rowCount + 1;  //db에서 다음row를 값을 보기 위해서 1을 더해준다(인덱스가 1이 추가되니 다음 인텍스가 됨)

              $sql = "INSERT INTO gallery (titleGallery, descGallery, imgFullNameGallery, orderGallery) VALUES (?, ?, ?, ?);";
              if (!mysqli_stmt_prepare($stmt, $sql)) { //위에서 mysqli_stmt_init()fn.으로 initualize했기 때문에 바로 mysqli_stmt_prepare()사용할 수 있다
                echo "SQL statement failed!";
              } else {
                // 실제 db에서 INSERT query 실행
                mysqli_stmt_bind_param($stmt, "ssss", $imageTitle, $imageDesc, $imageFullName, $setImageOrder); //위의 sql에서 VALUES 중에서 ?,?,?,? 4개의 물음표를 대체해서 사용할 수 있다
                mysqli_stmt_execute($stmt);

                move_uploaded_file($fileTempName, $fileDestination); //서버에 파일 저장 (정확히는 템프로 업로드 된것을 이동시킴)
                //첫번째 파라: 템프이름, 2번째 파라:저장 위치

                header("Location: ../41_gallery.php");
              }

            }
          }



        } else {
          echo "File size is too big!";
        }
      
    } else {
      echo "You had an error!";
    }
  } else {
    echo "You need to upload a proper file type!";
    exit();
  }


}
