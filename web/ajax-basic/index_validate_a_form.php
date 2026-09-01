<?php

    if (isset($_POST['submit'])) {
        $name = $_POST['name'];
        $email = $_POST['email'];
        #... 이런식으로 만들어준다

        $errorEmpty = false;
        $errorEmail = false;

        if (empty($name) || empty($email)) {
            echo "<span class="form-error">Fill in all fields!</span>"; // 여기에서 css class는 미리 만들어진 클래스(css파일 따로 있음)
            $errorEmpty = true; //자바스트립트에서 사용할 변수

        } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            echo "<span class="form-error">Write a valid e-mail address</span>"; 
            $errorEmail = true; //자바스트립트에서 사용할 변수
            
        } else { //에러가 없을 때
            echo "<span class='form-success'>good </span>";
        }

    } else {
        echo "There was an error!";
    }
?>


<!-- 이제 자바 스트립트에서 처리를 해준다 -->
위의 php를 통해서 만든 errorEmpty, erroEmail 변수들을 넘겨받아서 클래스를 바꿔준다
    <script>
    $("#comemnt-name, #comment-email").removeClass("input-error"); //class가 적용되었다면 삭제해준다
    
    var errorEmpty = "<?php echo $errorEmpty; ?>"; //php의 코드가 들어간다 
    var errorEmail = "<?php echo $errorEmail; ?>";

    if (errorEmpty == true) {
        $("#comemnt-name, #comment-email").addClass("input-error");  //css 클래스를 추가해줘서 css로 색이 바뀔 수 있게 해준다

    } 
    if (errorEmail == true) {
        $("#comment-email").addClass("input-error");
    }
    if (errorEmpty == false && errorEmail == false ) { //에러가 없을 경우 내용을 지워준다
        $("#comemnt-name, #comment-email").val("");   // val("") 빈 문자열로 만들면 내용이 없어진다. $셀렉터를 이용해서 모든 input을 선택해주면됨
    }

    </script>

