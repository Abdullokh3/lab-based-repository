# master_midterm_assignment

- Creating the midterm
```bash
<img width="1102" alt="Screenshot 2023-04-20 at 4 42 49 PM" src="https://user-images.githubusercontent.com/90837231/233607154-d63b2a3c-4ffd-40dd-bb79-51c70c1b7653.png">
<img width="1280" alt="Screenshot 2023-04-20 at 5 06 37 PM" src="https://user-images.githubusercontent.com/90837231/233607180-cc0693b6-df7f-44c1-8042-52b6e632e170.png">
<img width="1280" alt="Screenshot 2023-04-20 at 5 06 40 PM" src="https://user-images.githubusercontent.com/90837231/233607215-55a3e333-47f4-4fec-95d6-cf9df98e6402.png">
```
- Start roscore
```bash

<img width="1280" alt="Screenshot 2023-04-20 at 5 06 43 PM" src="https://user-images.githubusercontent.com/90837231/233607271-18090d4d-e74b-4900-b92f-960de2e1b3c6.png">
 
<img width="1280" alt="Screenshot 2023-04-20 at 5 06 46 PM" src="https://user-images.githubusercontent.com/90837231/233607304-69bf359d-1975-436c-aaa3-24c8cc31905d.png">
<img width="1280" alt="Screenshot 2023-04-20 at 5 06 49 PM" src="https://user-images.githubusercontent.com/90837231/233607332-b8ef0aab-a777-49b4-9591-05aba5ea0498.png">


### Task #1
- check the midterm services in the new tab
```bash
ros@ubuntu:~/catkin_ws/midterm$ source devel/setup.bash 
ros@ubuntu:~/catkin_ws/midterm$ rossrv list
--- omitted ---
map_msgs/ProjectedMapsInfo
map_msgs/SaveMap
map_msgs/SetMapProjections
midterm/WeatherStation <-------------
nav_msgs/GetMap
nav_msgs/GetPlan
nav_msgs/LoadMap
nav_msgs/SetMap
--- omitted ---
ros@ubuntu:~/catkin_ws/midterm$ rosrun midterm service_server
[ INFO] [1650766939.649994468]: Weather Station Server Running...
```
- Test the service in the new tab
```bash
ros@ubuntu:~/catkin_ws/midterm$ source devel/setup.bash
ros@ubuntu:~/catkin_ws/midterm$ rosservice list
/rosout/get_loggers
/rosout/set_logger_level
/weather_station <-------------
/weather_station_server_node/get_loggers
/weather_station_server_node/set_logger_level
ros@ubuntu:~/catkin_ws/midterm$ rosservice call /weather_station Seoul
weather_type: "sunny"
ros@ubuntu:~/catkin_ws/midterm$ rosservice call /weather_station Istanbul
weather_type: "cloudy"
ros@ubuntu:~/catkin_ws/midterm$ rosservice call /weather_station Sydney
weather_type: "windy"
ros@ubuntu:~/catkin_ws/midterm$ rosrun midterm service_client 
Type 'exit' to quit
Enter Location: Istanbul
The weather is cloudy
Enter Location: Seoul
The weather is sunny
Enter Location: Sydney
The weather is windy
Enter Location: Siberia
The weather is stormy
Enter Location: London
The weather is rainy
Enter Location: exit
[ INFO] [1650767144.709564698]: Exiting Application...
ros@ubuntu:~/catkin_ws/midterm$ 
```
### Task #2
- Raunch speed_check_simulator.launch
  - speed_limit is pre-defined (70 km/h) and can not be modified```
```bash
ros@ubuntu:~/catkin_ws/midterm$ source devel/setup.bash
ros@ubuntu:~/catkin_ws/midterm$ roslaunch midterm speed_check_simulator.launch 
... logging to /home/ros/.ros/log/c198ccb2-c374-11ec-b91c-974d1a0c2498/roslaunch-ubuntu-75746.log
Checking log directory for disk usage. This may take a while.
Press Ctrl-C to interrupt
Done checking log file disk usage. Usage is <1GB.

started roslaunch server http://ubuntu:44113/

SUMMARY
========

PARAMETERS
 * /plate_number: 1234.0
 * /rosdistro: noetic
 * /rosversion: 1.15.14
 * /speed: 50.0

NODES
  /
    speed_check_node1 (midterm/speed_check)
    speed_limit_node1 (midterm/speed_limit)

ROS_MASTER_URI=http://localhost:11311

process[speed_limit_node1-1]: started with pid [75760]
process[speed_check_node1-2]: started with pid [75761]
```
- Test changing speed 
  - ```plate_number``` is pre-defined (1234) and can be modified by ```rosparam set plate_number <new_value>```
  - ```speed``` is pre-defined (50 km/h) and can be modified by ```rosparam set speed <new_value>```
```bash
os@ubuntu:~/catkin_ws/midterm$ rosparam list
/plate_number <-------------
/rosdistro
/roslaunch/uris/host_ubuntu__33377
/roslaunch/uris/host_ubuntu__44113
/rosversion
/run_id
/speed <-------------
ros@ubuntu:~/catkin_ws/midterm$ rosparam dump
plate_number: 1234.0 <-------------
rosdistro: 'noetic

  '
roslaunch:
  uris:
    host_ubuntu__33377: http://ubuntu:33377/
    host_ubuntu__44113: http://ubuntu:44113/
rosversion: '1.15.14

  '
run_id: c198ccb2-c374-11ec-b91c-974d1a0c2498
speed: 50.0 <-------------
ros@ubuntu:~/catkin_ws/midterm$ rostopic list
/rosout
/rosout_agg
/speed <-------------
/speed_limit <-------------
ros@ubuntu:~/catkin_ws/midterm$ 
```
  - Initially there will not be any output as the ```speed``` does not exceed the ```speed_limit```
```bash
ros@ubuntu:~/catkin_ws/midterm$ rostopic echo speed
_
```
  - Increase ```speed``` that exceeds ```speed_limit``` (higher than 70) in a new tab
 ```bash
 ros@ubuntu:~/catkin_ws/midterm$ rosparam set speed 75
 ros@ubuntu:~/catkin_ws/midterm$
 ```
   -  and the ```plate_number``` will be printed
 ```bash
 ros@ubuntu:~/catkin_ws/midterm$ rostopic echo speed
 data: 1234.0
 ---
 data: 1234.0
 ---
 data: 1234.0
 ---
 data: 1234.0
 ---
 data: 1234.0
 ---
 data: 1234.0
 ---
 data: 1234.0
 ---
 data: 1234.0
 ---
 data: 1234.0
 ---
 data: 1234.0
 ---
 data: 1234.0
 ---
 data: 1234.0
 ...
 ```
