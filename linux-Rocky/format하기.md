vat형식
lsblk로 장치를 먼저 확인한 후에 
sudo mkfs.vfat /dev/sde1

파티션번호를 잘 입력할 것
> vfat형식은 fat32 형식인데 최대 32G 지원, 개별파일은 4G까지만 지원


centos에서는 exfat 형식을 지원하지 않는듯하다
명령어가 안먹힘

ext4 형식으로 바꾼후에  인식이 되는지 봐야겠다


먼저 exfat 형식으로 할 수 있게 exfat-utils 를 설치해야한다
```
sudo yum install exfat-utils fuse fuse-exfat
```

그러면 기존에는 exfat형식이 없는 명령어라고 나왔는데 이제 
```
sudo mkfs.exfat /dev/sde1
```
이런식으로 하면 잘 된다
```
mkexfatfs 1.3.0
Creating... done.
Flushing... done.
File system created successfully.
```

하지만 tv등에서는 인식이 되지 않는다
결론은 4GB의 데이터(영상)을 복사하려면 mkfs또는 exfat으로 포맷을 해줘야하는데 
tv가 구형이라 그런지 fat32형식 밖에 지원을 못하는 듯 하다


