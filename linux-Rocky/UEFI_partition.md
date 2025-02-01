# UEFI 파티션
UEFI 에서는 각 물리적 디스크에서 따로 파티션을 잡아서 하는 것이라고 착각했던 것 같다.

일단 윈도우 10을 먼저 설치를 하게 되면 자동으로 파티션을 만들어 주는데  

파티션 1, 17MB, Microsoft Reserved
파티션 2, 550MB, Microsoft Windows Recovery Environment(System) , NTFS
파티션 3, 550MB, EFI system (FAT , 32 bit)
파티션 4, primary 로 사용할 C 드라이브 정도..   

여기에서 파티션 1,2,3 (번호는 다를 수 있음) 는 자동으로 만들어 주는데, EFI system 파티션이 중요  

> 아마도 자동으로 만들어 주지 않는다면 이미 EFI system 이 있어서 그럴지도 모르겠다.   
또한 같은 디스크에 윈도우를 나중에 설치할 경우에 아마도 높은 확률로 리눅스 부트로더가 덮어 씌어질 듯 하고   

다른 디스크에 windows를 설치할 경우에는 딱히 문제는 안 생기는 듯 하다. 
(다만 EFI system을 리눅스에 만든 것을 사용하는 듯 하고, 덮어 씌어져서 리눅스가 부팅이 안되는 현상은 없다.)  


## 페도라
파티션 1, /boot/efi  100M (FAT 32_bit version)
파티션 2, /boot 1000MB



윈도우를 설치한 후 같은 디스크에 파티션을 나눠서 페도라를 설치하려고 하면, windows에서 만든 EFI system 을 사용할 수가 없다.  
> 일단 내 기억으로 그렇다;;;

우분투 와는 다르게 /boot/efi 를 mount 지점으로 갖는 파티션 EFI system 으로 만들어야지 페도라를 설치 할 수가 있다. 

이렇게 해서 멀티 부팅 설치를 진행하면 된다.


### 다른 디스크에 설치할 경우
fedora를 먼저 설치해서 EFI system 을 만든 경우에   
다른 디스크에 설치를 하려고 할 경우에는 윈도우에서 따로 자동으로 EFI 시스템을 사용하지 않는 것 같다.    
파티션 1, 17MB, Microsoft Reserved   
이 정도만 만들어주게 된다.   

디스크 다르므로 바이오스에서 부트 시작을 정해서 windows로 선택을 해주면 잘 진행이 된다.

단, 여기서 괜히 페도라에 있는 /boot/efi/EFI 이하의 Microsoft 등을 지우게 되면 윈도우 부팅이 불가하게 되므로 주의하자!
> 한번 날려먹음    
이후 windows 복구를 하면서 efi system를 다시 지정하게 되면 페도라 쪽의 /boot/efi 쪽이 완전히 이상해 지는 현상   
둘 다 들어갈 수가 없는 현상이 있었다.  

## ubuntu 경우
윈도우가 먼저 설치가 되어 있을 경우에는  (같은 디스크 사용)  

> 페도라와는 다르게 windows boot manager 를 사용할 수가 있다. 
우분투만 단독으로 설치할 경우에는 efi 시스템을 따로 만들어 진행할 듯 하지만.. windows 먼저 설치를 하고 해서 이는 확인이 필요할 듯 하다.  

우분투를 설치하는 과정에서 Device for boot loader installation 를 선택해서 파티션을 선택하는데..  
UEFI 기반에서는 디스크의 파티션으로 지정을 해준다. 윈도우의 EFI system로 되어 있는 파티션을 골라서 지정해준다.   
예: /dev/sda1 Windows Boot Manager

> /dev/sda ATA SAMSUNG SSD (500.0 GB) 이런 식으로 되어 있는 장치 자체를 선택하면 안됨. (legacy 기반일 경우에 선택한다)  


