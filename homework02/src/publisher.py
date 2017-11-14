#!/usr/bin/python2

import rospy
from homework00_01.msg import homework01

def publisher():
    inp = homework01()
    inp.sign = 'plus'
    inp.num_1 = 1
    inp.num_2 = 3
    pub = rospy.Publisher('/topic_publisher', homework01, queue_size=10)
    while not rospy.is_shutdown():
        pub.publish(inp)
        #print('%s %d %d'%(inp.sign, inp.num_1, inp.num_2))

if __name__=='__main__':
    rospy.init_node('node_publisher', anonymous=True)
    publisher()
