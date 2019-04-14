#!/usr/bin/env python

import rospy
#importo messaggi 
#from <categoria.msg> import <Tipo>

def callback(messaggio):
    #faccio cose
    
def listener():

    rospy.init_node(nomeNodo, anonymous=True)

    rospy.Subscriber(nomeTopic, String, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
