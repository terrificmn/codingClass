# artisan 커맨드
artisan 커맨드를 Controller class 부터 migration까지 할 수 있는 커맨드를 정리해보았다.


## controller 클래스

```
docker compose run --rm artisan make:controller CarsController이름 --resource
```

뒤에 --resource 옵션은 기본 메소드를 다 만들어준다.

> 모두 특정 경로에 직접 파일을 만들 수도 있다.



## 모델 및 migration 파일 같이 만들기

모델 과 migration 파일 같이 만들기
```
docker compose run --rm artisan make:model Api -m
```

Api  대신 원하는 이름을 넣어준다. 준다.

[마이그레이션.md 파일을 참고한다.](./마이그레이션.md)




