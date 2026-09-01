# debug_env 관련 문제 발생했을 경우
gz_sim 을 실행했을 경우에 아래와 같은 에러가 발생하는 경우

```
[INFO] [launch]: Default logging verbosity is set to INFO
[ERROR] [launch]: Caught exception in launch (see debug for traceback): launch configuration 'debug_env' does not exist
```

humble 브랜치  
commit ae3a1e1590407f6aff5239c4d6358a9fe544f56d   

pull 받은 후 다시 빌드 했을 경우 문제 없었음. (Release build 해도 소용 없었으나)  


결론 pull 을 받아서 최신화를 해주자. 


정확히 모르겠으나 아래 커밋 이후 뭔가 고쳐진 듯 하다
```
commit a422cfc2249dd4a1b8dbc68ab49cbc4a7e078fe3
Author: mergify[bot] <37929162+mergify[bot]@users.noreply.github.com>
Date:   Mon May 26 14:39:34 2025 +0200

    Fix debug_env (#747) (#750)
    
    (cherry picked from commit 76fc7ba3a40f96f7e2530a68557f2b1f98eb0c52)
    
    Signed-off-by: Alejandro Hernandez Cordero <ahcorde@gmail.com>
    Co-authored-by: Alejandro Hernández Cordero <ahcorde@gmail.com>
```

