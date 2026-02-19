# Docker Error: Returned a Non-zero Code: 137
일때

This means a out of memory error.

To fix, you can add more RAM.

Or you can add more swap memory (FREE!). Swap memory uses part of your harddisk for temporary memory.

These steps are exactly the same from a previous guide:

예전에 코어 한개 짜리에서 문제가 있었는데, 이번에는 빌드할 때 사용하니 효과가 있는 듯 하다.

> 빌드시에 메모리가 꽉차서 컴퓨터가 먹통이 되는 경우, cpu 코어 사용을 제한해서 빌드 하면 효과가 있지만  
그래도 멈출 때가 있다. 이때 swap을 좀 더 많이 할당해주면 도움이 될 수도 있다.

**Fedora, Ubuntu** 모두 **사용** 가능하다.

# Confirm you have no swap
```
sudo swapon -s
```

예, 이미 8G 를 사용하고 있는 경우
```
Filename				Type		Size		Used		Priority
/dev/zram0                              partition	8388604		0		100
```
이미 파티션으로 추가를 한 것이라 type이 partition이 나오고,  
파티션이 아니라면 file 이라고 나온다.  

이미 파티션이 있다면 필요한 용량 만큼만 더 추가로 만들어주면 된다.  예를 partition 이 8G 있고, 추가로 8G가 더 필요하면  
아래 8G 를 더 추가해서 만들어 주면 됨  


# Allocate 1GB (or more if you wish) in /swapfile
```
sudo fallocate -l 1G /swapfile
```
> 원하는 용량 만큼 8G or 16G

# Make it secure
```
sudo chmod 600 /swapfile
ls -lh /swapfile
```
여기 까지는 file로 만들어진다. 용량 및 root 이하에 만들어진 swapfile을 확인할 수가 있음  

# Activate it
```
sudo mkswap /swapfile
sudo swapon /swapfile
```

```
Setting up swapspace version 1, size = 16 GiB (17179865088 bytes)
no label, UUID=2e613513-5c30-4f2a-87e3-a3e56627e799
```
이런 결과를 확인 할 수 있음

# Confirm again there's indeed more memory now
```
free -m
sudo swapon -s
```
> 또는 `free -h` 해보면 swap 메모리가 파티션에 추가되어 있던 것 까지 합쳐서 용량이 확보 되어 있다.   
system monitor 프로그램이나, htop 등에서도 확인 가능

예, 추가된 내용은 Type 이 file 로 표시됨  
```
$ sudo swapon -s
Filename				Type		Size		Used		Priority
/dev/zram0                              partition	8388604		0		100
/swapfile                               file		8388604		0		-2
```

# Configure fstab to use swap when instance restart
```
sudo nano /etc/fstab
```

# Add this line to /etc/fstab, save and exit
```
/swapfile   none    swap    sw    0   0
```

재부팅 후에도 사용이 가능하게 된다.

# Change swappiness to 10, so that swap is used only when 10% RAM is unused
# The default is too high at 60
```
echo 10 | sudo tee /proc/sys/vm/swappiness
echo vm.swappiness = 10 | sudo tee -a /etc/sysctl.conf
```

> 파이프라인 기호를 이용해서 출력한 내용을 | 오른쪽에 저장을 해준다. 

## swap 해제
만약 다시 만들거나  
해제 하려면 `sudo swapoff /swapfile`

/etc/fstab 에도 저장했다면 해당 부분을 찾아서 지워준다.

`sudo vi /etc/fstab`  

삭제
```
/swapfile none swap defaults 0 0
```

> 장치라면 /dev/sda1 ... 식으로 나온다고 하는데  
리눅스 처음에 설치할 때 swap 을 설정했다면 /etc/fstab 에는 나오지 않는 듯 하다.   

**특히 UUID로 이미 잘 mount 해서 쓰고 있는 부분은 건들지 않는다. 잘못하면 부팅 안 될 수 있음**
