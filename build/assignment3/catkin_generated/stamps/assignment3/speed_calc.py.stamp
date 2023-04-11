#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32

WHEEL_RADIUS = rospy.get_param("~wheel_radius", 0.1) # 0.1 is the default value if the parameter is not defined

def subCallback(rpm):
    global WHEEL_RADIUS

    speed_pub = rospy.Publisher("speed", Float32, queue_size=10)

    # Speed = Circumference * Rev/s
    speed = (2 * WHEEL_RADIUS * 3.14159) * (rpm.data / 60)
    speed_msg = Float32(speed)

    speed_pub.publish(speed_msg)

def main():
    rospy.init_node("speed_calc_node", anonymous=True)
    rospy.Subscriber("rpm", Float32, subCallback)
    rospy.spin()

if __name__ == '__main__':
    main()

