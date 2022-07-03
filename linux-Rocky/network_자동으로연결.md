# 네트워크 시작부터 (부팅 후) 자동으로 시작되게 하기
사실 GUI 모드에서 setting에서 network 부분에서 하면 쉽게 할 수도 있으나  

CLI로 할 경우 네트워크 관련 파일을 확인할 수 있는데
```
$cat /etc/sysconfig/network-scripts/ifcfg-enp3s0
```

여기에서 ONBOOT=no 에서 yes로 바꿔주면 된다

** 참고:
네트워크 자체를 내리기, 원래는 systemctl start network.service 로 하면 되는데   
centos8에서는 deprected되었다고 한다. 그래서 nmcli 명령어를 사용한다
```
$sudo nmcli networking off
$sudo nmcli networking on
```
이거를 하면 아예 네트워크를 내리는 것이기 때문에   
GUI에서 셋팅에서 네트워크를 보면 아예 사라져버린다. on을 하면 다시 생김