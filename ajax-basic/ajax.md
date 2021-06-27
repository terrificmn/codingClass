데이터 베이스 테이블이 필요하므로 하나 만들어 준다
```sql
create table comments (
    id int(11) not null auto_increment primary key,
    author text not null,
    message text not null
);
```

아무런 데이터나 insert를 해줘야한다

그 다음에 php코드로 DB와 데이터베이스를 연결을 해줘야한다

그리고 나서 ajax를 사용할 페이지에서 
jquery cdn 버전을 넣어주고
```
<script src="https://code.jquery.com/jquery-3.6.0.min.js"
        integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4="
        crossorigin="anonymous">
</script>
```

그리고 다시 스크립 태그에서 써주면 된다

```jquery
<script>
    $(document).ready(functon() {
        var commentCount = 2;
        $("button").click(function() {
            commentCount = commentCount + 2;  // click이 될 때 마다 +2를 시켜준다
            $("#comments").load("load-comments.php", {
                commentNewCount: commentCount
            });
        })
    })
```
먼저 위의 코드를 포함한 메인페이지에서는 먼저 php로 db를 연결해서 LIMIT를 쿼리에 걸어서 
몇개만 보여주게 만들어준다 

그리고 위의 방식은 post방식으로 넘어 가므로 
php에서 데이터베이스에 연결 한 후 jquery에서 넘겨주는 commentCount라는 변수를 받아서 
쿼리에서 사용하면 된다. 

위의 load() 함수 같은 경우에는 load-comments.php 을 열어주는데 
이때 load-comments.php 파일에서는 db를 연결해주고 comentCount를 받아서 사용하게 되면 된다

예를 들면
```php
include 'dbh.php';

$commentNewCount = $_POST['commentNewCount']; //jquery에서 넘어온 데이터 

$sql = "SELECT * FROM comments LIMIT $commentNewCount";

$result = mysqli_query($conn, $sql);
if (mysqli_num_rows($result) > 0) {
    while ($row = mysqli_fetch_assoc($result)) {
        echo "<p>";
        echo $row['author'];
        echo "<br>";
        echo $row['message'];
        echo "</p>";
    }
} else {
    echo "There are no comments!";
}
```

위의 코드 같은 방식으로 짜 주면 된다

그러면 메인페이지에서 클릭 버튼을 누를 때마다 
새로고침이 없이 ajax 방식으로 2개의 커멘트가 계속 만들어지는 것을 볼 수 있다.

