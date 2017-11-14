#!/usr/bin/python2

import rospy
from geometry_msgs.msg import Twist

class control_robot():

    global stop
    global get_speed

    def stop():
        msg = Twist()
        msg.linear.x = 0
        msg.linear.y = 0
        msg.linear.z = 0

        msg.angular.x = 0
        msg.angular.y = 0
        msg.angular.z = 0

        return msg

    def get_speed(direction):
        msg = stop()
        if direction == 'U':
            msg.linear.z = 1
        elif direction == 'D':
            msg.linear.z = -1
        elif direction == 'L':
            msg.linear.y = 1
        elif direction == 'R':
            msg.linear.y = -1
        elif direction == 'F':
            msg.linear.x = 1
        elif direction == 'B':
            msg.linear.x = -1

        return msg

    def move(msg):
        vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        vel_msg = stop()

        while not rospy.is_shutdown():
            # set speed to 0
            vel_msg = stop()
            vel_pub.publish(vel_msg)

            rospy.loginfo('Linear: x: %f, y: %f, z: %f'%(vel_msg.linear.x, vel_msg.linear.y, vel_msg.linear.z))
            # get direction, speed and distance from user
            direction = raw_input('Input direction(U, D, L, R, F, B): ').upper()
            distance = int(raw_input('Input distance '))

            vel_msg = get_speed(direction)
            vel_pub.publish(vel_msg)

            # wait for robot to get to destination
            print 'Wait for robot to get to destination.'

            rospy.sleep(distance)


if __name__ == '__main__':
    rospy.init_node('robot_control_node', anonymous=True)
    control_robot().move()
