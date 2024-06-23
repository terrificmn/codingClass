    rapidjson::Type t = body_ref[v_keys[i].c_str()].GetType();
        ROS_WARN("type is %d", t);
        if(body_ref[v_keys[i].c_str()].IsObject()) {
        }