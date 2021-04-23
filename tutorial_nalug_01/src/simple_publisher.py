#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('pub', String, queue_size=10)
    rospy.init_node('talker',anonymous=True)
    rate=rospy.Rate(1)
    while not rospy.is_shutdown():
        msg_string = "messaggio inviato con timestamp %s" % rospy.get_time()
        rospy.loginfo(msg_string)
        pub.publish(msg_string)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass