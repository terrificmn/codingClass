# symlink remove 지우기
리눅스에서는 이름 뒤에 / slash 가 붙으면 디렉토리로 간주한다.  

그리므로 심링크 자체만 지우려면 무조건 /를 빼준다.  

```
rm -i my_symlink
```
-i 옵션을 넣어주자.  

실수로 `rm -i my_symlink/` 이렇게 사용했다면, 디렉토리 이므로 -i 로 지울 수가 없다.  
-r recursive 옵션이 들어가야 하기 때문에 안전하게 사용할 수가 있다.  

또한 심링크 자체만 삭제할려고 했는데 계속 지울 수가 없다고 할 경우에는  / (slash)가 들어가 있는지 확인한다.  


## symlink 디렉토리 지우기
만약 rm -rf 옵션을 사용해서 슬래쉬(/)까지 사용한다면 실제 포인팅 되어 있는 디렉토리를 지우게 된다.  
> 주의

ls -li 를 했을 때 
```
7785128 lrwxrwxrwx   1 myuser myuser   62 Jun  3  2025 my_symlink -> /home/myuser/Workspace/my_real_files
```

이렇게 되면 
`rm -rf my_symlink` 를 하게 되면  연결되어 있는 /home/myuser/Workspace/my_real_files 자체를 지우게 된다.  
아마도 이렇게 사용할 일이 없어야겠다. 혹은 실수로라도 사용하면 링크가 지워지는게 아니라 실제 파일이 지워지기 때문에 조심해야한다. 

