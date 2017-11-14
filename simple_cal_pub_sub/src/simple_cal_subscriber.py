#!/usr/bin/python2

import rospy

from simple_cal.msg import simple_cal_msg

def callback(recieveData):
    if recieveData.sign == 'plus':
        sign = '+'
    elif recieveData == 'minus':
        sign = '-'
    first_num = recieveData.first_num
    second_num = recieveData.second_num
    msg = '%d %s %d = '%(first_num, sign, second_num)

    if sign == '+':
        msg += '%s'%(first_num + second_num)
    elif sign == '-':
        msg += '%s'%(first_num - second_num)

    rospy.loginfo(msg)

def main():
    rospy.init_node('simple_cal_subscriber', anonymous=True)
    rospy.Subscriber('/simple_cal_publisher', simple_cal_msg, callback)
    rospy.spin()

if __name__=='__main__':
    main()
