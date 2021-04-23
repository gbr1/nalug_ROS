#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
from math import sin
from math import cos


def talker():
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    rospy.init_node('joint_control',anonymous=True)
    rate=rospy.Rate(100)
    angle1=0.0
    angle2=0.0
    msg=JointState()
    while not rospy.is_shutdown():
        msg.header=Header()
        msg.header.stamp=rospy.Time.now()
        msg.name=['joint1', 'joint2']
        msg.position=[sin(angle1), cos(angle2)]
        angle1=angle1+0.01
        angle2=angle1
        pub.publish(msg)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass