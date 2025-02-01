# shell script rm result 받기
쉘 스크립트로 rm을 실행한 후에 처리된 결과를 받아보는 것 중에 가장 간단한 것이
`echo $?` 로 할 수 있는데, 문제가 있으면 1을 반환한다 

rm 뿐만이 아니라 다른 일반적인 명령어도 적용이 가능하다.  

> 여기서 문제가 발생한 경우는 파일이 없거나 permission 에러 발생 시

예를 들어 
```sh
#!/bin/sh
sudo rm ${HOME}/myfile
echo $?
```
만약 파일이 없으면 *1*을 출력 해준다



이를 활용해서 if로 사용해 볼 수가 있다
```sh
#!/bin/sh
sudo rm ${HOME}/myfile

if [ $? = 0 ]  
then
    echo "deleted"
else 
    echo "not deleted"
fi
```

> 주의 할 점은 $?을 echo로 출력하게 되면 if문이 성립이 안되는 듯 하다.   
테스트 할 때에는 echo $?로 확인하고, 실제로는 if문 사용해야하는 듯 하다

한계점은 rm -i 등으로 y/n 을 물어보게 되면 n을 해도 결과는 0 이게 되는 문제는 있다.  

즉 정상적인 경우에는 0을 리턴, 에러가 발생한 경우에 1을 리턴해서 그렇다

