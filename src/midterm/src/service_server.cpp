#include "ros/ros.h"
#include "midterm/WeatherStation.h"
// #include "cpr.cpr.h"

bool determineWeatherType(midterm::WeatherStation::Request &req,
                          midterm::WeatherStation::Response &res)
{
  std::string location = req.GPS_location;
  
  if (location == "Incheon") res.weather_type = "sunny";
  else if (location == "Seoul") res.weather_type = "cloudy";
  else if (location == "Busan") res.weather_type = "windy";
  else if (location == "Jeju") res.weather_type = "rainy";
  else if (location == "Ansan") res.weather_type = "stormy";
  else return false;
  return true;
}


int main(int argc, char **argv)
{
  ros::init(argc, argv, "weather_station_server_node");
  ros::NodeHandle node_handle;
  ros::ServiceServer service = node_handle.advertiseService("weather_station", determineWeatherType);
  ROS_INFO("Weather Station Server Running...");
  ros::spin();
  return 0;
}
