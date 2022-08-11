# mac address 찾기  : Media Access Control (MAC)
우분투  
```
ip link show
```

이 중에  1. lo: loopback , 2: eth0 또는 eno1, enp 등으로 나올 수 있는데  
이 부분에 나오는 link/ether 부분을 보면 된다. 바로 mac주소

```
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: eno1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether brd ff:ff:ff:ff:ff:ff
    altname enp0s31f6

```

또는 cat 명령어로 확인하기 
```
cat /sys/class/net/eno1/address 
```

중간에 eno1 은 사용자 환경에 따라 달라질 수 있으므로 탭을 눌러서 확인을 하자   
결과로는 간단하게  mac address 만 출력한다 
```
04:3c:12:02:e4:12
```


## 위를 활용해서  cpp 에서 mac 어드레스 찾기
system() 함수를 사용하면 c++ 에서 command 관련해서 사용할 수가 있다  

```cpp
#include <stdlib.h>
```
꼭 안 넣어도 되기는 한다. 

char 포인터를 사용하거나 
```
char *cmd = "cat /sys/class/net/eno1/address";
std::system(cmd);
```

또는 string 사용~ 이때는 c_str()로 변환해서 넣어줘야한다 

```
std::string cmd = "cat /sys/class/net/eno1/address";
std::system(cmd.c_str());
```

하지만 system() 실행만 해줄뿐, 리턴값이 0이다.  (성공했다는 것만 알 수 있음)   


그래서 ropen 함수를 사용해서 file로 열어서 값을 저장시킬 수 있다  
예
```cpp
    std::string get_mac_cmd = "cat /sys/class/net/eno1/address";
    
    //출력
    std::system(get_mac_cmd.c_str());

    FILE *fp;
    char var[20];

    fp = popen(get_mac_cmd.c_str(), "r");
    while (fgets(var, sizeof(var), fp) != NULL) {
        // printf("%s", var);
    }
    pclose(fp);
    
    std::string result = var;
    return result;
```
위에서 system() 은 파라미터로 const char* 을 받기 때문에  
string 은 변환을 해줘야함  

popen으로 열어서 'r'은 읽기모드  

fgets()함수는 파라미터가 char *str, int n, FILE *stream 으로 각각 받는다  
파일 스트림 포인터fp에서 스트링 포인터에 (*str)에 저장시켜준다 (int n 의 -1 만큼 진행)

어쨋든 이렇게 되면 var에 저장이 되는데   
흠...

그리고 에러가 발생하면 NULL 포인터를 리턴한다. 그래서 while문은 NULL 아니면 진행  

point var를  를 넘기는것은 잘 안되서 string으로 넣어준다음에 리턴함  
(함수로 만들었을 때 넘기고 난 뒤에 받을 함수 호출한 쪽에서 제대로 안되서 ..ㅠ)


또 다른 방법으로는 system() 사용할 때 > 리다이렉트로 파일로 저장한 후에  
fstream 라이브러리를 통해서 File을 열어서 getline()으로 저장시키면 된다  

```
std::string = "li";
system((cmd) + ">" + "test");

  string line;
  ifstream myfile ("macaddress.txt");
  
  if(myfile.is_open()){
    while(getline(myfile,line)){
      cout<<line<<endl;
    }
    myfile.close();
```