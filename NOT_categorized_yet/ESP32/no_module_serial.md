# esp32 serial 못 찾을 경우
아래와 같이 No module named 'serial' 이라고 나오면서 에러 발생할 경우
```
Traceback (most recent call last):
  File "/home/sgtocta/.arduino15/packages/esp32/tools/esptool_py/4.5.1/esptool.py", line 31, in <module>
    import esptool
  File "/home/sgtocta/.arduino15/packages/esp32/tools/esptool_py/4.5.1/esptool/__init__.py", line 41, in <module>
    from esptool.cmds import (
  File "/home/sgtocta/.arduino15/packages/esp32/tools/esptool_py/4.5.1/esptool/cmds.py", line 14, in <module>
    from .bin_image import ELFFile, ImageSegment, LoadFirmwareImage
  File "/home/sgtocta/.arduino15/packages/esp32/tools/esptool_py/4.5.1/esptool/bin_image.py", line 14, in <module>
    from .loader import ESPLoader
  File "/home/sgtocta/.arduino15/packages/esp32/tools/esptool_py/4.5.1/esptool/loader.py", line 30, in <module>
    import serial
ModuleNotFoundError: No module named 'serial'

exit status 1
```

esp32에 업로드를 할 때 위와 같은 에러가 발생한다면 serial 을 설치해야한다 
```
python3 -m pip install pyserial
```

이제 업로드 시에 문제가 없다

## esp32 Failed to commnicate with the flash chip
업로드 할 경우에 아래와 같은 워닝과 함께 업로드 실패하는 경우
```
WARNING: Failed to communicate with the flash chip, read/write operations will fail. Try checking the chip connections or removing any other hardware connected to IOs.
```

5v, vin에 나가는 출력이 있다면 빼준 후에 업로드 해준다.  

5v 입력을 해도 되는 경우도 있지만, 5v 를 제거하면 되는 경우도 있다   

이번 경우에는 5v 로 출력이 나갔는데 이를 빼고 업로드하니 성공했다


