<?php
    include '17_header.php'; 
    // include_once 'header.php';

    // 헤더를 include 해서 (예: nav을 한번에 바꿀 때 편하다)
    // 또 다른 방법은 함수들을 모아 놓는 것
    // 예를 들어 functions/user-functions.php 이런식으로 함수만 모아 놓는것도 
    // 좋은 방법이 될 수 있어 보인다
    // 주의할 점은 이때는 include_once 'filename.php' 을 사용하는게 좋다
    // 왜냐하면 함수가 두번 링크되면 에러가 나기 떄문

?>

        <section>
            <h1>A title</h1>
            <p>some content</p>
        </section>
    
        <?php ///you can include <footer> too ?>
        
        <footer>
            <p>a footer</p>
        </footer>

    </body>
</html>
