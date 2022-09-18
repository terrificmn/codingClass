```
<node pkg="tf" type="static_transform_publisher" name="camera_broadcaster"
    args="-1.0 0.0 0.2 -0.5 0.5 -0.5 0.5 chassis camera2 10" />

<node name="camera_info" pkg="rostopic" type="rostopic"
    args="pub camera_info sensor_msgs/CameraInfo
    ....
    >
```