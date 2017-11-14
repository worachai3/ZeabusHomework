#!/usr/bin/python2

import rospy

from std_msgs.msg import String
from simple_cal_service_client.srv import simple_cal_service

def callback(req):
    response = String()
    first_num = req.request.first_num
    second_num = req.request.second_num
    if req.request.sign == 'plus':
        res = '%d + %d = %d'%(first_num, second_num, first_num + second_num)
    elif req.request.sign == 'minus':
        res = '%d - %d = %d'%(first_num, second_num, first_num - second_num)

    response.data = res

    return response.data

def main():
    rospy.init_node('simple_cal_service_node', anonymous=True)
    service = rospy.Service('simple_cal_service', simple_cal_service,callback)
    rospy.spin()

if __name__=='__main__':
    main()
