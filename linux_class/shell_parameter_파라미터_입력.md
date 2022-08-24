입력 받기는 read  

```sh
#!/bin/sh
echo "입력하세요"
read input
echo $input
```

파라미터는 $1 로 받는다. 순서대로 받음

```sh
#!/bin/bash
param1=$1
param2=$2
echo $param1
echo $param2
```
파일명을 test.sh 라고 저장하고 실행을 파라미터를 넣어서 실행을 해본다 
```
sh test.sh 10 20
sh test.sh hello world
```
