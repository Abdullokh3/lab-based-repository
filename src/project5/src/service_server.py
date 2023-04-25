#!/usr/bin/env python

import rospy
from project5.srv import OddEvenCheck, OddEvenCheckResponse

def determineOddEven(req):
    remainder = req.number % 2

    if remainder == 0:
        return OddEvenCheckResponse(answer="Even")
    elif remainder == 1:
        return OddEvenCheckResponse(answer="Odd")
    else:
        return OddEvenCheckResponse(answer="Invalid input")

if __name__ == "__main__":
    rospy.init_node("odd_even_service_server_node")
    service = rospy.Service("odd_even_check", OddEvenCheck, determineOddEven)
    rospy.loginfo("Odd Even Check Server Running...")
    rospy.spin()

