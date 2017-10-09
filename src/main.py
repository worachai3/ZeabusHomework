#!/usr/bin/python2
import rospy

if __name__=='__main__':
    rospy.init_node('plus_minus_program')
    operation = raw_input()
    first = input()
    second = input()
    if operation == '1':
        print '%s'%(first+second)
    elif operation == '2':
        print '%s'%(first-second)
