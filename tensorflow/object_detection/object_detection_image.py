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


def load_model(model_name):
    base_url = 'http://download.tensorflow.org/models/object_detection/'
    model_file = model_name + '.tar.gz'
    model_dir = tf.keras.utils.get_file(
        fname=model_name, 
        origin=base_url + model_file,
        untar=True)

    model_dir = pathlib.Path(model_dir)/"saved_model"

    model = tf.saved_model.load(str(model_dir))

    return model


PATH_TO_LABELS = '/home/sgtOcta/Workspace/tensorflow/models/research/object_detection/data/mscoco_label_map.pbtxt'
category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS)

# If you want to test the code with your images, just add path to the images to the TEST_IMAGE_PATHS.
#PATH_TO_TEST_IMAGES_DIR = pathlib.Path('models/research/object_detection/test_images')
# test이미지
PATH_TO_TEST_IMAGES_DIR = pathlib.Path('data/images')
TEST_IMAGE_PATHS = sorted(list(PATH_TO_TEST_IMAGES_DIR.glob("*.jpg")))
print(TEST_IMAGE_PATHS)

# 모델 불러오기 , 함수호출
#model_name = 'ssd_mobilenet_v1_coco_2017_11_17'
model_name = 'faster_rcnn_inception_resnet_v2_640x640_coco17_tpu-8'
detection_model = load_model(model_name)
print(detection_model.signatures['serving_default'].output_dtypes)
print(detection_model.signatures['serving_default'].output_shapes)



def run_inference_for_single_image(model, image):
    image = np.asarray(image)
    # The input needs to be a tensor, convert it using `tf.convert_to_tensor`.
    input_tensor = tf.convert_to_tensor(image)
    # The model expects a batch of images, so add an axis with `tf.newaxis`.
    input_tensor = input_tensor[tf.newaxis,...]

    # Run inference
    model_fn = model.signatures['serving_default']
    output_dict = model_fn(input_tensor)

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



def show_inference(model, image_path):
    # the array based representation of the image will be used later in order to prepare the
    # result image with boxes and labels on it.
    image_np = np.array(Image.open(image_path)) # Image.open()은 RGB로 읽어들임. cv2라이브러리만 빼고 (BGR)
    image_np = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)  # cv2는 BGR로 읽기 때문에 변환해 준다
    # Actual detection.
    output_dict = run_inference_for_single_image(model, image_np)
    # Visualization of the results of a detection.
    
    vis_util.visualize_boxes_and_labels_on_image_array(
        image_np,
        np.array(output_dict['detection_boxes']),
        output_dict['detection_classes'],
        output_dict['detection_scores'],
        category_index,
        instance_masks=output_dict.get('detection_masks_reframed',None),
        use_normalized_coordinates=True,
        line_thickness=8)

    # 이미지 제목이 겹치면 한장만 나오기 때문에 윈도우창의 제목부분을 다르게해준다
    cv2.imshow(str(image_path), image_np)


# 함수 테스트 #위에 변수 있음 테스트 후 삭제 하기 (아래 2줄)
PATH_TO_TEST_IMAGES_DIR = pathlib.Path('data/images')
TEST_IMAGE_PATHS = sorted( list(PATH_TO_TEST_IMAGES_DIR.glob('*.jpg')) )



for image_path in TEST_IMAGE_PATHS:
    show_inference(detection_model, image_path)
    
    

cv2.waitKey()
cv2.destroyAllWindows()








