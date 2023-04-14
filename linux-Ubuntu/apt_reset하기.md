# restore apt repositories 

Reading package lists... Done                                                  
E: Failed to fetch https://40a28c6389e1d033e15e5087578b69890ab47742d0cda62d:@packagecloud.io/reelrbtx/SMACC_viewer/ubuntu/dists/focal/InRelease  402  Payment Required [IP: 52.53.48.94 443]
E: The repository 'https://packagecloud.io/reelrbtx/SMACC_viewer/ubuntu focal InRelease' is not signed.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
N: Usage of apt_auth.conf(5) should be preferred over embedding login information directly in the sources.list(5) entry for 'https://packagecloud.io/reelrbtx/SMACC_viewer/ubuntu'



`cd /etc/apt` 를 가보면 `sources.list` 가 있다   

열여서 확인을 해보면 뭐라뭐라~ 입력되어 있음  

이제 main, universe, multiverse, restricted 가 있는데  

- main : repository -- free open source 주로 Canonical의 개발자가 관여한다 (ubuntu 만드는 곳)   
- universe : 커뮤니티에서 관리하는 repository, 역시 free & open source
- multiverse : non-free software로 이루어진 repository
- restricted : 전혀 tree가 아닌 repository 


이제 sources.list를 삭제하고 새로 만든다  
```
cd ~/etc/apt
sudo rm -i ./sources.list
```

그리고 나서 모니터 왼쪽 상단의 Activities를 누르거나 키보드 superkey를 눌러서 검색   
software and updates (soft까지만 치면 된다)

새로 열리 창의 Ubuntu Software 탭 부분을 보면  
다 비활성화 되어 있다   main, universe만 선택할 수 도 있지만 다 선택해준다  

> 이왕 하는 거, Download from: 에 보면 Other를 선택할 수가 있고, mirror site를 선택할 수가 있는데  
~~select Best Server를 선택해준다.~~ china가 떠서;;;   
Korea,를 선택한 후에 mirror.kakao.com을 선택해준다   

그리고 close를 눌러주면 sources.list가 만들어 진다   



그리고 다시 
```
sudo apt update
```
를 하면 된다   


## 필요없는 list 삭제하기   
PPA라고 불리는 리스트를 삭제해준다   

내 경우에는 ros.list, docker.list, vscode.list 등이 있는데   
 
문제를 일으키는 reelrbtx_SMACC_viewer.list 를 삭제해줬다 

이번에는 source.list.d 디렉토리로 이동해서 직접 파일들을 삭제해준다  
```
cd /etc/apt/source.list.d
sudo rm -i reelrbtx_SMACC_viewer.list reelrbtx_SMACC_viewer.list.save 
```

그리고 이왕 source.list도 새로 reset 할 겸 위의 작업을 다시 진행하고   
`sudo apt update`

잘 된다 