# wl-clipboard
wl-clipboard 설치한 후에 사용  

깃허브에 있는 내용 그대로 가져옴
```
# copy a simple text message
$ wl-copy Hello world!

# copy the list of files in Downloads
$ ls ~/Downloads | wl-copy

# copy an image file
$ wl-copy < ~/Pictures/photo.png

# paste to a file
$ wl-paste > clipboard.txt

# grep each pasted word in file source.c
$ for word in $(wl-paste); do grep $word source.c; done

# copy the previous command
$ wl-copy "!!"

# replace the current selection with the list of types it's offered in
$ wl-paste --list-types | wl-copy
```

유용하게 꽤 많으나, 주로 wl-copy를 사용할 듯 하다. 

