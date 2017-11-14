#!/usr/bin/python2

import rospy

from simple_cal_service_client.srv import simple_cal_service
from simple_cal.msg import simple_cal_msg

def client_request():
    rospy.wait_for_service('simple_cal_service')
    client = rospy.ServiceProxy('simple_cal_service', simple_cal_service)
    request = simple_cal_msg

    request.sign = ''

    while request.sign != 'exit':
        request.sign = ''
        while request.sign != 'plus' and request.sign != 'minus' and request.sign != 'exit':
            request.sign = raw_input('Input plus, minus or exit: ').lower()

        if request.sign != 'exit':
            request.first_num = input('1st Number: ')
            request.second_num = input('2nd Number: ')

            print client(request)

    print 'Exit'

def main():
    client_request()

if __name__=='__main__':
    rospy.init_node('simple_cal_client_node', anonymous=True)
    main()
