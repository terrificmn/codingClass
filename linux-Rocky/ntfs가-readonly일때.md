# 리눅스에서 ntfs readonly 해결
리눅스에서 ntfs 파일시스템으로 쓰고 있는 드라이브가 갑자기 말썽이다
새로운 파일을 만들 수가 없다

Could not mount read-write, trying read-only

또는 파일을 만들려고 하면 read-only 라고 나오는 현상

ntfsfix 명령어를 이용해서 다시 마운팅을 하면 된다

먼저 마운팅 되어 있는 것을 해제를 시킨 후에
```
sudo umount -a
```

현재 마운팅해야하는 장치가 sdc의 2번째 파티션이기때문에   
자신의 장치에 맞게 선택해준다
(full read/write access 가능하게 해줌
```
sudo ntfsfix /dev/sdc2
```

```
Attempting to correct errors... 
Processing $MFT and $MFTMirr...
Reading $MFT... OK
Reading $MFTMirr... OK
Comparing $MFTMirr to $MFT... OK
Processing of $MFT and $MFTMirr completed successfully.
Setting required flags on partition... OK
Going to empty the journal ($LogFile)... OK
Checking the alternate boot sector... OK
NTFS volume version is 3.1.
NTFS partition /dev/sdc2 was processed successfully.
```

위와 비슷하게 나오게 되고 이제 다시 파일을 만들거나 복사 제거등이 가능해진다


## ntfsfix 없을 경우 설치

`ntfsfix` 라고 명령어를 쳤을 때 업다고 하면서 설치하겠냐고 물어본다  y 를 눌러주자
```
bash: ntfsfix: command not found...
Install package 'ntfsprogs' to provide command 'ntfsfix'? [N/y] y
```

또는 직접 설치
```
sudo dnf install ntfsprogs
```

사용법 help
```
Usage: ntfsfix [options] device
    Attempt to fix an NTFS partition.

    -b, --clear-bad-sectors Clear the bad sector list
    -d, --clear-dirty       Clear the volume dirty flag
    -h, --help              Display this help
    -n, --no-action         Do not write anything
    -V, --version           Display version information

For example: ntfsfix /dev/hda6
```
