#!/usr/bin/env python

import rospy
#importo messaggi 
from <category.msg> import <Type>

def callback(message):
    #do something - e.g. print
    print(message.data)
    
def listener():

    rospy.init_node('<Node name>', anonymous=True)

    rospy.Subscriber('<Topic to subscribe>', <Type>, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()