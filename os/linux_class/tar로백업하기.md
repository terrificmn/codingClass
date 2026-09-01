일단 경로만 지정해주면 그 안의 파일은 다 압축해주므로 해당 경로의 상위 디렉토리에서 실행

```
tar pzcvf backupfile.tar.gz /path/to/
```

| 옵션 | 내용 |
| -- | -- |
| p | preserve-permission 퍼미션을 그대로 유지|
| c | create 생성할 때 |
| z | Compresses the archive with gzip gzip으로 압축할 때, 옵션을 선택안하면 그냥 묶는다(압축안함) |
| v | verbose file들이 작업되는 것을 보여준다 |
| f | archive file명 지정 이 옵션 다음으로 오는 아규먼트는 파일이름 |

> z 옵션 같은 경우는 상황에 따라 다르겠지만 용량을 엄청 줄여주지는 않는 것 같다.   
내 경우는 800MB 정도를 압축했더니 700MB 정도가 됨 (중간 사진, 영상등이 포함되서 그런 듯)

예를 들어 src 디렉토리 안에 있는 파일들을 다 압축하려고 하면 (압축할 디렉토리에서)   
상위 디렉토리로 한번 이동 해준 뒤에  
```
cd ..
tar pzcvf backup.tar.gz src/
```

그냥 전체를 다 백업해준다

단, 마지막에 
```
tar: Exiting with failure status due to previous errors
```

이런에러가 나면 중간에 퍼미션 관해서 에러가 발생할 경우가 높다 

이럴 경우에는 stderr를 이용해서 에러가 발생하는 메세지만 볼 수가 있다   
다시 명령어를 실행하면서 리다이렉트 기호로 /dev/null 에 보내면
```
tar pzcvf backup.tar.gz src/ > /dev/null
```

리다이렉트 기능을 이용해서 /dev/null 로 보내주면 필터기능을 해서 에러 메세지를 보여준다   
대신에 작업이 되는 것은 볼 수가 없다. 잠깐 기다려야함 (물론 압축은 됨)
```
tar: src/storage/app/images/tmp/6297ec10-1654123536: Cannot open: Permission denied
tar: src/storage/app/images/tmp/6295e88e-1653991566: Cannot open: Permission denied
tar: src/storage/app/images/tmp/6297ec0a-1654123530: Cannot open: Permission denied
```

> 파일이 몇개 안된다면 -v 옵션 만으로도 충분하겠지만 파일이 많을 경우는 메세지가   
바로 넘어가버리므로 확인할 수가 없다 

이제 위의 tmp 디렉토리의 권한을 확인하고 조정한 뒤에 다시 압축을 해준다

내 경우에는 tmp안에 생성되는 디렉토리들이 소유자 한테만 사용할 수 있게 되어 있었음   
```
ls -l
drwx------. 2 33 tape  4096 May 31 15:30 6295b603-1653978627
```
이럴 경우 소유자가 33번이 아니므로 디렉토리 접근 자체가 안됨
```
-bash: cd: 62a03ef7-1654669047/: Permission denied
```

이제 권한을 바꿔준다 상위 디렉토리인 tmp로 이동한 뒤에
```
sudo chown $USER:$USER -R tmp/
```

이제 다시 압축을 하면 모든 파일을 다 압축할 수가 있다.

