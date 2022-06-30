
원래 코드

```cpp
class ImageSubscriber : public rclcpp::Node {
public:
    ImageSubscriber() : Node("image_subscriber") {
        using std::placeholders::_1;
        //현재 토픽은 테스트용
        subscription_ = this->create_subscription<sensor_msgs::msg::Image>(
            "/cam0/camera1/image_raw", 10, 
            std::bind(&ImageSubscriber::image_callback, this, _1)
        );  //topic은 gazebo 용, 바꿀려면 dolly_custom의 sdf 파일 변경해야함(camera link)
    }

    bool get_chk_if_green() {
        return this->is_green;
    }

protected:
    bool is_green;
    std::vector<int> center_pixel; //테스트 중.. getter로 활용할 방법 

private:
    rclcpp::Subscription<sensor_msgs::msg::Image>::SharedPtr subscription_;
    cv_bridge::CvImagePtr cvImgPtr;
    
    void image_callback(const sensor_msgs::msg::Image::SharedPtr msg) {     
        //rclcpp::WallRate loop_rate(500ms); 
        //rclcpp::sleep_for(500ms); //std::chrono::milliseconds(500)
        RCLCPP_INFO(this->get_logger(), "started_image_callback");
            try {
                // convert ROS image msg to OpenCV image
                cvImgPtr = cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::BGR8);
                //cvImgPtr = cv_bridge::toCvCopy(msg, msg->encoding);
            
            } catch(cv_bridge::Exception& e) {
                RCLCPP_ERROR(this->get_logger(), "cv_bridge exception: %s", e.what());
                return;
            }
            
            // 640 x 480
            // std::cout << "cols: " << cvImgPtr->image.cols << std::endl;  // width
            // std::cout << "rows: " << cvImgPtr->image.rows << std::endl;  // height
            int width = cvImgPtr->image.cols;
            int height = cvImgPtr->image.rows;

            cv::Mat cvtImgToRgb; 
            // RGB 변환
            cv::cvtColor(cvImgPtr->image, cvtImgToRgb, CV_BGR2RGB);

            // 첫 번째 포인트 at<cv::Vec3b>(row, col)
            int pointX1 = cvtImgToRgb.at<cv::Vec3b>(height/2, width/2)[0];  //x, y 딱 중간  //Red channel
            int pointY1 = cvtImgToRgb.at<cv::Vec3b>(height/2, width/2)[1];  //Green channel
            int pointZ1 = cvtImgToRgb.at<cv::Vec3b>(height/2, width/2)[2];  //Blue channel  // openCV BRG 상태라면 반대
            // 두 번째 포인트
            int pointX2 = cvtImgToRgb.at<cv::Vec3b>(200, 280)[0]; //x, y
            int pointY2 = cvtImgToRgb.at<cv::Vec3b>(200, 280)[1];
            int pointZ2 = cvtImgToRgb.at<cv::Vec3b>(200, 280)[2];
            // 세 번째 포인트
            int pointX3 = cvtImgToRgb.at<cv::Vec3b>(200, 360)[0]; //x, y
            int pointY3 = cvtImgToRgb.at<cv::Vec3b>(200, 360)[1];
            int pointZ3 = cvtImgToRgb.at<cv::Vec3b>(200, 360)[2];

            // std::cout << "RED Channel: " << pointX1 << std::endl;
            // std::cout << "GREEN Channel: " << pointY1 << std::endl;
            // std::cout << "BLUE Channel: " << pointZ1 << std::endl;

            bool is_green_p1, is_green_p2, is_green_p3;
            
            // 첫번째 포인트에 Y(Green)가 높으면 true주기
            if ((pointY1 > pointX1) && (pointY1 > pointZ1)) {
                is_green_p1 = true;
            } else {
                is_green_p1 = false;
            }

            // 두 번째 포인트에 Y가 높으면 true
            if ((pointY2 > pointX2) && (pointY2 > pointZ2)) {
                is_green_p2 = true;
            } else {
                is_green_p2 = false;
            }

            // 세번째 포인트도 무조건 Y가 높게
            if ((pointY3 > pointX3) && (pointY3 > pointZ3)) {
                is_green_p3 = true;
            } else {
                is_green_p3 = false;
            }
            
            // 3 포인트 모두 그린이 높으면 true 
            if (is_green_p1 == true && is_green_p2 == true && is_green_p3 == true) {
                this->is_green = true;
                this->center_pixel = {pointY1, pointY3};
                //RCLCPP_WARN(this->get_logger(), "a high chance of green");
            } else {
                this->is_green = false;
                this->center_pixel = {pointY1, pointY3};
                //RCLCPP_WARN(this->get_logger(), "a low chance of green");
            }

    }
};
```



포인터부분으로 변경된 코드
정리필요함!!!!!!!!!!!!!!!!


```cpp
class ImageSubscriber : public rclcpp::Node {
public:
    ImageSubscriber() : Node("image_subscriber") {
        using std::placeholders::_1;
        // 가제보 시뮬용   //"/cam0_sensor/image_raw" --터틀봇
        subscription_ = this->create_subscription<sensor_msgs::msg::Image>(
            "/cam0/camera1/image_raw", 10, 
            std::bind(&ImageSubscriber::image_callback, this, _1)
        );  
    }

    bool get_chk_if_green() {
        return this->is_green;
    }

protected:
    bool is_green;
    bool result_green;

private:
    rclcpp::Subscription<sensor_msgs::msg::Image>::SharedPtr subscription_;
    cv_bridge::CvImagePtr cvImgPtr;
    
    void image_callback(const sensor_msgs::msg::Image::SharedPtr msg) {     
        //RCLCPP_INFO(this->get_logger(), "started_image_callback");
            try {
                // convert ROS image msg to OpenCV image
                cvImgPtr = cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::BGR8);
            
            } catch(cv_bridge::Exception& e) {
                RCLCPP_ERROR(this->get_logger(), "cv_bridge exception: %s", e.what());
                return;
            }
            
            // 640 x 480
            // std::cout << "cols: " << cvImgPtr->image.cols << std::endl;  // width
            // std::cout << "rows: " << cvImgPtr->image.rows << std::endl;  // height
            int width = cvImgPtr->image.cols;
            int height = cvImgPtr->image.rows;
            int rgbPoint1[3], rgbPoint2[3], rgbPoint3[3]; //3곳의 RGB채널값 저장 array

            cv::Mat cvtImgToRgb; 
            // RGB 변환
            cv::cvtColor(cvImgPtr->image, cvtImgToRgb, CV_BGR2RGB);

            // at<cv::Vec3b>(row, col)
            // 첫 번째 포인트
            rgbPoint1[0] = cvtImgToRgb.at<cv::Vec3b>(height/2, width/2)[0];  //x, y 딱 중간  //Red channel
            rgbPoint1[1] = cvtImgToRgb.at<cv::Vec3b>(height/2, width/2)[1];  //Green channel
            rgbPoint1[2] = cvtImgToRgb.at<cv::Vec3b>(height/2, width/2)[2];  //Blue channel  // openCV BRG 상태라면 반대
            
            // 두 번째 포인트
            rgbPoint2[0] = cvtImgToRgb.at<cv::Vec3b>(200, 280)[0]; //(x, y) // x
            rgbPoint2[1] = cvtImgToRgb.at<cv::Vec3b>(200, 280)[1]; // y
            rgbPoint2[2] = cvtImgToRgb.at<cv::Vec3b>(200, 280)[2]; // z

            // 세 번째 포인트
            rgbPoint3[0] = cvtImgToRgb.at<cv::Vec3b>(200, 360)[0];  //x   //(x, y)
            rgbPoint3[1] = cvtImgToRgb.at<cv::Vec3b>(200, 360)[1];  //y
            rgbPoint3[2] = cvtImgToRgb.at<cv::Vec3b>(200, 360)[2];  //z

            this->img_green_check(&rgbPoint1[0], &rgbPoint2[0], &rgbPoint3[0], 3);  //주소값만 넘겨주기
    }

    bool img_green_check(int* spot1Ptr, int* spot2Ptr, int* spot3Ptr, int size) {
        // array주소값만 받아서 처리

        bool is_spot_green[3];
        
        // 더블pointer에 포인터를 담을 수 있게 또 포인터로 만들어준다
        int** rgbPointPPtr = new int*[size];  // pointer poninter 할당해주기 //allocate (array)
        for(int i=0; i < size; i++) {
            rgbPointPPtr[i] = new int[size];
        }
        
        // referencing
        rgbPointPPtr[0] = spot1Ptr;
        rgbPointPPtr[1] = spot2Ptr;
        rgbPointPPtr[2] = spot3Ptr;
        
        for (int i=0; i < size; i++) {
            // 각각 포인트별로 Y(Green, 인덱스1)가 높으면 true주기   // indexing 0: r, 1: g, 2: b
            if ((rgbPointPPtr[i][1] > rgbPointPPtr[i][0]) && (rgbPointPPtr[i][1] > rgbPointPPtr[i][2])) {
                is_spot_green[i] = true;
            } else {
                is_spot_green[i] = false;
            }
        }

        //deallocate
        delete[] rgbPointPPtr;
        rgbPointPPtr = NULL;

        // 세곳의 포인트 모두 그린이 높으면 true 리턴
        if(is_spot_green[0] == true && is_spot_green[1] == true && is_spot_green[2] == true) {
            RCLCPP_WARN(this->get_logger(), "a high chance of green");
            return this->is_green = true;
        } else {
            RCLCPP_WARN(this->get_logger(), "a low chance of green");
            return this->is_green = false;
        }
    }
};
```

