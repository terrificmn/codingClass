markdown은 간편하게 사용할 수 있게 만들어진 것이라 (html을 대체하는게 아니기 때문에)
색을 지정하는 것은 없다~

글자 색만 강조하고 싶다면~ span태그를 사용하면 된다
```html
<span style="color:yellow">(터틀봇3 없이 진행할 때)</span>
```

단, 깃허브에는 적용이 안된다


헤딩 # title 이런식으로 작성한 것은 페이지의 한 부분으로 점프해서 링크를 걸 수 가 있다
사용법은 보통 마크다운의 링크 작성법대로 하다가 #을 붙여주고 heading 내용을 적어주면 된다
중간의 빈 공간은 (스페이스) - 로 대신해서 적어준다
```
[여기를 눌러서 다음 내용 보기](#두-번째-내용-시작)

...
..
.생략...

# 두 번째 내용 시작
``` 

이거를 구현하면

[여기를 눌러서 다음 내용 보기](#두-번째-내용-시작)

내용1
내용2
내용3
내용4
내용5

# 두 번째 내용 시작

