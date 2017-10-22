#!/usr/bin/python2

import rospy
from homework03.srv import homework03_service
from homework00_01.msg import homework01
from std_msgs.msg import String

def client_request():
    rospy.wait_for_service('calculator_service')
    client = rospy.ServiceProxy('calculator_service',homework03_service)
    print('Press plus or minus or exit')
    sign = String(raw_input().lower())
    if sign.data == 'exit':
        print('Exit')
        exit()
    num_1 = int(input('Number1: '))
    num_2 = int(input('Number2: '))
    res = client(sign,num_1,num_2)
    print(res.res_result.data)
    client_request()

if __name__=='__main__':
    rospy.init_node('node_client',anonymous=True)
    client_request()
