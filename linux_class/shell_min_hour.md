test

```sh
#!/bin/bash
reserved_min=201
converted_hour=0
converted_min=0

let converted_hour=$reserved_min/60
let converted_min=$reserved_min%60

echo ${converted_hour} 
echo ${converted_min}

test_a=100
#result=0
let result=test_a/10
echo ${result}
let result=$test_a+100
echo $result
```