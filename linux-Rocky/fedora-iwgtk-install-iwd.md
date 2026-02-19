# iwgtk 빌드
iwd 를 사용할 때 iwctl 의 기능들을 GUI 로 사용할 수 있는 프로그램    

Fedora에서는 의존성 설치에 문제가 없어서 설치가 가능하다  
```
https://github.com/J-Lentz/iwgtk.git
```

다만, Ubuntu 22 에선는 gtk4 의 버전이 맞지 않아서 설치가 불가능  
> 아예 불가능 하지는 않을 수도 있지만,   
따로 release 버전 또는, 배포된 것이 없는 듯하고  
gtk4 를 따로 빌드하는 것은 별로 좋지 못하다. (추천 하지 않음)  

의존성 설치
```
sudo dnf install meson gtk4-devel qrencode-devel scdoc
```

빌드 설치

```
meson setup build
```
> prefix 설치 위치 변경 시에는 setup 시에 --prefix 옵션을 넣어준다.
예) usr 로 설치, 기본은 /usr/local  
`meson setup --prefix=/usr build`

```
cd build
meson compile
sudo meson install
```

## ubutnu 22
```
sudo apt install meson scdoc
sudo apt install libqrencode-dev adwaita-icon-theme-full
sudo apt install libgtk-4-dev
```
위에서 말한 것 처럼, libgtk-4-dev 의 버전이 맞지 않아서 meson 빌드가 실패한다.  

우분투 24에서는 가능하다고 하는 듯 하다.  



