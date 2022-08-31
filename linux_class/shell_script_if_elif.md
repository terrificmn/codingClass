# sh shell script if - else if문 

sh 에서는 elif 로 해주고 then 을 사용해주면 됨

```sh
#!/bin/sh
# parameter
robot=$1  
# comparison
comp="v1"
#echo $robot
if [ -z $robot ]  #null check
then 
	echo "do when a parameter is null"
else
	if [ $robot = $comp ]
	then 
		echo "do something"
			elif [ $robot = "p1" ]
			then
				echo "do something"
			elif [ $robot = "p2" ]
			then
				echo "do something"
	else
		echo "do other thing"
	fi
fi
```