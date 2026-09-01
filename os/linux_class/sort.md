# ls & sort

ls pipe 으로 연결하기, 날짜 순으로 정렬
```
ls -l --time-style=long-iso | sort -r -k 6,6
```

