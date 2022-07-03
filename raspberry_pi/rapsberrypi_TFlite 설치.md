먼저 라즈베리파이에 설치
```
echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
sudo apt-get update
sudo apt-get install python3-tflite-runtime
```

tflite_runtime을 사용하려면 코드 몇개를 바꿔주면 된다고 함  
아래 예를 보기  
Run an inference using tflite_runtime  

Instead of importing Interpreter from the tensorflow module,    
you now need to import it from tflite_runtime.

For example, after you install the package above, copy and run the label_image.py file.  
It will (probably) fail because you don't have the tensorflow library installed.  
To fix it, edit this line of the file:

import tensorflow as tf

So it instead reads:

import tflite_runtime.interpreter as tflite

And then change this line:

interpreter = tf.lite.Interpreter(model_path=args.model_file)

So it reads:

interpreter = tflite.Interpreter(model_path=args.model_file)

Now run label_image.py again. That's it! You're now executing TensorFlow Lite models.

깃허브를 라즈베리파이 클론시켜준다
```
git clone https://github.com/tensorflow/examples --depth 1
```

MobileNet model and labels file을 다운로드 받기. 먼저 디렉토리 이동
```
cd examples/lite/examples/object_detection/raspberry_pi

# The script takes an argument specifying where you want to save the model files
bash download.sh /tmp
```
bash 스크립트로 실행


그리고  example 코드 실행
```
python3 detect_picamera.py \
  --model /tmp/detect.tflite \
  --labels /tmp/coco_labels.txt
```

