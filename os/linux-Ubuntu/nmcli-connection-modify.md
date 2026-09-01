# nmcli connection
네트워크 매니저 GUI 를 사용하지 못하는 경우이거나 CLI 를 이용해서 수동 IP 설정할 경우 사용  

```
nmcli connection modify [AP-SSID] ipv4.addresses 192.168.5.100/24
nmcli connection modify [AP-SSID] ipv4.gateway 192.168.5.254
nmcli connection modify [AP-SSID] ipv4.dns "8.8.8.8,8.8.4.4"
nmcli connection down [AP-SSID]
nmcli connection up [AP-SSID]
```

> 192.168.5.100/24 는 mask까지 같이 설정

 