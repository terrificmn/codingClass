# grep & sed

## grep
-q quiet 옵션 (결과를 출력하지 않는다.) 

예
```shell
grep -q "^amr_group:" /etc/group
```

바로 쉘 if 문에 사용할 수 있다. 

```shell
if grep -q "^amr_group:" /etc/group; then
    echo "found"
fi

```
결과를 파이프를 이용해서 grep 으로 넘겨 받아서 찾을 수도 있다. 

`id -Gn | grep -qw "amr_group";`

> id 의 Gn 옵션을 사용하면 그룹명만 나오게 된다. 


## grep 과 sed 연계
grep 에 -E 옵션은 정규식을 사용할 수 있음.   
> -E, --extended-regexp     PATTERNS are extended regular expressions  
-e, --regexp=PATTERNS     use PATTERNS for matching


예)  
문자열에서 [0-9]+ 0에서 9까지의 숫자를 하나 이상 되는 것을 고르기  (패턴)  
```
name="marker-01"   
robot_id=$(echo "$name" | grep -oE 'marker-[0-9]+')   
echo $robot_id
```

s : The substitute command. 를 이용해서 sed 를 사용할 수 있는데     
sed 는 패턴을 사용할 때 s/.../.../ 이런식으로 슬래쉬(/) 를 2개를 사용하게 되는데,    
첫번째 /.../ 는 패턴이고, 두 번째 /.../ 는 해당 내용을 바꾸라는 것   
즉, **`sed -E 's/search/replace/'`**   
단, 두 번째가 // 이면 empty 이므로 지우게 된다.  

echo "marker-01" | sed -E 's/marker-0*//'

asterisk(*) 는 숫자 바로 직전에 사용된 0 가 0 이거나 더 많을 경우까지 찾는다.  
아예 0 이 없다면 marker- 까지만 지우게 된다.   

> sed -E 옵션은 regular expression 을 사용할 수 있게 해줌   
> sed 는 The stream editor tool used to filter and transform text.

이 2개를 결합해서 | 로 넘겨서 진행을 하게 되면  

```
echo "marker-01" | grep -oE 'marker-[0-9]+' | sed -E 's/marker-0*//'
```

결국 숫자만 남게 된다.  
