외장하드에 리눅스를 시험 삼아 설치를 했는데   
테스트로 Rocky Linux 설치를 해봤는데 이제는 필요가 없어서  
그냥 하나의 파티션으로 저장공간으로 활용하려고 하는데 lvm으로 설정이 되어 있어서  
파티션 삭제가 안된다

내 컴 기준으로 파티션 sdd5 부분에 lmv으로 만들어져 있다

lsblk 를 입력하면 간단하게 장치 및 정보를 볼 수가 있다
```
lsblk
```
```
sdd           8:48   0 111.8G  0 disk 
├─sdd1        8:49   0  37.3G  0 part /run/media/sgtocta/5417359b-4823-469c-a5c6
├─sdd2        8:50   0   600M  0 part /run/media/sgtocta/9E2D-8F05
├─sdd3        8:51   0     1G  0 part /run/media/sgtocta/9f48dcca-4d95-41fa-b14b
└─sdd5        8:53   0    73G  0 part 
  ├─rl-swap 253:3    0   1.5G  0 lvm  
  ├─rl-home 253:4    0  37.5G  0 lvm  
  └─rl-root 253:5    0    34G  0 lvm  
```

이제 sdd5 파티션 부분을 지울려고 하는데 lvm으로 되어 있어서 그냥 삭제가 안된다    

> fdisk 명령어를 이용해서 파티션을 지울려고 했는데 실패  
mkfs 명령어로 아예 포맷할려고 했는데 이것도 실패  

먼저 vgdisplay 를 이용해서 lvm 구성을 살펴보자
```
sudo vgdisplay
```

결과는 
```
 --- Volume group ---
  VG Name               rl
  System ID             
  Format                lvm2
  Metadata Areas        1
  Metadata Sequence No  4
  VG Access             read/write
  VG Status             resizable
  MAX LV                0
  Cur LV                3
  Open LV               0
  Max PV                0
  Cur PV                1
  Act PV                1
  VG Size               72.94 GiB
  PE Size               4.00 MiB
  Total PE              18673
  Alloc PE / Size       18671 / 72.93 GiB
  Free  PE / Size       2 / 8.00 MiB
  VG UUID               zrPqHF-5iMV-eMVq-7a5u-ifeC-R4vJ-wNlflL
```

볼륨이 VG Name부분에 rl이라고 나온다  
그리고 위에 lsblk로 확인했을 때에도 보면 rl-swap, rl-home, rl-root 로 나왔음  

> (주의: 기존 원래 리눅스가 설치되어 있는 곳은 cl로 되어 있었음   
그리고 현재 외장 저장장치로 추가가 되어서 rl로 생성이 되어있었던 것 같음
(본인 컴 기준임))

이제 볼륨 rl를 지워보자. 명령어는 vgremove 를 사용한다
```
sudo vgremove rl
```

그러면 3개의 논리적 볼륨을 지울꺼냐고 물어본다
```
Do you really want to remove volume group "rl" containing 3 logical volumes? [y/n]: y
Do you really want to remove active logical volume rl/swap? [y/n]: y
  Logical volume "swap" successfully removed
Do you really want to remove active logical volume rl/home? [y/n]: y
  Logical volume "home" successfully removed
Do you really want to remove active logical volume rl/root? [y/n]: y
  Logical volume "root" successfully removed
  Volume group "rl" successfully removed
```

이제 확인을 해보면
```
lsblk
```

아래 처럼 나옴
```
생략..
sdd      8:48   0 111.8G  0 disk 
├─sdd1   8:49   0  37.3G  0 part /run/media/octa/5417359b-4823-469c-a5c6-c32b
├─sdd2   8:50   0   600M  0 part /run/media/octa/9E2D-8F05
├─sdd3   8:51   0     1G  0 part /run/media/octa/9f48dcca-4d95-41fa-b14b-4f30
└─sdd5   8:53   0    73G  0 part 
```
lvm이 제거가 되었다

이제 그냥 저장공간으로 다시 쓰기 위해서 포맷  
(파티션숫자를 더블체크해서 입력해야한다~ 모든 데이터가 지워진다)
```
sudo mkfs.ext4 /dev/sdd5
```

또는 
```
sudo mkfs -t ext4 /dev/sdd5
```

이렇게 했더니 하나의 파티션으로 다시 잡혀서 잘 된다~