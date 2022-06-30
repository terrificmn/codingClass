파일들을 지우게 되면 윈도우상에서 볼 수가 없지만   
파일들은 deallocated 되어 있을 뿐 하드디스크등에는 여전히 남아 있게 된다.

" After it is deallocated, the space is available for use when new data is written to the disk.
Until the space is overwritten, you can recover the deleted data by using a low-level disk editor   
or data-recovery software.


주의할점은 반드시 다른 프로그램은 다 꺼준다. (주의사항이라고 한다) 
그리고 파워셀만 켜준다

파워셀을 실행해서 /w 옵션을 주는데 이는 할당되지 않는 공간 (즉 지운 파일들이 있는 공간)을 다시입력이 되는 것   
(overwritten) 

> Data that isn't allocated to files or folders is overwritten. 
The data is permanently removed. It can take a long time if you overwrite a large amount of space.

> 그리고 지우지 않은 현재 파일들에게는 전혀 영향이 없다.

드라이브 전체에 사용할 수도 있고
```
cipher /w:C:      
```

또는 특정 디렉토리를 지정해도 된다
```
cipher /w:C:\test
```

> 만약 원하는 특정 드라이브가 C 드라이브가 아니라면 C 대신에 다른 드라이브 알파벳을 적어주면 된다.

```
To remove as much data as possible, please close all other applications while                                           
running CIPHER /W.
Writing 0x00
.........................................................................................................
Writing 0xFF
.........................................................................................................
Writing Random Numbers
.........................................................................................................   
```

이런식으로 진행이 된다. 시간이 꽤 걸린다~ 정확히 재보지는 않았지만 1시간 뒤 와보니 다 되어 있었음

파일들은 휴지통에 지운 후 아예 지워버렸다고 해도 하드 디스크나 SSD에는 여전히 존재하는 상태이므로 
지워진 파일들을 완전히 제거 할 때에는 위의 cipher 를 이용하거나 다른 유틸리티를 사용한다

*위에서는 일단 test라는 디렉토리는 남아있는 상태였고
그 안에 파일들을 지운 상태에서 실행을 함.
test 디렉토리까지 지운상태에서도 실행이 가능한지는 확인해보지 않았다
