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

js_pub = rospy.Publisher("test_joint/joint_state", JointState, queue_size=1)

# tl.waitForTransform(child, parent, rospy.Time(), rospy.Duration(4.0))

fr = 0.0
old_pos = 0.0
old_time = 0.0
while not rospy.is_shutdown():
    rospy.sleep(1.0)
    if True:
        fr += 0.05
        pos = 0.5 * math.sin(fr)
        joint_state = JointState()
        joint_state.header.stamp = rospy.Time.now()
        cur_time = joint_state.header.stamp.to_sec()
        # TODO(lucasw) does frame_id matter?
        # joint_state.header.frame_id
        joint_state.name.append('test_joint')
        joint_state.position.append(pos)
        vel = (pos - old_pos)/(cur_time - old_time)
        joint_state.velocity.append(vel)
        effort = vel * 2.0
        joint_state.effort.append(effort)
        js_pub.publish(joint_state)

        old_pos = pos
        old_time = cur_time

    # https://github.com/ros/geometry/issues/117
    try:
        pos, quat = tl.lookupTransform(child, parent, rospy.Time())
    except tf.LookupException as e:
        rospy.logerr(e)
        continue

    rospy.loginfo("\n" + str(pos) + "\n" + str(quat))
