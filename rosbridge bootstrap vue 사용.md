CDN 방식으로 html의 head 태그에 넣어준다 

```html
<!-- CSS only -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
```

[부트스트랩 홈피에 가면https://getbootstrap.com/ package manager로 설치하거나 CDN으로 link해줄 수가 있다](https://getbootstrap.com/)


일단 참고만 하자~ 최신 버전으로는 아직 js 문법을 잘 모르겠다.. 추후 연구 필요
이번에는 VUE js를 CDN 방식으로 추가해준다. 마찬가지로 html의 head태그에 추가해준다  
```html
<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
```

[여기 vuejs 공식 페이지에서 사용방법 확인할 수 있다~https://vuejs.org/guide/quick-start.html](https://vuejs.org/guide/quick-start.html)

역시나 npm으로 설치가능하나~ 그냥 편하게 cdn으로 링크

**잠깐! 그래서 아래 방식으로 일단 사용**

현재 버전은 vue 버전은 3 이상이 나온 듯 하나, 스크립트는 vue 2.6 버전 기준인 듯 하다  
그래서 new Vue 를 했을 때 Vue는 contructor가 아니라고 에러가 발생한다. 아무래도 버전 업 되면서   
뭔가 많이 바뀐듯 하다 

결론은 2.6버전을 사용. 아래 내용을 html head 태그 안에 넣어주자
```html
<script src="https://cdn.jsdelivr.net/npm/vue@2.6.14/dist/vue.min.js"></script>
```


