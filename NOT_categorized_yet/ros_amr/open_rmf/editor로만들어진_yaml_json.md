참고 ...  
traffic-editor 를 통해서 만들어진 yaml 파일

대략 이런식으로 생겼다.
```yaml
coordinate_system: reference_image
crowd_sim:
  agent_groups:
    - {agents_name: [], agents_number: 0, group_id: 0, profile_selector: external_agent, state_selector: external_static, x: 0, y: 0}
  agent_profiles:
    - {ORCA_tau: 1, ORCA_tauObst: 0.40000000000000002, class: 1, max_accel: 0, max_angle_vel: 0, max_neighbors: 10, max_speed: 0, name: external_agent, neighbor_dist: 5, obstacle_set: 1, pref_speed: 0, r: 0.25}
  enable: 0
  goal_sets: []
  model_types: []
  obstacle_set: {class: 1, file_name: L1_navmesh.nav, type: nav_mesh}
  states:
    - {final: 1, goal_set: -1, name: external_static, navmesh_file_name: ""}
  transitions: []
  update_time_step: 0.10000000000000001
graphs:
  {}
levels:
  L1:
    doors:
      - [48, 56, {motion_axis: [1, end], motion_degrees: [3, 90], motion_direction: [2, -1], name: [1, "null"], plugin: [1, normal], right_left_ratio: [3, 1], type: [1, hinged]}]
      - [50, 51, {motion_axis: [1, end], motion_degrees: [3, 90], motion_direction: [2, -1], name: [1, "null"], plugin: [1, normal], right_left_ratio: [3, 1], type: [1, hinged]}]
      - [45, 47, {motion_axis: [1, end], motion_degrees: [3, 90], motion_direction: [2, -1], name: [1, "null"], plugin: [1, normal], right_left_ratio: [3, 1], type: [1, hinged]}]
      - [54, 55, {motion_axis: [1, start], motion_degrees: [3, 90], motion_direction: [2, -1], name: [1, "null"], plugin: [1, normal], right_left_ratio: [3, 1], type: [1, hinged]}]
      - [83, 81, {motion_axis: [1, start], motion_degrees: [3, 90], motion_direction: [2, -1], name: [1, "null"], plugin: [1, normal], right_left_ratio: [3, 1], type: [1, hinged]}]
    drawing:
      filename: theconstruct_office.png
    elevation: 0
    floors:
      - parameters: {ceiling_scale: [3, 1], ceiling_texture: [1, blue_linoleum], indoor: [2, 0], texture_name: [1, blue_linoleum], texture_rotation: [3, 0], texture_scale: [3, 1]}
        vertices: [42, 43, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]
    lanes:
      - [57, 58, {bidirectional: [4, true], demo_mock_floor_name: [1, ""], demo_mock_lift_name: [1, ""], graph_idx: [2, 0], orientation: [1, ""], speed_limit: [3, 0]}]
      - [58, 59, {bidirectional: [4, true], demo_mock_floor_name: [1, ""], demo_mock_lift_name: [1, ""], graph_idx: [2, 0], orientation: [1, ""], speed_limit: [3, 0]}]
      - [59, 60, {bidirectional: [4, true], demo_mock_floor_name: [1, ""], demo_mock_lift_name: [1, ""], graph_idx: [2, 0], orientation: [1, ""], speed_limit: [3, 0]}]
      - [60, 61, {bidirectional: [4, true], demo_mock_floor_name: [1, ""], demo_mock_lift_name: [1, ""], graph_idx: [2, 0], orientation: [1, ""], speed_limit: [3, 0]}]
      - [61, 62, {bidirectional: [4, true], demo_mock_floor_name: [1, ""], demo_mock_lift_name: [1, ""], graph_idx: [2, 0], orientation: [1, ""], speed_limit: [3, 0]}]
      - [62, 63, {bidirectional: [4, true], demo_mock_floor_name: [1, ""], demo_mock_lift_name: [1, ""], graph_idx: [2, 0], orientation: [1, ""], speed_limit: [3, 0]}]
      - [63, 64, {bidirectional: [4, true], demo_mock_floor_name: [1, ""], demo_mock_lift_name: [1, ""], graph_idx: [2, 0], orientation: [1, ""], speed_limit: [3, 0]}]
      - [64, 65, {bidirectional: [4, true], demo_mock_floor_name: [1, ""], demo_mock_lift_name: [1, ""], graph_idx: [2, 0], orientation: [1, ""], speed_limit: [3, 0]}]
      - [65, 66, {bidirectional: [4, true], demo_mock_floor_name: [1, ""], demo_mock_lift_name: [1, ""], graph_idx: [2, 0], orientation: [1, ""], speed_limit: [3, 0]}]
      - [66, 67, {bidirectional: [4, true], demo_mock_floor_name: [1, ""], demo_mock_lift_name: [1, ""], graph_idx: [2, 0], orientation: [1, ""], speed_limit: [3, 0]}]
      - [67, 68, {bidirectional: [4, true], demo_mock_floor_name: [1, ""], demo_mock_lift_name: [1, ""], graph_idx: [2, 0], orientation: [1, ""], speed_limit: [3, 0]}]
      - [68, 60, {bidirectional: [4, true], demo_mock_floor_name: [1, ""], demo_mock_lift_name: [1, ""], graph_idx: [2, 0], orientation: [1, ""], speed_limit: [3, 0]}]
      - [58, 69, {bidirectional: [4, true], demo_mock_floor_name: [1, ""], demo_mock_lift_name: [1, ""], graph_idx: [2, 0], orientation: [1, ""], speed_limit: [3, 0]}]
      - [69, 70, {bidirectional: [4, true], demo_mock_floor_name: [1, ""], demo_mock_lift_name: [1, ""], graph_idx: [2, 0], orientation: [1, ""], speed_limit: [3, 0]}]
      - [70, 71, {bidirectional: [4, true], demo_mock_floor_name: [1, ""], demo_mock_lift_name: [1, ""], graph_idx: [2, 0], orientation: [1, ""], speed_limit: [3, 0]}]
      - [69, 72, {bidirectional: [4, true], demo_mock_floor_name: [1, ""], demo_mock_lift_name: [1, ""], graph_idx: [2, 0], orientation: [1, ""], speed_limit: [3, 0]}]
    layers:
      {}
    measurements:
      - [0, 1, {distance: [3, 8.7699999999999996]}]
    vertices:
      - [914.41099999999994, 230.077, 0, ""]
      - [914.41099999999994, 664.351, 0, ""]
      - [47.094000000000001, 22.864000000000001, 0, ""]
      - [613.78399999999999, 19.952999999999999, 0, ""]
      - [770.86199999999997, 242.55099999999999, 0, rick_charging_station, {is_charger: [4, true], is_holding_point: [4, true], is_parking_spot: [4, true]}]
      - [771.43499999999995, 314.80399999999997, 0, ""]
      - [806.98800000000006, 314.80399999999997, 0, coffee_countertop]
      - [806.98800000000006, 456.44200000000001, 0, table_1_top_right]
      - [745.63099999999997, 457.01600000000002, 0, table_1_top_left]
      - [741.61599999999999, 509.77199999999999, 0, table_1_top_left_2]
      - [741.04300000000001, 554.5, 0, table_1_bottom_left_2]
      - [743.33699999999999, 602.09500000000003, 0, table_1_bottom_left]
      - [778.31600000000003, 600.94799999999998, 0, table_1_bottom]
      - [824.19100000000003, 602.66800000000001, 0, table_1_bottom_right]
      - [822.471, 553.35299999999995, 0, table_1_bottom_right_2]
      - [823.04399999999998, 513.21199999999999, 0, table_1_top_right_2]
      - [715.23800000000006, 314.80399999999997, 0, table_3]
      - [715.23800000000006, 345.76900000000001, 0, ""]
      - [678.53899999999999, 341.18200000000002, 0, ""]
      - [706.06299999999999, 262.62099999999998, 0, table_4]
      - [735.30899999999997, 260.327, 0, ""]
      - [608.57899999999995, 440.95999999999998, 0, morty_charging_station, {is_charger: [4, true], is_holding_point: [4, true], is_parking_spot: [4, true]}]
      - [673.37800000000004, 440.95999999999998, 0, ""]
      - [672.23099999999999, 480.52699999999999, 0, table_2_top]
      - [701.476, 480.52699999999999, 0, ""]
      - [694.02099999999996, 545.89800000000002, 0, table_2_bottom]
      - [639.54499999999996, 407.12700000000001, 0, ""]
      - [638.971, 364.69299999999998, 0, ""]
      - [592.53700000000003, 334.86000000000001, 0, ""]
      - [592.83100000000002, 319.887, 0, ""]
      - [593.12400000000002, 381.54199999999997, 0, ""]
      - [463.45600000000002, 361.077, 0, hallway, {is_passthrough_point: [4, true]}]
      - [296.85599999999999, 361.52499999999998, 0, ""]
      - [296.85599999999999, 454.67700000000002, 0, ""]
      - [460.76900000000001, 460.49900000000002, 0, ""]
      - [517.19799999999998, 460.49900000000002, 0, ""]
      - [518.09400000000005, 425.11900000000003, 0, rb1_shipping_position]
      - [517.64599999999996, 607.44899999999996, 0, ""]
      - [450.46600000000001, 646.90800000000002, 0, rb1_loading_position]
      - [451.77100000000002, 583.31600000000003, 0, ""]
      - [397.63600000000002, 583.64200000000005, 0, ""]
      - [397.63600000000002, 465.589, 0, ""]
      - [377.74299999999999, 423.19400000000002, 0, rb1_charging_station, {is_charger: [4, true], is_holding_point: [4, true], is_parking_spot: [4, true]}]
      - [272.41399999999999, 312.40300000000002, 0, student_table_3]
      - [272.41399999999999, 236.976, 0, student_table_2]
      - [272.70499999999998, 158.70599999999999, 0, student_table_1]
      - [268.435, 82.706999999999994, 0, teacher_table]
      - [297.298, 559.67499999999995, 0, turtlebot_lab]
      - [274.89100000000002, 617.05799999999999, 0, ""]
      - [273.798, 711.05799999999999, 0, ""]
      - [198.92599999999999, 709.41899999999998, 0, rodrigos_desk]
      - [197.833, 808.33699999999999, 0, ""]
      - [273.798, 807.24400000000003, 0, back_office_2]
      - [271.52100000000002, 892.01199999999994, 0, ""]
      - [117.64400000000001, 891.34900000000005, 0, back_office_3]
      - [120.297, 807.77800000000002, 0, back_office_1]
      - [734.25800000000004, 170.56200000000001, 0, ""]
      - [838.35699999999997, 149.678, 0, kitchen_table]
      - [896.875, 76.225999999999999, 0, fridge]
      - [961.46400000000006, 75.254999999999995, 0, kitchen]
      - [665.23099999999999, 136.44399999999999, 0, kitchen_sofa]
      - [235.77600000000001, 387.95699999999999, 0, student_table_4]
      - [758.00599999999997, 399.012, 0, ""]
    walls:
      - [2, 3, {alpha: [3, 1], texture_height: [3, 2.5], texture_name: [1, default], texture_scale: [3, 1], texture_width: [3, 1]}]
      - [3, 4, {alpha: [3, 1], texture_height: [3, 2.5], texture_name: [1, default], texture_scale: [3, 1], texture_width: [3, 1]}]
      - [4, 5, {alpha: [3, 1], texture_height: [3, 2.5], texture_name: [1, default], texture_scale: [3, 1], texture_width: [3, 1]}]
      - [5, 6, {alpha: [3, 1], texture_height: [3, 2.5], texture_name: [1, default], texture_scale: [3, 1], texture_width: [3, 1]}]
      - [6, 7, {alpha: [3, 1], texture_height: [3, 2.5], texture_name: [1, default], texture_scale: [3, 1], texture_width: [3, 1]}]
      - [7, 8, {alpha: [3, 1], texture_height: [3, 2.5], texture_name: [1, default], texture_scale: [3, 1], texture_width: [3, 1]}]
      - [8, 9, {alpha: [3, 1], texture_height: [3, 2.5], texture_name: [1, default], texture_scale: [3, 1], texture_width: [3, 1]}]
      - [9, 10, {alpha: [3, 1], texture_height: [3, 2.5], texture_name: [1, default], texture_scale: [3, 1], texture_width: [3, 1]}]
      - [10, 11, {alpha: [3, 1], texture_height: [3, 2.5], texture_name: [1, default], texture_scale: [3, 1], texture_width: [3, 1]}]
      - [11, 12, {alpha: [3, 1], texture_height: [3, 2.5], texture_name: [1, default], texture_scale: [3, 1], texture_width: [3, 1]}]
      - [12, 13, {alpha: [3, 1], texture_height: [3, 2.5], texture_name: [1, default], texture_scale: [3, 1], texture_width: [3, 1]}]
      - [13, 14, {alpha: [3, 1], texture_height: [3, 2.5], texture_name: [1, default], texture_scale: [3, 1], texture_width: [3, 1]}]
      - [14, 15, {alpha: [3, 1], texture_height: [3, 2.5], texture_name: [1, default], texture_scale: [3, 1], texture_width: [3, 1]}]
      - [15, 16, {alpha: [3, 1], texture_height: [3, 2.5], texture_name: [1, default], texture_scale: [3, 1], texture_width: [3, 1]}]
      - [16, 17, {alpha: [3, 1], texture_height: [3, 2.5], texture_name: [1, default], texture_scale: [3, 1], texture_width: [3, 1]}]
      - [17, 18, {alpha: [3, 1], texture_height: [3, 2.5], texture_name: [1, default], texture_scale: [3, 1], texture_width: [3, 1]}]
      - [18, 19, {alpha: [3, 1], texture_height: [3, 2.5], texture_name: [1, default], texture_scale: [3, 1], texture_width: [3, 1]}]
      - [19, 20, {alpha: [3, 1], texture_height: [3, 2.5], texture_name: [1, default], texture_scale: [3, 1], texture_width: [3, 1]}]
      - [20, 21, {alpha: [3, 1], texture_height: [3, 2.5], texture_name: [1, default], texture_scale: [3, 1], texture_width: [3, 1]}]
      - [21, 22, {alpha: [3, 1], texture_height: [3, 2.5], texture_name: [1, default], texture_scale: [3, 1], texture_width: [3, 1]}]
      - [22, 23, {alpha: [3, 1], texture_height: [3, 2.5], texture_name: [1, default], texture_scale: [3, 1], texture_width: [3, 1]}]
      - [23, 24, {alpha: [3, 1], texture_height: [3, 2.5], texture_name: [1, default], texture_scale: [3, 1], texture_width: [3, 1]}]
      - [24, 25, {alpha: [3, 1], texture_height: [3, 2.5], texture_name: [1, default], texture_scale: [3, 1], texture_width: [3, 1]}]
      - [25, 26, {alpha: [3, 1], texture_height: [3, 2.5], texture_name: [1, default], texture_scale: [3, 1], texture_width: [3, 1]}]
      - [26, 27, {alpha: [3, 1], texture_height: [3, 2.5], texture_name: [1, default], texture_scale: [3, 1], texture_width: [3, 1]}]
      - [27, 28, {alpha: [3, 1], texture_height: [3, 2.5], texture_name: [1, default], texture_scale: [3, 1], texture_width: [3, 1]}]
      - [28, 29, {alpha: [3, 1], texture_height: [3, 2.5], texture_name: [1, default], texture_scale: [3, 1], texture_width: [3, 1]}]
      - [29, 30, {alpha: [3, 1], texture_height: [3, 2.5], texture_name: [1, default], texture_scale: [3, 1], texture_width: [3, 1]}]
      - [30, 31, {alpha: [3, 1], texture_height: [3, 2.5], texture_name: [1, default], texture_scale: [3, 1], texture_width: [3, 1]}]
      - [31, 32, {alpha: [3, 1], texture_height: [3, 2.5], texture_name: [1, default], texture_scale: [3, 1], texture_width: [3, 1]}]
      - [32, 33, {alpha: [3, 1], texture_height: [3, 2.5], texture_name: [1, default], texture_scale: [3, 1], texture_width: [3, 1]}]
      - [33, 34, {alpha: [3, 1], texture_height: [3, 2.5], texture_name: [1, default], texture_scale: [3, 1], texture_width: [3, 1]}]
      - [34, 35, {alpha: [3, 1], texture_height: [3, 2.5], texture_name: [1, default], texture_scale: [3, 1], texture_width: [3, 1]}]
      - [35, 36, {alpha: [3, 1], texture_height: [3, 2.5], texture_name: [1, default], texture_scale: [3, 1], texture_width: [3, 1]}]
      - [36, 37, {alpha: [3, 1], texture_height: [3, 2.5], texture_name: [1, default], texture_scale: [3, 1], texture_width: [3, 1]}]
      - [37, 38, {alpha: [3, 1], texture_height: [3, 2.5], texture_name: [1, default], texture_scale: [3, 1], texture_width: [3, 1]}]
      - [38, 39, {alpha: [3, 1], texture_height: [3, 2.5], texture_name: [1, default], texture_scale: [3, 1], texture_width: [3, 1]}]
lifts: {}
name: theconstruct_office
```


## rmf 패키지의 json 구성

json파일 참고, valid_task 라는 Key로 리스트에 각각, "Loop", "Clean" 이란 테스크를 가지고 있고    
이 Valid_task는 task에 카테고리 안에 각각 설정이 되어 있다, 방문할 장소의 이름이 설정 되어 있는 듯    

기본적으로의 task에는 Delivery, Loop, Clean, Station, Patrol, Charging 등이 있다. 

```json
{ 
  "world_name" : "Starbots",
  "valid_task" : ["Loop", "Clean"],
  "task": {
    "Delivery": {},
    "Loop": {
      "places": [
        "rick_charging_station",
        "morty_charging_station",
        "coffee_bar",
        "table_1_top",
        "table_1_right",
        "table_1_left",
        "table_1_bottom",
        "table_2_top",
        "table_2_bottom",
        "table_3",
        "table_4"
      ]
    },
    "Clean": {
      "option": [
        "table_1_top",
        "table_2_top",
        "table_3",
        "table_4"
      ]
    },
    "Station": {},
    "Patrol": {},
    "Charging": {}
  }
}
```