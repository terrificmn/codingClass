# extend 하려면 
일단 비어 있는 또는 파티션이 확장하려는 파티션 바로 아래 순서로 위치 해야한다.  
order 가 중요하다

lsblk
sudo fdisk -l  등으로 확인할 수가 있다. 

이번 경우에 60기가 정도가 남았는데 하필이면 예전에 만들어둔 파티션이라  
/home 파티션 보다 먼저 순서여서 확장이 불가  

`sudo parted /dev/nvme0n1 print` 를 해보면  
각 파티션을 확인할 수가 있다.  

```
Number  Start   End     Size    File system     Name                  Flags
 1      1049kB  316MB   315MB   fat16           EFI System Partition  boot, esp
 2      316MB   1389MB  1074MB  ext4
 3      1389MB  9979MB  8590MB  linux-swap(v1)                        swap
 6      9979MB  74.6GB  64.6GB  xfs
 4      74.6GB  생략GB   생략GB   xfs
 5      생략
```
unallocated 되어 있는 64기가 정도를 파티션 지정 및 xfs 포맷하니  6번 파티션이 되었는데  
순서가 Start 및 End가 먼저 이고 그 다음에 4번 순서여서  
이런 경우에는 4번 파티션을 확장하는게 불가능 하다고 한다.  

또는 `sudo parted /dev/nvme0n1 print free` 를 해보면 free space 까지 표시해주는데  
중요한 것은 확장을 원하는 파티션 바로 아래 free space가 있으면 가능하지만 중간에 다른 파티션이 있거나  
순서가 위에 있을 경우에는 확장이 불가능  


가장 좋은 방법은 그냥  
마운트 해서 사용하는 방법이다. 이게 가장 안전하고 쉬운 것 같다 

```
sudo mkdir /mnt/data
sudo mount /dev/nvme0n1p6 /mnt/data
```
포맷은 disk 프로그램에서 포맷, other를 선택후 xfs 로 포맷 

또는 명령으로 포맷 `sudo mkfs.xfs /dev/nvme0n1p6`  
> 파티션 번호를 주의해서 확인한다.  
mkfs.xfs 는 xfs로 포맷, make filesystem XFS  

아예 fstab 에 포함시키기



```
# get the UUID
sudo blkid /dev/nvme0n1p6

# add to /etc/fstab:
UUID=your-uuid  /mnt/data  xfs  defaults  0  2
```

fstab 에 대한 자세한 내용

The last two numbers are:
0 — dump: Whether the dump backup utility should back up this partition. Almost always 0 (disabled) since dump is rarely used anymore.
2 — pass (fsck order): Controls the order in which fsck checks filesystems for errors at boot time:

0 = never check (used for swap, network filesystems, etc.)
1 = check first — only for / (root)
2 = check after root — for all other regular partitions like /home, /data

So 0 2 means: don't back up with dump, and check this filesystem second at boot (after root). This is the standard setting for any non-root partition.
Note for XFS: fsck doesn't actually apply to XFS the same way it does to ext4 — XFS does its own journal recovery automatically at mount time. So for XFS you could technically put 0 0, but 0 2 is harmless and commonly used anyway.

