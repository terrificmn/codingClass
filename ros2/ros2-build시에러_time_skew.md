```
make[2]: Warning: File '/home/sgtubun/colcon_ws/src/maze/src/maze_client.cpp' has modification time 16173 s in the future
make[2]: warning:  Clock skew detected.  Your build may be incomplete.
```

touch 가능? 
이거는 확인을 못해봄~ 파일들을 다시 복사해서 붙여넣더니 정상 상태로 돌아옴

> The touch command changes the time stamp of the file with the 'file name' give as argument to the command. For every file the Linux OS

 [EDIT :] Okay here's an update: You can use the touch command for any number of files in the following manner:
             1. Just 'cd' into the directory where the files need a time-stamp update.
             2. Next use the following command which will update the time-stamps of all the files in the directory:
                    # find . -exec touch {} \;

비슷한 경우가 생기면 참고