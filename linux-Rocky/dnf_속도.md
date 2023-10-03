# dnf 속도 
다운속도가 느릴 경우에 몇가지 추가해준다  

`/etc/dnf/dnf.conf` 파일을 열어서 추가   

> sudo 를 해준다

```
fastestmirror=true
deltarpm=true
max_parallel_downloads=10
```