# scrcpy

리눅스에서 안드로이드 기계를 usb로 연결해서 화면 공유로 컨트롤 및 볼 수 있게 해주는 프로그램

## 설치
설치는 다행히 apt나, snap 패키지등을 사용해서 인스톨 가능

```
sudo apt install scrcpy
```

[최신 버전을 빌드해서 사용할 경우에는 여기 깃허브 문서 참고](https://github.com/Genymobile/scrcpy/blob/master/doc/linux.md)

의존성 패키지 설치
```
sudo apt install ffmpeg libsdl2-2.0-0 adb wget \
                 gcc git pkg-config meson ninja-build libsdl2-dev \
                 libavcodec-dev libavdevice-dev libavformat-dev libavutil-dev \
                 libswresample-dev libusb-1.0-0 libusb-1.0-0-dev
```

이후 깃클론 및 sh스크립트 파일로 빌드 및 설치
```
git clone https://github.com/Genymobile/scrcpy
cd scrcpy
./install_release.sh
```

## 삭제
빌드했던 scrcpy 디렉토리로 이동 후 
```
cd scrcpy
sudo ninja -Cbuild-auto uninstall
```


## 사용
먼저 안드로이드 태블릿이나 핸드폰에서 development mode를 활성화 시켜준다   
보통 about phone 같은 폰 정보 보는 메뉴 선택  >> Software information 선택   
Build number 가 목록에 있는데 여러번 클릭(터치)해주면 모드가 활성화됨

이후 첫 메뉴로 다시 진입하면 Developer Options가 있는데  
USB debugging Debug mode when USB connected 부분을 활성화 시켜준다   

안드로이드와 컴퓨터를 usb케이블로 연결 후에   
터미널에 `scrcpy` 명령어를 입력해주면 실행이 된다   

핸드폰에서 허용만 해주면 바로 화면 공유가 된다   


