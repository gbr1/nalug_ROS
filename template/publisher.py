#!/usr/bin/env python

import rospy
#importo messaggi 
#from <categoria.msg> import <Tipo>


def talker():
    #modifica il publisher
    pub = rospy.Publisher(nomeTopic, Tipo, queue_size=10)
    rospy.init_node(nomeNodo, anonymous=True)
    rate = rospy.Rate(frequenza) #in Hz
    while not rospy.is_shutdown():
        #crea messaggio
        pub.publish(messaggio)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass