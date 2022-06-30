먼저 현재 깔려있는 정보 확인
list {package_name}
```
sudo dnf list firefox
```

현재 정보가 만약
```
Installed Packages
firefox.x86_64                       91.10.1-1.el8_6                       @appstream
```

이렇게 나올 때 다운그레이드할 수 있는 방법은 2가지 이다

downgrade {package_name} 명령어 사용

```
sudo dnf downgrade firefox
```

또는 특정 버전을 입력해준다 (단, 리포지터리에서 가능한 것만)

먼저 가능한 정보를 검색
```
dnf --showduplicates list firefox
```

시간이 조금 걸린다.   
이후 나온 결과는 대충 이런 식
```
Installed Packages
firefox.x86_64                       91.10.0-1.el8_6                       @appstream
Available Packages
firefox.x86_64                       91.9.0-1.el8_5                        appstream 
firefox.x86_64                       91.9.1-1.el8_6                        appstream 
firefox.x86_64                       91.10.0-1.el8_6                       appstream 
```

깔려있는 패키지는 첫 번째 줄, 가능한 버전은 2개 (현재 버전 빼고)  

이제는 다시 install 명령어나 downgrade 명령어를 사용해서 설치를 하면 된다 

패키지명에서 x86_64는 붙일 필요가 없다. {패키지}**-**{버전} 이렇게 구분을 하면 되는 듯 하다
```
sudo dnf install firefox-91.9.0-1.el8_5
```
또는 
```
sudo dnf downgrade firefox-91.9.0-1.el8_5
```

> install 시 패키지가 이미 설치되어 있고 설치하려는 버전이 낮으면 downgrade를 해준다 


