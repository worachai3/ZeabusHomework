#!/usr/bin/python2

import rospy
from homework03.srv import homework03_service
from homework00_01.msg import homework01
from std_msgs.msg import String

def callback(req):
    req_sign = req.req_sign.data
    req_num_1 = req.req_num_1
    req_num_2 = req.req_num_2
    if req_sign == 'plus':
        res_result = String('%d + %d = %d'%(req_num_1, req_num_2, req_num_1+req_num_2))
    elif req_sign == 'minus':
        res_result = String('%d - %d = %d'%(req_num_1, req_num_2, req_num_1-req_num_2))
    return res_result

if __name__ == '__main__':
    rospy.init_node('node_service', anonymous=True)
    service = rospy.Service('calculator_service', homework03_service, callback)
    rospy.spin()
