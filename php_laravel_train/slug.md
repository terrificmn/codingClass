# slug
왜 슬러그를 사용할까라는 의문에...

보통 db 테이블에 id, title, text 라는 컬럼이 있다면
글들을 각각 title과 text로 받은 후에 db에 입력을 하고나서
글을 id를 통해서 (primary key)이면서 unique 속성을 가지고 있으므로 
id로 글을 가지고 오면 그에 해당하는 title, text를 볼 수 있는데

슬러그는 타이틀의 띄어쓰기는 -(하이픈)를 넣어서 만들어 주고, 특수기호는 없애고 변환시키는 방법이다

일단 slug라는 컬럼이 필요하고
그래서 예를 들어 이런글을 title에 올린다고 하면
a person or thing that is being discussed!!!
slug 컬럼에는 a-person-or-thing-that-is-being-discussed 로 들어가게 되는 것인데

라라벨에서는 Str::slug($request->title) 식으로 만들 수 있다
그리고 나서 화면에 출력을 할때 slug컬럼을 이용해서 db에서 데이터를 가지고 오고 
그 데이터를 바탕으로 title 및 text를 보여줄 수가 있게 됨

그래서 왜?
이뉴는 첫 째는 URL에 친화적인? 형태를 띄고, 특수기호등이 다 빠진다
정확히는 SEO friendly라고 한다.
둘째는 id를 url에서 안나오게 할 수 있다. 일단 id자체는 unique 건데 이거를 노출 시키는 거보다 
slug를 노출시키게 되면 진짜 타이틀(띄어쓰기 및 특수기호등이 들어가 있음) 및 id를 알 수 없게 되므로
셋째는 slug 변환된 자체도 유니크하게 되어서 포스팅을 보여주기에 무리가 없다 (혹시 중복은? 이거는 잘 모르겠다 ㅋ)

> SEO friendly란? Making a website SEO-friendly means that Google and other search engines can crawl each page on the website efficiently, interpret the content effectively, and index it in their database. Once indexed, they can then serve the most relevant and valuable web pages to their users based on the topics they search for.