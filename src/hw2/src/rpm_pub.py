#! /usr/bin/python

import rospy
from std_msgs.msg import Float32

RPM = 60

def main():
    rospy.init_node('rpm_pub_node')
    pub = rospy.Publisher('rpm', Float32, queue_size=10)
    rate = rospy.Rate(10)
    rospy.loginfo('Publishing RPM...')

    while not rospy.is_shutdown():
        msg = Float32()
        msg.data = RPM
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    main()
