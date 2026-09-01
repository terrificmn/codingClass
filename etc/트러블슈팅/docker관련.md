## 도커설치시 centos 8
리파지터리를 추가한 후에 
```
sudo yum install docker-ce docker-ce-cli containerd.io
```
했을 때 아래와 같은 에러가 발생 시 

```
Error: 
 Problem 1: problem with installed package podman-2.2.1-7.module_el8.3.0+699+d61d9c41.x86_64
  - package podman-2.2.1-7.module_el8.3.0+699+d61d9c41.x86_64 requires runc >= 1.0.0-57, but none of the providers can be installed
  - package containerd.io-1.4.4-3.1.el8.x86_64 conflicts with runc provided by runc-1.0.0-70.rc92.module_el8.3.0+699+d61d9c41.x86_64
  - package containerd.io-1.4.4-3.1.el8.x86_64 obsoletes runc provided by runc-1.0.0-70.rc92.module_el8.3.0+699+d61d9c41.x86_64
  - cannot install the best candidate for the job
```

runc를 지워준다
```
sudo
yum remove runc
```

그리고 다시 설치해주면 잘 설치가 된다
```
sudo  yum install docker-ce docker-ce-cli containerd.io

```

