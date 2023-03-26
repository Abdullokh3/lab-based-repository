#include "ros/ros.h"

#include "std_msgs/Float32.h"

float limit_of_speed;

ros::Publisher speed_pub;


void subCallback(const std_msgs::Float32::ConstPtr& rpm)
{
  
  ros::NodeHandle callback_node_handle;
  
  if (callback_node_handle.getParam("limit_of_speed", limit_of_speed))
   {
      std_msgs::Float32 speed_msg;

      // Speed = Circumference * Rev/s
      speed_msg.data = (2 * limit_of_speed * 3.14159) * (rpm->data / 60);
 
      speed_pub.publish(speed_msg);
   }
   else 
   {
      ROS_WARN(" No Value set for speed_limit server parameter.");
   }
  
}


int main(int argc, char **argv)
{
  ros::init(argc, argv, "limit_of_speed_node");

  ros::NodeHandle node_handle;

  speed_pub = node_handle.advertise<std_msgs::Float32>("speed", 200);

  ros::Subscriber rpm_sub = node_handle.subscribe("rpm", 200, subCallback);

  ros::spin();

  return 0;
}