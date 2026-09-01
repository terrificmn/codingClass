# usb convertor 에러
아래와 같은 에러 발생 시.. 심볼릭 링크까지, 또는  /dev/ttyUSB* 시리즈로 잘 인식은 되나

제대로 된 기능이 안되는 현상 발생 (업로드 및 통신이 안됨) 

```
[    5.896877] usb 3-3: cp210x converter now attached to ttyUSB1
[    5.903335] usb 3-6.2: FTDI USB Serial Device converter now attached to ttyUSB0
[    5.957594] usb 3-7: pl2303 converter now attached to ttyUSB2
[  666.391201] pl2303 ttyUSB2: pl2303_get_line_request - failed: -32
[  666.392060] pl2303 ttyUSB2: pl2303_get_line_request - failed: -32
[  668.448319] pl2303 ttyUSB2: error sending break = -32
[  675.045453] pl2303 ttyUSB2: pl2303_get_line_request - failed: -32
[  675.046393] pl2303 ttyUSB2: pl2303_get_line_request - failed: -32
[  675.444064] pl2303 ttyUSB2: error sending break = -32
[  675.488359] pl2303 ttyUSB2: pl2303_get_line_request - failed: -32
[  675.488879] pl2303 ttyUSB2: pl2303_get_line_request - failed: -32
[  679.633568] pl2303 ttyUSB2: error sending break = -32
[  753.713272] ftdi_sio ttyUSB0: FTDI USB Serial Device converter now disconnected from ttyUSB0
[  758.277335] usb 3-6.2: FTDI USB Serial Device converter now attached to ttyUSB0
[  773.196025] pl2303 ttyUSB2: pl2303_get_line_request - failed: -32
[  773.196608] pl2303 ttyUSB2: pl2303_get_line_request - failed: -32
[  780.463203] pl2303 ttyUSB2: pl2303_get_line_request - failed: -32
[  780.606976] pl2303 ttyUSB2: pl2303_get_line_request - failed: -32
[  785.271196] pl2303 ttyUSB2: error sending break = -32
```

이번 케이스에서는 실제 시리얼 통신 컨버터와, 업로드용 컨버터를 서로 바꿔서 적용했을 때 
제대로 작동안하는 현상이 있었다. 다시 바꾼 후에 제대로 인식하니 잘 작동함.   

물론 하드웨어가 고장이 날 수도 있겠지만? 비슷한 상황이 생긴다면 통신포트와 udevadm 명령어 등을 이용해서  
맞는 장치와 통신을 하고 있는지 확인해 볼 것.  

> 어쨋든 이번은 라벨링이 잘못 되어서 반대로 연결한 상황이었음.;;
