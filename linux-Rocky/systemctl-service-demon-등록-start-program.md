# systemctl 에 service 등록
service를 등록해서 rc.local 과 같은 시작프로그램을 등록할 수가 있다.   
> 사실 rc.local 등의 서비스는 나온지 몇 10년은 되었다고 한다. 


어쨋든 비슷한 구조이기는 하다.  
아직 본격적인 테스트는 못해 봤지만,  일단 

```
[Service]
Type=forking
ExecStart=/path/to/shell_script start
```

여기에서 type simple, forking 있는데, simple는 foregraound로 실행을 해서  
보통 쉘 스크립트를 테스트 하기 위해서 직접 쉘스크립트를 실행해도 문제 없이 잘 되고   
막상 systemctl 로 서비스를 시작하려고 하면 background에서 작동하기 때문에 실패되는 경우가 있다.  
이를 참고해서 백그라운드에서 돌아가게 하려면 Type을 forking으로 해준다.   


`ExecStart` 라는 파라미터를 통해서 start 명령어를 실행하는데   
사실 rc.local에서는 쉡 스크립트에 딱히 파라미터를 받지 않아도 문제가 없다   

하지만 여기에서 쉡 스크립트에 문자열 파라미터를 넘겨주는 경우인데   
이를 활용해서  

`ExecStop=`, `ExecRestart=` 등을 만들어 볼 수가 있고   
실행할 스크립트에 문자열로 stop, restart 등을 넘겨주게 만들면 된다.   

예를 들어 
```
[Service]
... 생략...
ExecStart=/path/to/shell_script start
ExecStop=/path/to/shell_script stop
ExecRestart=/path/to/shell_script restart
```

이제 실제 실행할 스크립트에서 문자열 파라미터를 받고 `./shell_script start` 이런식의 실행이 된다.   
이제 쉡 스크립트에서 파라미터를 받아서 case 형태나 if문으로 처리해주면 된다.   

쉡스크립트 파라미터 다룬 부분의 문법을 확인하자..;; 기억안남 %1 인가? 했던거 같다 ㅋㅋㅋ



## 그 밖에 

root로 실행하거나 user로 실행하는 것에 따라서 해당 패스를 잘 못받아 올 수 있으므로  
잘 확인해서 테스트 한다.  

> root 로 실행하게 되면 $HOME 따위의 변수를 사용하게 되면 /root 디렉토리를 찾기 때문에 주의


///TODO: 실제 테스트는 못해봤지만 간략한 정보 업데이트 해봄,   큰 틀에서는 rc.lcoal 서비스 등록과 비슷한 듯 하다.

