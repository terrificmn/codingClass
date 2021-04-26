import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile
import os
import pathlib
import cv2

from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image


from object_detection.utils import ops as utils_ops
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util


# 버전호환성 확인하는 것
# patch tf1 into `utils.ops`
utils_ops.tf = tf.compat.v1
# Patch the location of gfile
tf.gfile = tf.io.gfile


# 로컬에 설치된 레이블 mscoco_label_map 가져오기
PATH_TO_LABELS = '/home/sgtOcta/Workspace/tensorflow/models/research/object_detection/data/mscoco_label_map.pbtxt'
category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS, use_display_name=True)

# If you want to test the code with your images, just add path to the images to the TEST_IMAGE_PATHS.
#PATH_TO_TEST_IMAGES_DIR = pathlib.Path('models/research/object_detection/test_images')
PATH_TO_TEST_IMAGES_DIR = pathlib.Path('data/images')
TEST_IMAGE_PATHS = sorted(list(PATH_TO_TEST_IMAGES_DIR.glob("*.jpg")))
print(TEST_IMAGE_PATHS)



# 모델을 다운로드
def load_model(model_name, model_date):
    base_url = 'http://download.tensorflow.org/models/object_detection/tf2/'
    model_file = model_name + '.tar.gz'
    model_dir = tf.keras.utils.get_file(
        fname=model_name, 
        origin=base_url + model_date + '/' + model_file,
        untar=True)

    model_dir = pathlib.Path(model_dir)/"saved_model"

    model = tf.saved_model.load(str(model_dir))

    return model

# Enable GPU dynamic memory allocation
gpus = tf.config.experimental.list_physical_devices('GPU')

# 모델 불러오기 함수호출 load_model()
#model_name = 'ssd_mobilenet_v1_coco_2017_11_17'

# 다운로드 주소에서 링크주소를 마우스 오른쪽 버튼 누른 후 카피해서 사용
# tensorflow의 매뉴얼에서 파일명 규칙은 주소에서 날짜부분은 model_date에 넣어주고
# model_name 은 압축파일 확장자를 뺀 상태로 넣어주면 됨
# https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/auto_examples/plot_object_detection_saved_model.html

model_name= 'faster_rcnn_resnet152_v1_800x1333_coco17_gpu-8'
#model_name = 'ssd_mobilenet_v1_coco_2017_11_17'
model_date = '20200711'

#model_name = 'mask_rcnn_inception_resnet_v2_1024x1024_coco17_gpu-8'
detection_model = load_model(model_name, model_date)
print(detection_model.signatures['serving_default'].output_dtypes)
print(detection_model.signatures['serving_default'].output_shapes)



def run_inference_for_single_image(model, image):
    # 넘파이 array로 바꿔준다. 해당모델의 이미지를 추론 (예측) 해서
    image = np.asarray(image)
    # The input needs to be a tensor, convert it using `tf.convert_to_tensor`.
    input_tensor = tf.convert_to_tensor(image)
    # The model expects a batch of images, so add an axis with `tf.newaxis`.
    input_tensor = input_tensor[tf.newaxis,...]

    # Run inference
    model_fn = model.signatures['serving_default']
    output_dict = model_fn(input_tensor) #결과 받아옴

    # All outputs are batches tensors.
    # Convert to numpy arrays, and take index [0] to remove the batch dimension.
    # We're only interested in the first num_detections.
    num_detections = int(output_dict.pop('num_detections'))
    output_dict = {key:value[0, :num_detections].numpy() 
                    for key,value in output_dict.items()}
    output_dict['num_detections'] = num_detections

    # detection_classes should be ints.
    output_dict['detection_classes'] = output_dict['detection_classes'].astype(np.int64)
    
    # Handle models with masks:
    if 'detection_masks' in output_dict:
        output_dict['detection_masks'] = tf.convert_to_tensor(output_dict['detection_masks'], dtype=tf.float32)
        output_dict['detection_boxes'] = tf.convert_to_tensor(output_dict['detection_boxes'], dtype=tf.float32)
        # Reframe the the bbox mask to the image size.
        detection_masks_reframed = utils_ops.reframe_box_masks_to_image_masks(
                output_dict['detection_masks'], output_dict['detection_boxes'],
                image.shape[0], image.shape[1])  
        detection_masks_reframed = tf.cast(detection_masks_reframed > 0.5,
                                        tf.uint8)
        output_dict['detection_masks_reframed'] = detection_masks_reframed.numpy()
        
    return output_dict



def show_inference(model, image_np): 
    # 기존 이미지로 받을 때와는 다르게 이미지만 보낼때는 경로가 필요했지만 동영상은 이미지 경로가 필요없으므로 파라미터변경
    # the array based representation of the image will be used later in order to prepare the
    # result image with boxes and labels on it.

    # Actual detection. 결과 예측, 함수호출
    output_dict = run_inference_for_single_image(model, image_np)
    # Visualization of the results of a detection.
    
    # 비주얼 라이징하기
    vis_util.visualize_boxes_and_labels_on_image_array(
        image_np,
        np.array(output_dict['detection_boxes']),
        output_dict['detection_classes'],
        output_dict['detection_scores'],
        category_index,
        instance_masks=output_dict.get('detection_masks_reframed',None),
        use_normalized_coordinates=True,
        line_thickness=8)

    cv2.imshow('result', image_np)

import time
# 카메라의 영상 실행
#cap = cv2.VideoCapture(0) # 캠 영상 실행
cap = cv2.VideoCapture('data/video/video.mp4')

if cap.isOpened() == False:
    print("error occured to start to play a video")

else:
    while cap.isOpened():
        ret, frame = cap.read() #동영상의 사진을 하나씩 frame에 넣어준다
        if ret == True:
            #cv2.imshow('Frame', frame)
            startTime = time.time()
            show_inference(detection_model, frame)  # 이미지 경로는 필요없고 이미 np array로 받아왔기때문에 frame넘겨주면 됨
            endTime = time.time()
            print(endTime-startTime)
            if cv2.waitKey(25) & 0xFF == 27:
                break
        else:
            break

    cap.release()

cv2.waitKey()
cv2.destroyAllWindows()








