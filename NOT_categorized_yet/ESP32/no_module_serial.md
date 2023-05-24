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