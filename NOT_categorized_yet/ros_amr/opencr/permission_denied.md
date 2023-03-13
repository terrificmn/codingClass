
ser_open: unable to open port: Permission denied


일단 
```
sudo usermod -aG dialout $USER
```

유저를 dialout 그룹에 포함시켜준다   

> 로그아웃 해야함


터미널에 `id` 를 입력해서 user의 그룹을 알 수 있다

처음에는 dialout 이 없지만, 로그아웃 (안되면 재부팅) 해주면 dialout 이 생긴다

```
uid=1000(유저id) gid=1000(유저id) groups=1000(유저id),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),120(lpadmin),132(lxd),133(sambashare)
```

이후
```
uid=1000(유저id) gid=1000(유저id) groups=1000(유저id),4(adm),20(dialout),24(cdrom),27(sudo),30(dip),46(plugdev),120(lpadmin),132(lxd),133(sambashare)
```

dialout 그룹에 속하게 되었으므로, `chmod 777 /dev/tty...` 등이 필요없고, Permission 문제가 해결된다

