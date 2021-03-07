컨트롤러 request를 받아서 처리 
필요한 데이터를 DB로 부터 받음 
Eloquent Model 

그 다음에 컨트롤러는 뷰에게 정보를 전달

예를 들면 사용자는 뭔가 페이지를 클릭하거나 URL를 브라우저에
입력했을 때 

컨트롤러가 예를 들어 PizzaController.php 가 
모델로부터 (DB)로 필요한 정보를 받아온다
그리고 뷰에게 전달
Pizza.blade.php 라는 html, css, javascript 만들어서
사용자에게 보여줌


참고 Controller의 기본 7가지 Actions
https://laravel.com/docs/8.x/controllers#actions-handled-by-resource-controller