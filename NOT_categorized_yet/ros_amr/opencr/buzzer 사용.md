`pitches.h` is often part of a sketch, not a library. An example of this is the official "**02.Digital > toneMelody**" example sketch that comes with the Arduino IDE:

에서 사용하면 된다.   

[깃허브 examples](https://github.com/arduino/arduino-examples/tree/main/examples/02.Digital/toneMelody)

> pitches.h 파일의 내용을 복사해서 include 디렉토리에 만들어준다

```cpp
#include "pitches.h"

// notes in the melody:
int melody[] = {
  NOTE_C4, NOTE_G3, NOTE_G3, NOTE_A3, NOTE_G3, 0, NOTE_B3, NOTE_C4
};

// note durations: 4 = quarter note, 8 = eighth note, etc.:
int noteDurations[] = {
  4, 8, 8, 4, 4, 4, 4, 4
};

void setup() {
  // iterate over the notes of the melody:
  for (int thisNote = 0; thisNote < 8; thisNote++) {

    // to calculate the note duration, take one second
    // divided by the note type.
    //e.g. quarter note = 1000 / 4, eighth note = 1000/8, etc.
    int noteDuration = 1000 / noteDurations[thisNote];
    tone(BDPIN_BUZZER, melody[thisNote], noteDuration);

    // to distinguish the notes, set a minimum time between them.
    // the note's duration + 30% seems to work well:
    int pauseBetweenNotes = noteDuration * 1.30;
    delay(pauseBetweenNotes);
    // stop the tone playing:
    noTone(BDPIN_BUZZER);
  }
}

void loop() {
  // no need to repeat the melody.
}
```

아주 간단한 소리를 내는데 훌륭할 듯 하다. 위의 코드는 setup() 안에 넣어주면 한 번 하고 끝나고  
loop() 에 넣어주면 무한 멜로디 반복하게 된다

> loop() 에는 내용이 없더라도 함수 자체는 존재해야한다
