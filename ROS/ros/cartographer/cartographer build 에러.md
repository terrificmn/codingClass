별 다른 것을 한 적이 없는디... 갑자기 build가 에러..;;

ImportError: cannot import name 'soft_unicode' from 'markupsafe' (/home/amrlabs2/.local/lib/python3.8/site-packages/markupsafe/__init__.py)
make[2]: *** [docs/CMakeFiles/build_doc.dir/build.make:58: docs/CMakeFiles/build_doc] Error 1


markupsafe를 지우고 사실은 업데이트를 하려고 했으나 실패
```
python3 -m pip install markupsafe==2.0.1
```



다시 markupsafe를 설치해준다  
```
python3 -m pip install markupsafe


```

