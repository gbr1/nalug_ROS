#!/usr/bin/env python

import rospy
#import messages type 
#from <category.msg> import <Type>


def talker():
    # ----- publisher ----- #
    
    pub = rospy.Publisher('<Topic name>', <Type>, queue_size=<n>)
    
    rospy.init_node('<Node name>', anonymous=True)
    
    rate = rospy.Rate(<Hz>)

    while not rospy.is_shutdown():
        #message creation
        
        #publish
        pub.publish(<message>)

        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass