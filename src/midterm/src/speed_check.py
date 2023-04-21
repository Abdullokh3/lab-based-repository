#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32

PLATE_NUMBER = 0.0
SPEED = 0.0
speed_check = None

def subCallback(speed_limit):
    global PLATE_NUMBER, SPEED
    if rospy.has_param("plate_number"):
        PLATE_NUMBER = rospy.get_param("plate_number")
    else:
        rospy.logwarn("No Value set for plate_number parameter.")

    if rospy.has_param("speed"):
        SPEED = rospy.get_param("speed")
    else:
        rospy.logwarn("No Value set for speed parameter.")

    if SPEED > speed_limit.data:
        over_speed_msg = Float32()
        over_speed_msg.data = PLATE_NUMBER
        speed_check.publish(over_speed_msg)

def main():
    global speed_check

    rospy.init_node("speed_check_node")

    speed_check = rospy.Publisher("speed_check", Float32, queue_size=10)

    speed_limit = rospy.Subscriber("speed_limit", Float32, subCallback, queue_size=10)

    rospy.spin()

if __name__ == '__main__':
    main()

