주의   
용량이 꽉차서 df -h를 해보니  
docker가 사용하는 곳이 93%를 사용중;;;; 65기가   
```
Filesystem           Size  Used Avail Use% Mounted on
overlay               70G   65G  5.4G  93% /var/lib/docker/overlay2/f9a60303585c74acb3c301677d7c3465fe5d8e3704f796f01753e6d4fed3b789/merged
```

지우는 방법은... 근데 이거는 다 지우는 거 이므로;;; 원래 다 지울 생각은 없었는데;; 망 ㅋㅋ  
절대 주의!! 뭐 로컬에서 하는것은 지워져도 상관은 없긴한데... 그래도 너무 다 지워버렸네; ㅠ   
```
docker system prune --all --volumes --force
```
이렇게 하면 다 지운다
```
Deleted Containers:
4520d9f063e1037b681b10570d6ef3c647f470f8a239f65b3224ab7fcb2918c8
81fa3df8568205da555f20830363a244bf011754640becc93b0f6617ef1c4f44
923ce86e9f4ca2a3564a5c34781a85693c9f345d92fc26cbae9b3c5a1af5bf07
bcb3de26e90d2ddbffb0d4af74976026837d2ab11508787fb59756cde3cf6003
23964680fe8b575af852a24af9c4eb0545c9cd30c01892f73afa7bc724ed8966

Deleted Networks:
movie-recommendation-api_default
docker-tfod_default
docker-api-test_default
docker-laravel-blog_default
movie-api-docker-git_default
docker-ml_default
docker-streamlit_default

Deleted Volumes:
docker-laravel-blog_mysqldata

...
..
중략..
Total reclaimed space: 54.6GB
```

사용안하는 컨테이너등 모든 것들을 지움;;;  
54기가 확보됨 ;;;

docker ps -a 해보면 아무것도 남아 있지 않다;;

  


## 용량 확인하기
aws 사용할 때의 기록  

aws overlay 용량이 많이 차지 할 때   df -h 명령어를 치면 용량을 보여준다
```
df -h
```

```
ubuntu@ip-172-51:~$ df -h
Filesystem      Size  Used Avail Use% Mounted on
udev            476M     0  476M   0% /dev
tmpfs            98M  1.1M   97M   2% /run
/dev/xvda1       30G   12G   18G  39% /
tmpfs           490M     0  490M   0% /dev/shm
tmpfs           5.0M     0  5.0M   0% /run/lock
tmpfs           490M     0  490M   0% /sys/fs/cgroup
/dev/loop0       32M   32M     0 100% /snap/snapd/11036
/dev/loop1       56M   56M     0 100% /snap/core18/1988
/dev/loop2       34M   34M     0 100% /snap/amazon-ssm-agent/3552
overlay          30G   12G   18G  39% /var/lib/docker/overlay2/bc0db97f413128627de0a55b7c031cf97e9f331c0897a325e5eedefcb4eee09a/merged
overlay          30G   12G   18G  39% /var/lib/docker/overlay2/7b3280a5e25404a64d135ee1f20ab06582adfee5e999a2e20f9337c525538ed5/merged
overlay          30G   12G   18G  39% /var/lib/docker/overlay2/db32788b8003b5e270b1fec351d977b9d945d0007209814b9e832ae37ce1bf0a/merged
overlay          30G   12G   18G  39% /var/lib/docker/overlay2/776267f2d5de7809c48201f41a473af942d22b6f62edaae09c4c0ac15bf3b2e4/merged
tmpfs            98M     0   98M   0% /run/user/1000
```

용량 파악하려면 / 디렉토리로 이동 후   
du 명령어를 사용한다 
```
sudo du -h . | sort -hr | head -10
```

```
du: cannot access './proc/303/task/303/fd/4': No such file or directory
du: cannot access './proc/303/task/303/fdinfo/4': No such file or directory
du: cannot access './proc/303/fd/3': No such file or directory
du: cannot access './proc/303/fdinfo/3': No such file or directory
14G	.
7.2G	./var
7.0G	./var/lib
6.7G	./var/lib/docker
6.6G	./var/lib/docker/overlay2
2.5G	./tmp
2.2G	./var/lib/docker/overlay2/1807477df7cb3ad43cd527314010bd1e956d44bbe5ba99d4b6f2fd3ef524f3db/diff
2.2G	./var/lib/docker/overlay2/1807477df7cb3ad43cd527314010bd1e956d44bbe5ba99d4b6f2fd3ef524f3db
1.6G	./var/lib/docker/overlay2/1807477df7cb3ad43cd527314010bd1e956d44bbe5ba99d4b6f2fd3ef524f3db/diff/usr/local/lib/python3.7/site-packages
1.6G	./var/lib/docker/overlay2/1807477df7cb3ad43cd527314010bd1e956d44bbe5ba99d4b6f2fd3ef524f3db/diff/usr/local/lib/python3.7
```

tmp에 2.5는 지워도 될 듯 하고  
도커 파이썬 에서 용량을 많이 차지함.. 


```
sudo du -h /var/lib/docker/overlay2/1807477df7cb3ad43cd527314010bd1e956d44bbe5ba99d4b6f2fd3ef524f3db/diff/usr/local/
lib/python3.7/site-packages | sort -hr | head -101.6G	/var/lib/docker/overlay2/
```
코드가 길지만 위에서 나온 결과를 토대로 복사해서 확인해보니  
대충 어디에서 용량을 많이 차지 하는지 알 수 있었다. ..

```
1807477df7cb3ad43cd527314010bd1e956d44bbe5ba99d4b6f2fd3ef524f3db/diff/usr/local/lib/python3.7/site-packages
927M	/var/lib/docker/overlay2/1807477df7cb3ad43cd527314010bd1e956d44bbe5ba99d4b6f2fd3ef524f3db/diff/usr/local/lib/python3.7/site-packages/tensorflow
764M	/var/lib/docker/overlay2/1807477df7cb3ad43cd527314010bd1e956d44bbe5ba99d4b6f2fd3ef524f3db/diff/usr/local/lib/python3.7/site-packages/tensorflow/python
95M	/var/lib/docker/overlay2/1807477df7cb3ad43cd527314010bd1e956d44bbe5ba99d4b6f2fd3ef524f3db/diff/usr/local/lib/python3.7/site-packages/tensorflow/include
68M	/var/lib/docker/overlay2/1807477df7cb3ad43cd527314010bd1e956d44bbe5ba99d4b6f2fd3ef524f3db/diff/usr/local/lib/python3.7/site-packages/pyarrow
65M	/var/lib/docker/overlay2/1807477df7cb3ad43cd527314010bd1e956d44bbe5ba99d4b6f2fd3ef524f3db/diff/usr/local/lib/python3.7/site-packages/scipy
50M	/var/lib/docker/overlay2/1807477df7cb3ad43cd527314010bd1e956d44bbe5ba99d4b6f2fd3ef524f3db/diff/usr/local/lib/python3.7/site-packages/tensorflow/include/external
49M	/var/lib/docker/overlay2/1807477df7cb3ad43cd527314010bd1e956d44bbe5ba99d4b6f2fd3ef524f3db/diff/usr/local/lib/python3.7/site-packages/pandas
39M	/var/lib/docker/overlay2/1807477df7cb3ad43cd527314010bd1e956d44bbe5ba99d4b6f2fd3ef524f3db/diff/usr/local/lib/python3.7/site-packages/notebook
35M	/var/lib/docker/overlay2/1807477df7cb3ad43cd527314010bd1e956d44bbe5ba99d4b6f2fd3ef524f3db/diff/usr/local/lib/python3.7/site-packages/notebook/static
```


