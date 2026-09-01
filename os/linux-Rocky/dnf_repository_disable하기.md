# dnf disable
특정 레파지토리를 등록한 후에 해당 리포 때문에 안되는 경우에는 해당 리포를 disable 할 수 있다.

repo 현황을 먼저 확인
```
sudo dnf repolist 
```

여기에서 repo id 로 나오는 것들이 보여지는데.. 

```
sudo dnf config-manager --set-disabled 문제있는-repo이름
```

로 해주면 
`dnf install` 명령어가 잘 된다.

> 특정 리포가 문제 일 경우 dnf install, update 등이 작동이 안된다.


