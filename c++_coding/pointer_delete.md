업데이트 필요!!!

CameraDriver* camObj = nullptr;

    if(!camObj) {
        ROS_ERROR("IT's nullptr");
        ROS_WARN("first address: %p", camObj);
    } 

     camObj = new CameraDriver;
    CameraStatus camStatusObj;
    ROS_WARN("first new address: %p", camObj);



// delete
       delete camObj;
            camObj = nullptr;


다시 생성

ROS_ERROR("IT's nullptr");
                ROS_WARN("after delete second address: %p", camObj);
                camObj->test(); // 되었어도 아마도 delete가 잘 안된 듯 하다. 기능이 작동한다;;;
                camObj = new CameraDriver; // delete 된 후에 다시 할당
                ROS_WARN("new address: %p", camObj);



