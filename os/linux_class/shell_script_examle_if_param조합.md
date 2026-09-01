ssh 접속하는 sheel script example   

test.sh 파일로 저장하고 파라미터로 ok를 넣어주면 실행 된다 

```sh
#!/bin/sh
param1=$1
comparison="ok"

echo "user name:"
read user
echo "ip address:"
read ip

if [ -z $param1 ]  #null check
then
    echo "check paramete [usage]: sh test.sh ok"
else
    if [ $param1 = $comparison ]
    then
        echo "`ssh $user@$ip`"
    else
        exec pwd
    fi
fi

```
