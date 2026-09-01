05Aug 에러~~   
send goal을 했을 때 에러 발생 ~~ 그 전까지는 특별한 에러 없었음  

 WARN] [1659695481.146462865, 9.566000000]: Timed out waiting for transform from base_footprint to map to become available before running costmap, tf error: canTransform: target_frame map does not exist.. canTransform returned after 9.566 timeout was 0.1.
[ WARN] [1659695481.199374952, 9.619000000]: global_costmap: Parameter "plugins" not provided, loading pre-Hydro parameters
[ INFO] [1659695481.203488640, 9.623000000]: global_costmap: Using plugin "static_layer"
[ INFO] [1659695481.206556990, 9.626000000]: Requesting the map...
[ INFO] [1659695481.408310669, 9.828000000]: Resizing costmap to 1504 X 1504 at 0.050000 m/pix
[ INFO] [1659695481.507597178, 9.927000000]: Received a 1504 X 1504 map at 0.050000 m/pix
[ INFO] [1659695481.509737017, 9.930000000]: global_costmap: Using plugin "obstacle_layer"
[ INFO] [1659695481.511666600, 9.932000000]:     Subscribed to Topics: laser_scan_sensor
[ INFO] [1659695481.518409974, 9.938000000]: global_costmap: Using plugin "inflation_layer"
[ WARN] [1659695481.534282763, 9.954000000]: local_costmap: Pre-Hydro parameter "static_map" unused since "plugins" is provided
[ WARN] [1659695481.534407988, 9.954000000]: local_costmap: Pre-Hydro parameter "map_type" unused since "plugins" is provided
[ INFO] [1659695481.534629468, 9.954000000]: local_costmap: Using plugin "obstacle_layer"
[ INFO] [1659695481.536085000, 9.956000000]:     Subscribed to Topics: laser_scan_sensor
[ INFO] [1659695481.540935650, 9.961000000]: local_costmap: Using plugin "inflation_layer"
[ INFO] [1659695481.551753865, 9.972000000]: Created local_planner base_local_planner/TrajectoryPlannerROS
[ INFO] [1659695481.553657465, 9.973000000]: Sim period is set to 0.10
[ WARN] [1659695481.555892879, 9.976000000]: Trajectory Rollout planner initialized with param meter_scoring not set. Set it to true to make your settings robust against changes of costmap resolution.
[ INFO] [1659695481.753378181, 10.173000000]: Recovery behavior will clear layer 'obstacles'
[ INFO] [1659695481.755467529, 10.175000000]: Recovery behavior will clear layer 'obstacles'
[ INFO] [1659695481.765940038, 10.186000000]: odom received!
QObject::connect: Cannot queue arguments of type 'QVector<int>'
(Make sure 'QVector<int>' is registered using qRegisterMetaType().)
QObject::connect: Cannot queue arguments of type 'QVector<int>'
(Make sure 'QVector<int>' is registered using qRegisterMetaType().)
[ INFO] [1659695483.872832788, 12.289000000]: Initial odometry pose is Origin: (-4.8840035854257161523e-06 4.9121311966756180733e-06 0)
Rotation (RPY): (0, 0, -0.0043833176299778011178)

[ INFO] [1659695483.873000310, 12.289000000]: Datum (latitude, longitude, altitude) is (-30.060224, -51.173913, 10.205444)
[ INFO] [1659695483.873073164, 12.289000000]: Datum UTM coordinate is (483236.593072, 6674528.556970) zone 22
[ INFO] [1659695483.907060555, 12.324000000]: Corrected for magnetic declination of 0.000000, user-specified offset of 1.570796 and meridian convergence of 0.001520. Transform heading factor is now 1.572317
[ INFO] [1659695483.907141299, 12.324000000]: Transform world frame pose is: Origin: (-5.4715791409933244119e-06 5.0164161930620550402e-06 0)
Rotation (RPY): (0, 0, -0.0044485074164674308361)

[ INFO] [1659695483.907213530, 12.324000000]: World frame->cartesian transform is Origin: (-6671524.7677133847028 523068.9549331299495 -10.025311576419301929)
Rotation (RPY): (0, 0, -1.5767654688917429606)

[ WARN] [1659695500.133065287, 28.532000000]: The goal sent to the navfn planner is off the global costmap. Planning will always fail to this goal.
[ WARN] [1659695501.231280947, 29.630000000]: The goal sent to the navfn planner is off the global costmap. Planning will always fail to this goal.
[ WARN] [1659695502.231805328, 30.630000000]: The goal sent to the navfn planner is off the global costmap. Planning will always fail to this goal.
[ WARN] [1659695503.336381591, 31.733000000]: The goal sent to the navfn planner is off the global costmap. Planning will always fail to this goal.
[ WARN] [1659695504.430088093, 32.826000000]: The goal sent to the navfn planner is off the global costmap. Planning will always fail to this goal.
[ WARN] [1659695505.214722926, 33.610000000]: Clearing both costmaps to unstuck robot (3.00m).
[ WARN] [1659695505.432340410, 33.827000000]: The goal sent to the navfn planner is off the global costmap. Planning will always fail to this goal.
[ WARN] [1659695506.442473173, 34.833000000]: The goal sent to the navfn planner is off the global costmap. Planning will always fail to this goal.
[ WARN] [1659695507.525297071, 35.916000000]: The goal sent to the navfn planner is off the global costmap. Planning will always fail to this goal.
[ WARN] [1659695508.525893288, 36.917000000]: The goal sent to the navfn planner is off the global costmap. Planning will always fail to this goal.
[ WARN] [1659695509.525495803, 37.916000000]: The goal sent to the navfn planner is off the global costmap. Planning will always fail to this goal.
[ WARN] [1659695510.318744553, 38.709000000]: Rotate recovery behavior started.


