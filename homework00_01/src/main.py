#!/usr/bin/python2
import rospy

if __name__ == '__main__':
    rospy.init_node('simple_calulator')
    sign = raw_input()
    num_1 = input()
    num_2 = input()
    if sign == '1':
        print '%d' % (num_1+num_2)
    elif sign == '2':
        print '%d' % (num_1-num_2)
