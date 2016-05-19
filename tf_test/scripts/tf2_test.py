#!/usr/bin/env python
# Lucas Walter

import math
import rospy
import tf2_ros


rospy.init_node('tf_test')

tf_buffer = tf2_ros.Buffer()
tl = tf2_ros.TransformListener(tf_buffer)

parent = rospy.get_param("~parent", "parent")
child = rospy.get_param("~child", "child")
rospy.loginfo(parent + ' to ' + child)


# tl.waitForTransform(child, parent, rospy.Time(), rospy.Duration(4.0))

fr = 0.0
old_pos = 0.0
old_time = 0.0
while not rospy.is_shutdown():
    rospy.sleep(1.0)
    # try:
    trans = tf_buffer.lookup_transform(child, parent, rospy.Time())
    # except:  # tf.LookupException as e:
    #     rospy.logerr(e)
    #     continue

    rospy.loginfo("\n" + str(trans))
