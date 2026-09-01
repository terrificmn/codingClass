# header() 
```            
Warning: Cannot modify header information - headers already sent by (output started at /home/public_html/wp-config.php:#) in /home/public_html/wp-includes/file-example.php on line 33
```
이런식으로 발생할 때

첫 번째 해당 사항은 
header() 함수를 사용하기전에 echo()등의 함수를 사용한 경우에 위에 워닝이 발생하면서 페이지 이동이 안됨

그 외에는 <?php 의 시작 태그  ?>인 closing tag를 하기 전에 스페이스바가 있다던가,   
print, echo 함수가 먼저 사용되거나, 등..

이번 케이스는 echo를 빼 주면 해결된다   
```php
// echo $_POST['pass_wd'];
header("location: index.php");    
```
