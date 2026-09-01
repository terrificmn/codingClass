# Linux에서 Windows NTFS 인식하기
특히 CentOS 계열에서는 Windows의 NTFS 파일시스템을 인식 못하므로  
인식할 수 있게 설치를 해준다

> 우분투에서는 NTFS가 설치 없이 바로 인식되었던 것 같다

NTFS 시스템 마운트 하기   
기존 윈도우에서 사용하던 하드 디스크를 mount를 하려고 하면  
nfts 파일 시스템을 못 읽을 떄   

NTFS 드라이버를 설치해야 한다고 함

먼저 epel 저장소 설치
```
$sudo yum install epel-release
```

그 다음 ntfs-3g 드라이버 패키지라고 함, 패키지fmf epel 저장소에 설치
```
$sudo yum install ntfs-3g
```

그러면 이제 mount 명령어로 마운트를 시키면 됨   
만약 마운트할 디렉토리가 없다면 만들어 준다  
그리고 mount  

```
$sudo mount /dev/sdb1 /media/disk
```

이때 mount.ntfs-3g 로 입력하면서 -o 옵션을 넣어줄 수 있는데   
나중에 윈도우에서 문제가 없도록 옵션을 넣어줄 수 있음   
windows_names <---- 파일/폴더 만들 때 windows에서 허용 안되는 문자열을 막아줌
hide_hid_files <---- 휴지통이나 볼륨 정보를 숨겨줌 ((RECYCLER/ System Volume Information)

사용 예:
```
$sudo mount.ntfs-3g -o hide_hid_files,windows_names /dev/sdb1 /media/disk
```
