# 다빈치 리졸브 18베타 설치
공식 웹사이트에서 다운 studio 버전은 유료 (무료버전까지 포함)
그냥 버전으로 받음

zip파일 압축풀기
```
unzip DaVinci_Resolve_18.0b2_Linux.zip -d davinci/
```
> -d 디렉토리를 만들고 압축을 풀어준다

설치
```
./DaVinci_Resolve_18.0b2_Linux.run -i
```

wayland에서 설치하면 아래처럼 나오고 끝
```
QT_QPA_PLATFORM=wayland
Creating Common Data Dir : /var/BlackmagicDesign/DaVinci Resolve
DaVinci Resolve installed to /opt/resolve
```
x-11 에서 설치하면 아무것도 안나오고 끝

가장 큰 문제는 gpu를 인식하지 못해서 사용을 할 수가 없다는 것   
환경설정으로 유도를 하지만 GPU가 나오지 않으니 선택도 못하고 진행을 할 수 없다

<img 에러메세지>

<br/>

## amdgpu 설치 (opencl 사용) -다빈치 리졸브 18베타
사실 동영상 플레이어, 캡쳐 등등 처음 상태 그대로 따로 설치를 안해도 기본으로 잘 된다.

다만 다빈치 리졸브를 사용하려면 GPU를 인식못하게 되면 프로그램 자체를 사용할 수가 없다  
환경설정에서 GPU를 선택해줘야하는데 더 이상할 수 없는 문제발생

그래서 open-cl이 필요하다고 하는데

closed source (CL + GL + kernel part) 라는 의견도 있더라..

어쨋든 Rocky Linux 8.5에 맞춰서 하면 amdgpu설치는 잘 되지만 다빈치에서는 여전히 인식을 못함

어쨋든 나름 몇번의 재부팅 및 트러블슈팅을 통해서 성공함 

| amdgpu / 커널 버전 | 다빈치 인식 | 비고 |
|---|---|---|
| 21.50 / 8.5 | 실패 | rpm설치후 설치 |
| 21.40.1 /8.4 | 실패 | rpm설치후 설치, 재부팅 후 화면 안 들어옴 |
| 20.50 / 8.3 | 성공 | amdgpu-pro-install 직접 설치, 재부팅 후도 ok |

버전 호환이 안될 시 화면이 안 들어올 수도 있다. 

~~20.50 커널8.3 버전은 부작용이 *vlc플레이어가 X-11 디스플레이* 에서만 작동한다.~~  
(아래에서 설명)


중요한 점은 *커널 업데이트*를 꼭 하고 해야 한다는 점이다   
*혹시라도 잘못 되면 이전 커널 버전으로 부팅 할 수 있다*
```
sudo dnf update
```
그래야 혹시 모를 사태에 대비할 수 있다

> 라데온 R9 380 경우, 공홈에서 제품으로 검색해서 들어가면   
드라이버 목록이 나오는데 9.0, 8.6, 7.9 등.. 버전이 맞는게 없다.  
그리고 rpm으로 나름 편하게 설치 후 amdgpu-install 설치하게 되어있다

결국 다빈치 리졸브에서 인식을 못하므로 그래서 버전을 낮춰서  
Radeon™ Software for Linux® 20.50 버전을 설치   
[여기에서](https://www.amd.com/en/support/kb/release-notes/rn-amdgpu-unified-linux-20-50)


## amdgpu 설치
다만 설치를 하기 전에 약간 해킹(?)ㅋㅋㅋ 트릭을 써야한다

rocky linux을 사용하기 때문에 ID를 속여야한다 ㅋㅋ 그래야 설치가 가능
그냥 설치하려고 하면 지원가능한 os가 아니라고 나온다. 설치불가

> 상위 버전 rpm으로 설치해서 하는 것들을 이미 rocky 리눅스도 지원범위로 추가 변경했다고 한다  
하지만 파일로 직접 설치하는 것은 예전 버전이므로 호환이 안된다고 나옴

먼저 파일을 연다
```
sudo vi /etc/os-release 
```

내용은 아래 처럼 나오는데
```
NAME="Rocky Linux"
VERSION="8.5 (Green Obsidian)"
ID="rocky"
... 생략..
```

그 중에 ID를 변경 후 저장한다
```
ID="centos"
```

이제 다운 받은 것 압축풀기
```
cd ~/Downloads
tar -xvf amdgpu-pro-20.50-1234664-rhel-8.3.tar.xz
```

그리고 압출 풀린 디렉토리로 이동
```
cd amdgpu-pro-20.50-1234664-rhel-8.3
```

이제 20.50 버전은 직접 실행파일을 통해서 설치를 하게되는데 

설치하기, 옵션으로 opencr을 rocr, legacy를 설치
```
./amdgpu-pro-install -y --opencl=rocr,legacy
```

설치가 다 되고 나서 `WARNING: amdgpu dkms failed for running kernel` 이라고 나오지만
실행에는 문제가 없다

> 원래 이 명령어를 활용해 보려고 하는데 `./amdgpu-pro-install --no-dkms‍`  
amdgpu-pro-install 에서는 안되고 admgpu-install 에서 사용하라고 한다  
하지만 amdgpu-install로 설치하면 Davinci에서 역시 인식을 못함;;   
amdgpu-pro-install 명령어로 설치해야한다

이제 다빈치 리졸브를 실행해보자

New Project를 연후 DaVinci Resolve 첫 번째 메뉴에서 Pre
Memory and GPU 부분을 클릭하면 GPU가 제대로 나오고 OpenCL도 나온다

<img setting에서 차이>
<img gpu선택>

마지막으로 `sudo vi /etc/os-release` 해서 ID를 rocky로 다시 변경

### VLC 관련 (재생 시 프로그램 종료)
로그인 시 Waylands Display Server를 선택했을 경우 
VLC media player를 재생할려고 하면 프로그램이 그냥 종료되는데    

그냥 X-11 Display Server에서 실행한다
또는
Tools > Preferences 에서 Video 탭에서 Display 부분의 Output 설정을 X11 video output (XCB)로 변경해준다  
(VLC 3.0버전)



## 지우기
혹시 뭔가 문제가 있다면 화면이 재부팅시 화면이 안 들어 올 수도 있는데
이때는 재부팅 시 부트로더에서 최초 커널 (하위버전) 부팅을 해준다음에

해당 설치했던 디렉토리로 이동 후 
```
./amdgpu-install --uninstall
```
이렇게 하면 아예 amdgpu 그래픽드라이버를 지워준다

다시 재부팅을 해서 최신 커널로 부팅을 해주면 화면이 잘 보인다


rpm 으로 설치했다면 아예 설치프로그램을 지우기
```
$ sudo yum remove amdgpu-install
```
또는 
```
sudo rpm -e amdgpu-install 
```



## 테스트

8.5 (rpm)
amdgpu-install --usecase=graphics,opencl --vulkan=pro --opencl=rocr
8.5  실패 vlc 이상없음, 다빈치 인식 안됨


8.4 (rpm)
amdgpu-install --usecase=graphics --vulkan=amdvlk --opencl=rocr
실패
