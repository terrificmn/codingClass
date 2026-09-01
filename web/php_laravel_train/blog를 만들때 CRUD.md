Create - post 리퀘스트
/blog/create 
메소드 store


Read - get 리퀘스트
/blog
메소드 index


Update - post 리퀘스트
/blog/{slug}
or
/blog/{id}
메소드 put or patch


Delete
/blog/{slug}
or
/blog/{id}
메소드 delete


Show - get 리퀘스트
/blog/{id}

Edit  - get 리퀘스트
/blog/{id}/edit


___

CRUD application

**C**reate
**R**ead
**U**pdate
**D**elete

php에서는 이것을 resource로 컨트롤 할 수 있다

php artisan make:controller PostController --resource

위와 같이 하면 
auto create methods such as index, show, .. and destory
php artisan make:controller CarsController --resource
