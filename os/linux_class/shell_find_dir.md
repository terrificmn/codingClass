# dir 찾기

if 와 -d 옵션으로 사용한다 

```shell
if [ -d "/path" ]
    then
    echo "exists"
fi
```

반대로는 !를 해주면 된다
```shell
if [ ! -d "/path" ]
    then
    echo "not exist"
fi
```

심볼릭 링크는 -L 옵션으로 찾을 수 있다
```shell
if [ -L "/path" ]
```

없으면 자연스럽게 만들어주면된다

```shell
dir="${HOME}/my_dir"
if [ ! -d "$dir" ]
    then
     mkdir -p "$dir"
fi
```

이를 한 줄로도 가능한 듯 하다
```shell
dir="${HOME}/my_dir"
[ ! -d "$dir" ] && mkdir -p "$dir"
```

