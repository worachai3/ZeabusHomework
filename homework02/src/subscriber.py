#!/usr/bin/python2

import rospy
from homework00_01.msg import homework01

def callback(recieveData):
    msg = recieveData
    sign = msg.sign
    num_1 = msg.num_1
    num_2 = msg.num_2
    if sign == 'plus':
        print('%d+%d = %d'%(num_1, num_2, num_1+num_2))
    elif sign == 'minus':
        print('%d-%d = %d'%(num_1, num_2, num_1-num_2))

if __name__=='__main__':
    rospy.init_node('node_subscriber', anonymous=True)
    rospy.Subscriber('/topic_publisher', homework01, callback)
    rospy.spin()
