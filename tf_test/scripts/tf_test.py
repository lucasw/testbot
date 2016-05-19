#!/usr/bin/env python
# Lucas Walter

import math
import rospy
import tf

from sensor_msgs.msg import JointState


rospy.init_node('tf_test')

tl = tf.TransformListener()

parent = rospy.get_param("~parent", "parent")
child = rospy.get_param("~child", "child")
rospy.loginfo(parent + ' to ' + child)

# js_pub = rospy.Publisher("joint_state", JointState, queue_size=1)

while not rospy.is_shutdown():
    rospy.sleep(1.0)
    if False:
        joint_state = JointState()
        joint_state.header.stamp = rospy.Time.now()
        joint_state.header.frame
        js_pub.publish(joint_state)

    try:
        pos, quat = tl.lookupTransform(child, parent, rospy.Time())
    except tf.LookupException as e:
        rospy.logerr(e)
        continue

    rospy.loginfo("\n" + str(pos) + "\n" + str(quat))
