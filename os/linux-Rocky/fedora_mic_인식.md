# mic 인식은 되나, input 이 없을 경우

내장 마이크가 아닌, 외장 마이크를 사용하려고 3.5 잭에 연결했는데 headphone으로 잘 잡히지만,  
전혀 input이 없어서 소리가 안 들어가는 경우에는   

TRRS 잭이 아닌, TRS 잭을 사용해보자.  

원래는 컴퓨터에는 4극 자리인 TRRS잭을 사용해야한다고 알고 있었는데, (아래에서 설명할) 설정을 해도  
전혀 input이 없었다.  

그래서 그냥 마지막으로 3극인 TRS 잭을 컴퓨터에 꽂아서 (headphone 단자에) 사용했더니,  
INPUT이 있다... 

> 노트북의 내장 마이크는 Digital Microphone - Alder Lake.. 라고 나오고   
외장 마이크는 Headphones Stereo Microphone - Alder Lake PCH-P High Definition Audio Controller   

뭔가 좀 이상하지만.. 뭐 되서 다행이다. 


## alsa.config 사용하기
성공하지는 못했지만 일단 참고로 남겨본다. 어쨋든 위의 경우가 아닌 경우에는   
alsa-base.conf 파일을 만들어서 적용할 수가 있다고 한다.  

먼저 모델명을 찾기
```
cat /proc/asound/card*/codec* | grep Codec
```

> card 0, 1 이런식으로 있는데 * 표시로 다 검색할 수 있다  
결과는 Codec: Realtek ALC256 이런식으로 나옴

[장치의 모델 찾기](https://www.kernel.org/doc/html/latest/sound/hd-audio/models.html)

위에서 alc256 처럼 자신의 모델명을 검색하면 이름이 나온다. (코덱)  


alsa-base파일 만들기 및 수정
```
sudo vi /etc/modprobe.d/alsa-base.conf
```

여기에 아래 라인을 추가해준다.
```
options snd-hda-intel model=alc256-eapd
```

그리고 재부팅하면 된다. 

