########### SUCCESS with amcl

######### 4.2 / 0.76 | max_vel_x/y: 0.0 | acc_lim_x: 1.5 , acc_lim_theta: 2.5, acc_lim_y: 1.5

######### path_distance_bias: 10.0, goal_distance_bias: 32.0 | occdist_scale: 0.02

  

####### cartoros without amcl ######

### the same above except, path_distance_bias: 32.0

### fail -- max_vel_x/y 0.0 or it goes wrong

####### cartoros ###### the same params from move_base version but only one thing different

#### path_distance_bias: 32.0

  
  

##### 3.6 / 0.76 | max_vel_x/y: 0.0 | acc_lim_x: 1.5, acc_lim_theta: 2.5, acc_lim_y: 1.5

## path_distance_bias: 12.0, goal_distance_bias: 32.0 | forward_point_distance: 0.325

## succ | return fail

  

##### 4.0 / 0.76 | max_vel_x/y: 0.8/-0.8 | acc_lim_x: 1.5, acc_lim_theta: 2.5, acc_lim_y: 1.5

## path_distance_bias: 12.0, goal_distance_bias: 32.0 | forward_point_distance: 0.325

## succ | return fail

  

##### acc_lim_theta: 3.2 fail

  

##### 4.0 / 0.76 | max_vel_x/y: 0.8/0.0 | acc_lim_x: 1.5, acc_lim_theta: 2.5, acc_lim_y: 1.5

## path_distance_bias: 12.0, goal_distance_bias: 32.0 | forward_point_distance: 0.325

## succ | in fail | return fail

  

### max_vel_x/y: 1.0/0.0 -- fail

### 1.0/-1.0 in/out success | return fail

### 0.1/-0.1 fail

### 0.6/-0.6 in-out suc | return fail

### 0.6/0.1 out fail | return fail

### 0.7/-0.7 in-out suc | return fail

### RETURN FAIL

### 0.0 / 0.0

  

##### door pass 7.0 / 0.5 wall crash

##### door pass 7.0 / 0.65 wall 3-5cm fail

##### door pass 7.0 / 0.65 wall 6-10cm half fail

##### door pass 7.0 / 0.75 wall 6-10cm half success elevator fail

##### door pass 6.5 / 0.8 wall 10-15cm door in/out pass but fail to return

##### door pass 6.3 / 0.85 wall 15cm door in/out pass but fail to return

##### door pass 6.0 / 0.9 wall 15cm door in/out pass but fail to return

##### door pass 6.0 / 0.99 wall 15cm door in/out/return pass

##### door pass 5.5 / 1.1 wall 25cm door in/out/return pass

##### door pass 5.1 / 1.2 wall 30cm door in/out/return pass | acc_lim_x: 2.0 | acc_lim_theta: 1.5 path_distance_bias: 6.0 goal_distance_bias: 24.0

##### door pass 5.5 / 1.43 wall 40cm door in/out/return pass | acc_lim_x: 2.0 | acc_lim_theta: 1.5 path_distance_bias: 6.0 goal_distance_bias: 32.0

#### with max_vel_trans: 0.5 max_vel_theta: 0.45

  

##### 4.2/1.55 door out/in pass , return pass | twice fail

##### 4.3/1.51 door out/in pass , return pass | twice fail

##### 4.3/1.53 door out/in fail ,

##### 4.2/1.56 door out/in fail/success

##### 4.0/1.56 door out/in success | twice half success out return pass , in fail

#### 4.1/1.56 fail

##### 4.1/1.52 in/out suc | return fail | center ok ---

### acc_lim_x: 1.0 , acc_lim_theta: 2.5, acc_lim_y: 2.0 (dwa_local_planner_param)

### path_distance_bias: 6.0 | occdist_scale: 0.02 ---> occdist_scale x2 turn fail

  

##### 4.7/1.26 in/out suc | return fail | center ok ---

### acc_lim_x: 1.0 , acc_lim_theta: 2.5, acc_lim_y: 2.0 (dwa_local_planner_param)

### path_distance_bias: 12.0 | occdist_scale: 0.02

  

##### 5.2/1.1 in/out suc | return fail | center ok ---

### acc_lim_x: 1.0 , acc_lim_theta: 2.5, acc_lim_y: 2.0 (dwa_local_planner_param)

### path_distance_bias: 12.0 | occdist_scale: 0.02

  

##### 4.9/1.05 in/out suc | return fail | center ok ---

### acc_lim_x: 1.0 , acc_lim_theta: 2.5, acc_lim_y: 2.0 (dwa_local_planner_param)

### path_distance_bias: 12.0 | occdist_scale: 0.02

  

##### 5.3/0.95 in/out suc | return fail | center ok ---

### acc_lim_x: 1.0 , acc_lim_theta: 2.5, acc_lim_y: 2.0 (dwa_local_planner_param)

### path_distance_bias: 12.0 | occdist_scale: 0.02

  

##### 5.6/0.95 in/out suc | return fail | center ok ---

### acc_lim_x: 1.0 , acc_lim_theta: 2.5, acc_lim_y: 2.0 (dwa_local_planner_param)

### path_distance_bias: 12.0 | occdist_scale: 0.02

  

##### 6.2/0.86 6.4/0.81 in/out suc | return fail | center ok ---

### acc_lim_x: 1.0 , acc_lim_theta: 2.5, acc_lim_y: 2.0 (dwa_local_planner_param)

### path_distance_bias: 12.0 | occdist_scale: 0.02

  

#### 7.0 / 0.76 out fail

### 5.6 / 0.91 in/out pass return fail | occdist_scale: 0.015

### 6.2/ 0.86 in/out pass return fail \occdist_scale: 0.02

### 7.9/ 0.66 in/out pass return fail \occdist_scale: 0.02

### 8.4/ 0.6 in/out pass return fail \occdist_scale: 0.02

### 8.8/ 0.5 in/out pass return fail \occdist_scale: 0.02 quite space enough .. but return fail

  

### 5.9/ 0.81 in/out | return pass occdist_scale is not a problem // it was max_vel_y and min_vel_y

### 5.8/ 0.86 in/out sucss | return pass | max_vel_y: 0.6 , min_vel_y: 0.1

  

### 7.3 / 0.85 in/out pass | return fail | min_vel_y&max:0