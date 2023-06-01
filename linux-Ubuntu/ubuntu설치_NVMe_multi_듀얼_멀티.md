# 듀얼 설치일 경우
멀티/ 듀얼 부팅에 대해서 많이 다뤄보았지만 이번에는 nvme 형식으로 파티션을 지정할 경우에  

> NVMe (NonVolatile Memory express) 

새로운 저장 방식 및 transport에 대한 프로토콜이기도 하며, Solid State Drives의 새로운 방식   
즉, flash and next-generation 형태   

즉, 윈도우에서 먼저 설치를 하고 나서 나음 파티션에 (RAW인 상태) ubuntu 을 설치하려고 할 경우에   
nvme0n1 처럼 장치가 잡히는데 파티션은 뒤의 `p1, p2, p3` 이런식으로 구분이 된다  

이때 우분투로 설치하려고 나오는 파티션을 잘 찾아본다  
*nvme0n1p1*, *nvme0n1p2*, *nvme0n1p3*  이런식으로 나오는데   
nfts 로 되어 있는 Windows 파티션은 잘 배제를 하고   

용량으로 확인해서 맞는 파티션을 골라서 (예를 들어 nvme0n1p3) 의 체크박스를 눌러서   
ext4 형식으로 만들어주고 / (root) 를 지정해주고   
그곳에 설치를 해주면 된다   

boot loader 같은 경우에는 UEFI 방식일 경우   
콤보 리스트를 눌러서 **Windows Boot Manager** 가 설치된 곳으로.. 아마도 p1, p2? 이런식으로  
파티션 숫자가 나와 있을 것이다. 

> 아마도 다른 곳은 리눅스가 설치될 장치인 nvme0n1 이런식으로만 나왔던 것 같다   
그래서 UEFI에서는 Windows Boot Manager가 설치된 파티션에 (예를 들어서) nvme0n1p2 식으로   
설정을 해줘야 한다. (nvme의 경우 반대 경우는 테스트는 사실 못 해봄)    
* legacy BIOS 일 경우에는 아예 리눅스가 설치되는 장치에 boot loader를 지정해준다  

그곳으로 설정을 해주면 부트로더를 원할하게 설치를 해서   
멀티 듀얼 부팅: windows, linux ubuntu 간에 부팅이 원할하게 될 것이다!

## 듀얼 부팅
DEL을 누른 후에 BIOS 셋업에 들어가서  
Boot opiton을 지정해 주거나,  

또는 컴퓨터의 바이오스 마다 다르지만, F11, F12 등을 눌러서 Boot Option을 선택할 수가 있다.   






