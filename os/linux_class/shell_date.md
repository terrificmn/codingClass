# date 명령어 사용

date를 사용해서 echo나 파일에 저장할 때 사용하면 좋다

man을 이용해서 `date --help` 를 사용하면 다양한 옵션에 대해서 나온다
```shell
day=$(date +"%F")
now=$(date +"%T")
```

> 여기서 주의할 점은 + 와 "%F" 꼭 붙여서 사용해야한다. **+"%F"**   


