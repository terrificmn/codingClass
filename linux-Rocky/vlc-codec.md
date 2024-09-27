# vlc libavcodec 설치

rpm fusion repo 활성화

```
sudo dnf install \
  https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
```

이후 libavcode-freeworld 설치
```
sudo dnf install ffmpeg-free libavcodec-freeworld
```



