#!/usr/bin/python2

import rospy

def main():
    rospy.init_node('simple_cal', anonymous=True)

    sign = raw_input('Input sign(1(+), 2(-)): ')
    first_num = input('Input 1st num: ')
    second_num = input('Input 2nd num: ')

    if sign == '1':
        print '%0.2f'%(first_num+second_num)

    elif sign == '2':
        print '%f'%(first_num-second_num)

    else:
        print 'Error please enter either 1 for + or 2 for -.'

if __name__=='__main__':
    main()
