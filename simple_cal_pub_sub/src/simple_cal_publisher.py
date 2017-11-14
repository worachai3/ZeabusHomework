#!/usr/bin/python2

import rospy

from simple_cal.msg import simple_cal_msg

def publisher():
    pub = rospy.Publisher('/simple_cal_publisher', simple_cal_msg, queue_size=10)
    inp = simple_cal_msg()

    while not rospy.is_shutdown():
        inp.sign = 'plus'
        inp.first_num = 1
        inp.second_num = 2

        pub.publish(inp)

def main():
    rospy.init_node('simple_cal_publisher', anonymous=True)
    publisher()

if __name__=='__main__':
    main()

