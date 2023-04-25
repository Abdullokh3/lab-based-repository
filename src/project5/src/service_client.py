#!/usr/bin/env python

import rospy
from project5.srv import OddEvenCheck

if __name__ == '__main__':
    rospy.init_node('odd_even_service_client_node')

    client = rospy.ServiceProxy('odd_even_check', OddEvenCheck)

    print("Type '0' to quit")

    while not rospy.is_shutdown():
        input_num = int(input("Enter an Integer: "))

        if input_num == 0:
            rospy.loginfo("Exiting Application...")
            break

        response = client(input_num)

        rospy.loginfo("The number is " + response.answer)

