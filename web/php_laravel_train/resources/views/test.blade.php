<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    테스트
    
    <?php 
    #echo $name;

    # 위처럼 그냥 실행하면 url에서 get방식으로 넘어온 것을 그대로 처리해줌
    # 자바 스크립트 실행됨
    #만약 사용자가 url에서 <script>alert('hello');</script> 직접 넣으면 자바스크립트 실행됨
    #$name 을 출력해주기전에 이스케이프를 시켜야함 전통적 방법
    #htmlspecialchars($name, ENT_QUOTES);

    #라라벨에서는 컬리 브라겟을 두번씩 감싸준다 {{ }} php코드로 작성하면 안됨 
    # 그냥 html로 작성
    # 그래서 라라벨에서는 {{ }} 많이 사용하게 됨
    ?>

    <h2> ecscaped {{ $name }} </h2>
    
    <h3> not escaped {!! $name !!} </h3>
    <?php
    # 위와 같은 코드는 php가 해석하지 못함, 그래서 블레이드 엔진이 대신 처리해주는데
    # storage/framework/views 에 가보면
    # 파일들이 생성이 되어 있는데 그 중에 한 파일에서 컴파일이 된 파일
    # php코드로 작성이  php echo e($name); 되어 있는 것을 확인 할 수 있고 
    # e() function를 찾아가보면
    # 똑같이 이스케이프가 되어 있음
    ?>

</body>
</html>