<a>tag 마우스 class 
```css
class="hover:underline"
```


줄 간격 관련해서는 좌우는 px를 활용 (좌우 패딩)
```html
<li class='inline italic text-gray-600 px-2'>
```
그리고 inline tag가 자동으로 줄 바꿈되는 경우에 줄이 겹칠 때는
leading-클래스 이용

```html
<p class="leading-none ...">Lorem ipsum dolor sit amet ...</p>
<p class="leading-tight ...">Lorem ipsum dolor sit amet ...</p>
<p class="leading-snug ...">Lorem ipsum dolor sit amet ...</p>
<p class="leading-normal ...">Lorem ipsum dolor sit amet ...</p>
<p class="leading-relaxed ...">Lorem ipsum dolor sit amet ...</p>
<p class="leading-loose ...">Lorem ipsum dolor sit amet ...</p>
```

줄간격을 fix해주려면 숫자형태도 가능
```html
<p class="leading-3 ...">Lorem ipsum dolor sit amet ...</p>
<p class="leading-4 ...">Lorem ipsum dolor sit amet ...</p>
<p class="leading-5 ...">Lorem ipsum dolor sit amet ...</p>
```

