# 트러블 슈팅 설치 완료 후 grub 윈도우 선택이 안될 때
한개의 하드 디스크 (또는SSD)에 우분투를 듀얼 부팅이 가능하게 설치했지만

그리고 나서 다시 윈도우즈10으로도 잘 되나 다시 재부팅을 해보면  
윈도우즈 선택하는 것 없이 바로 리눅스 우분투로 실행이 되 버린다.  

다행히 쉽게 해결할 수 있다.

터미널을 열어서 간단하게 fdisk -l 로 확인한 후
```
$ sudo fdisk -l
``` 

<img src=0>
<br>

/dev/sda1, /dev/sda2, /dev/sda3 이렇게 NTFS 파일시스템으로, 윈도우 10이 잘 보인다. 너무 걱정 안해도 된다. 윈도우가 지워진 것은 아니니 안심하자~ 😅 


이제 update-grub 명령어를 통해서 간단히 해결할 수 있다  
터미널에서   
```
$ sudo update-grub
```

<img src=1>
<br>

이제 재부팅을 하면 부트로더 선택하는게 나타나게 된다.
윈도우로 부팅하려면 아래에 있는 windows를 선택해주고 
우분투로 들어가려면 ubuntu를 선택해주면 된다
