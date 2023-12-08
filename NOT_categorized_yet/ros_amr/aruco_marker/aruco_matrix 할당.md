# aruco marker

cv::Mat 로 만들어진 변수에 array 또는 값 넣어줄 때

```cpp
std::vector<cv::Vec3d> r_vecs, t_vecs;
cv::Mat camera_matrix, dist_coeffs;
```

이렇게 있을 경우   
cv::Mat1d() 를 이용해서 row3, col3 으로 만들어 준다. 
```cpp
camera_matrix = (cv::Mat1d(3, 3) << camera_array[0], 0, camera_array[2], 0, camera_array[4], camera_array[5], 0, 0, 1);
//또는
camera_matrix = (cv::Mat1d(3, 3) << 0.231, 0, 0.24123, 0, 0.12314, 1.4123, 0, 0, 1);
```

카메라 intrinsic 아래 처럼 3x3 형태로 만들어준다.
```
 fx   0  cx
  0  fy  cy
  0   0   1 
```


dsit_coeffs 는 5개 배열이 필요하므로 1, 5로 만들어준다. 
```cpp
dist_coeffs = (cv::Mat1d(1, 5) << 0.21, -1.3, 0, 0, 0);
```

물론 4, 5, 또는 8개의 배열일 경우도 있다고 한다. 그럴 경우에는..
```cpp
cv::Mat distortion_coefficients = (Mat1d(1, 4) << k1, k2, p1, p2);
cv::Mat distortion_coefficients = (Mat1d(1, 5) << k1, k2, p1, p2, k3);
cv::Mat distortion_coefficients = (Mat1d(1, 8) << k1, k2, p1, p2, k3, k4, k5, k6);
```

카메라 은 
cpp_aruco_marker 패키지의 maker_calibration.cpp 를 참고하자 




## pose Estimate 을 한 후에 
t_vecs의 cv::Vec3d 를 할당 하려면   

```cpp
double x = t_vecs.at(0)[0];
double y = t_vecs.at(0)[1];
double z = t_vecs.at(0)[2];
```
배열 첫 번째의 값을 불러와 주면 된다.

> 만약 t_vecs 벡터가 만들어지지 않은 경우에 접근을 하면 세그먼트 오류가 나므로 예외처리를 해주고 시작


