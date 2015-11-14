#!/usr/bin/env python

import rospy
import subprocess

rospy.init_node('wrap_shell_script')

# TODO get other script arguments?
#namespace = rospy.get_namespace()
# assume the shell script only wants private params
namespace = rospy.get_name()

script = rospy.get_param("~script")
pkg    = rospy.get_param("~pkg")

subprocess.call('ROS_NAMESPACE=' + namespace + ' rosrun ' + pkg + ' ' + script, shell=True)

