#! /usr/bin/python

import rospy
from std_msgs.msg import Float32

WHEEL_RADIUS = 0.0

def sub_callback(rpm):
    global WHEEL_RADIUS, pub

    if rospy.has_param('wheel_radius'):
        WHEEL_RADIUS = rospy.get_param('wheel_radius')
        speed_msg = Float32()
        speed_msg.data = (2 * WHEEL_RADIUS * 3.14159) * (rpm.data / 60)
        pub.publish(speed_msg)
    else:
        rospy.logwarn('No value set for wheel_radius server parameter.')

def main():
    global pub

    rospy.init_node('speed_calc_node')
    pub = rospy.Publisher('speed', Float32, queue_size=10)
    rospy.Subscriber('rpm', Float32, sub_callback)
    rospy.spin()

if __name__ == '__main__':
    main()
