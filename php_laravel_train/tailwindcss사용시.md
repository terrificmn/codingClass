[참고:tailwindcss공식](https://tailwindcss.com/docs/guides/laravel)

테일윈드css는 
기본이 base 에 
일단 모든 태그들은 기능을 제거? 되어 있다 
예를 들어서 h1 h2 .. 태그 같은 것들도 크기가 나오지 않는다
이유는 기본 밑바탕이 없는 상태에서 내가 원하는 것만 스타일을 조절해 주면 되기 때문에 

대신에 @layer 라는 것을 이용해서 기본 base에 특정 태그들의 css를 정해줄 수 있다
(말 그대로 layered 되는 것 같음)

라라벨 기준
/resources/css/app.css

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  h1 {
    @apply text-2xl;
  }
  h2 {
    @apply text-xl;
  }
}
```

근데 바로 적용이 안된다. 아무래도 Laravel Mix를 해야하는 듯 하다
아직 정확하지 않다.. 잘 몰라서 ㅠ
일단 npm을 실행해서 컴파일을 해준다
```shell
$npm run watch
```
또는 npm run dev


아직까지 이해한바로는 현재는 h1태그정도나 스타일을 정해주고 싶은데 
그냥 페이지에서는 
`<h1 class="text-4xl text-blue-500">` 이런식으로 넣을 수 있기 때문에 
어떤게 좋을 지 테스트를 한 후에 app.css 파일에 최종적으로 수정한 후에 
laravel mix를 진행하면 될 듯하다

아니면 그냥 h1태그에 일일이 스타일을 주던가.. 
db에는 `<h1>`이라고만 들어가 있어서 코드를 짜줘야할 듯해서 괜히 복잡해지는 것 같아서;;
그럴 필요가 없을 듯 하다.. 02Apr 2021

특히 a 태그를 지정할 때는  hover:underline 이런 클랙스는 오류가 난다. 
직접 클래스를 지정할 때는 잘 되지만, @apply를 사용할 때는 에러가 남
그리고 a태그를 지정하게 되면 nav의 메뉴의 링크 표시도 바뀌게 되어서;; 결국 포기

<br/>


최종 완성이 되었다고 하면 
```shell
$npm run production
```

그러면 용량이 css용량이 예 (3mb 정도에서 4kb 정도로) 사이즈가 대폭 줄어든다
