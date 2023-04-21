#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32

SPEED_LIMIT = 80.0

def main():
    rospy.init_node("speed_limit_node")

    speed_limit = rospy.Publisher("speed_limit", Float32, queue_size=10)

    pub_rate = rospy.Rate(10)  # Publish rate 10 Hz

    rospy.loginfo("Publishing SPEED LIMIT...")

    while not rospy.is_shutdown():

        msg = Float32()
        msg.data = SPEED_LIMIT

        speed_limit.publish(msg)

        pub_rate.sleep()

if __name__ == '__main__':
    main()

