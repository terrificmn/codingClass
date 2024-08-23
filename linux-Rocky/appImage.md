# AppImage Tool


https://github.com/AppImage/AppImageKit

여기의 AppImage Tool 이다.  `appimagetool-x86_64.AppImage` 


appimage-builder 도 있는데 문서는 이쪽에 있으며 
https://appimage-builder.readthedocs.io/en/latest/intro/install.html#intro-install
위의 프로그램과는 다른 프로그램. 파라미터 등도 다르다.



## 실패

빌드는 해서 성공했지만, 역시 
```
/tmp/.mount_vnc_co8d4UkU/usr/bin/appimage-vnc_connector: error while loading shared libraries: libQt6Quick.so.6: cannot open shared object file: No such file or directory
```

에러 발생.. 역시 shared library 까지 알아서 만들어 주지는 않는 듯 하다. 다시 시도해보자.

