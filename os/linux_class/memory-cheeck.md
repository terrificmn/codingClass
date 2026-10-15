# memory 확인

가장 쉽게 확인할 수 있는 것은 htop  에서 Mem 을 확인하면 된다.  


또는 `free -h`  
```
               total        used        free      shared  buff/cache   available
Mem:            12Gi       7.2Gi       2.7Gi        28Mi       2.6Gi       5.0Gi
```

여기에서 보면 total 이 12Gi 로 나오고, 실제 GB 와는 차이가 있다. 
> (1 GiB = 1,024³ bytes)   
Gigabytes (GB) base-10 (1 GB = 1,000³ bytes).  

어쨋든, 나머지는 하드웨어서 Linux kernel 이 숨기거나, integrated GPU 를 위해서 사용하기 위해서 사용이 된다.  

`sudo dmidecode -t memory | grep -E "Size|Locator"` 를 해보면 

실제 Locator: 몇 번째 슬롯 DIMM 0  및, Size 등이 나온다. 
```
    Size: No Module Installed
	Locator: DIMM 0
	Bank Locator: P0 CHANNEL A
	Non-Volatile Size: None
	Volatile Size: None
	Cache Size: None
	Logical Size: None
	Size: 16 GB
	Locator: DIMM 0
	Bank Locator: P0 CHANNEL B
	Non-Volatile Size: None
	Volatile Size: 16 GB
	Cache Size: None
	Logical Size: None
```

