# WARNING: amdgpu dkms failed for running kernel

GPU를 머신러닝에 이용하기 위해서 삽질;; 역대급 삽질이었다;;    
amdgpu-pro 드라이버를 설치하다보면 에러 워닝이 발생하는데..   
뭐.. 사실 warning이면 돌아가는데 문제가 없어야하는거 아닌가? 했지만..  
정작 중요한 기능이 안되니 warning이 맞긴 한가보다.. 화면이 안나오는거는 아니니깐..  

드라이버 설치 중에 원격 리파지터리에서 다운을 받고 설치를 진행하는데   
설치하는 의존성 패키지들이 많아서 잘 모르고 넘어갈 수 있다.  

```
amdgpu-dkms-1:5.9.20.104-1247438.el8.noarch
Complete!
WARNING: amdgpu dkms failed for running kernel
```


에러 로그를 찾아보자
vi /var/lib/dkms/amdgpu/5.9.20.104-1247438.el8/build/make.log
  /var/lib/dkms/amdgpu/5.9.20.104-1247438.el8/build/Makefile:26: "Local GCC version 80404 does not match kernel compiler GCC version 80401"

하지만.. 실마리는 찾았지만~
커널 컴파일러 gcc 랑 로컬 버전이랑 호환이 안된다라....흠..

CentOS 8 Stream 에는 amdgpu-pro 그래픽 드라이버가 호환이 안되는 것 같다...

일단 다음에 시도하기로.. 
뭐 내 컴으로 머신러닝을 돌릴꺼도 아니고.. 
진짜 행렬 연산에 그래픽 카드가 빠르다는데.. 그냥 확인만 해볼려고 했던건데..

힘들다...ㅠ

결국 커널 업데이트도 해보고, 나름 해볼 수 있는 수단은 알아보고 시도 했지만, 다 실패..

작년 2020년 말에 나름 핫했던.. 이슈였던  
CentOS 8의 지원 중단 -> 올해까지 2021년 말까지만 지원을 하고 중단한다고 하는...  

> 이제 페도라 선두에 서서 Upstream 개발단에서 안정적인 부분을 Red Hat으로   
그리고 CentOS는 Red Hat의 안정적인 부분을 다시 이식받는 downstream 이였는데....  
내년부터는 Upstream이 된다고 한다. 페도라와 마찬가지로 개발쪽 이라고 해야하나?   
프로그램, 기능 등을 먼저 구현해보고 이게 안정적이면 Red Hat으로 가는 방향으로 된다고 한다.
 
어쨌든.. 그거는 또 그때 생각해보자 하고;; centos 8로 설치

리눅스에서 부팅 usb를 만드는 방법은 윈도우에서 만드는 것보다 훨씬 쉽다.
```shell
$ su -
#비번 입력 후 
# dd if=./CentOS-8.3.2011-x86_64-dvd1.iso of=/dev/sdd status=progress
```


그리고 리눅스 배포판 운영체제를 설치하면   
처음으로 해야할 것은 업데이트 

```shell
$sudo yum update
```
그러면 커널이 업데이트 된다.
그러면 반드시 재부팅을 해서 업데이트 된 커널로 부팅을 해줘야한다 

```shell
$init 6
```

그리고 나서 다시 amdgpu-pro 를 다운을 받고 
그래픽 카드 제품에 맞는 것을 찾아 공식 사이트에서 다운을 받고   
```shell
$tar xvf amdgpu-pro-21.10-1247438-rhel-8.3/
```

압축을 풀고 압축이 풀린 디렉토리에 들어가서 실행을 하면 된다.

```shell
$./amdgpu-pro-install -y --opencl=pal,legacy
```

참고 사이트   

https://www.amd.com

https://www.amd.com/en/support/graphics/amd-radeon-r9-series/amd-radeon-r9-300-series/amd-radeon-r9-380  

https://amdgpu-install.readthedocs.io/en/latest/install-installing.html