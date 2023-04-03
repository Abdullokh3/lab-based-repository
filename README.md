# Smart_Mobility_Service-lab-based
Smart_Mobility_Service (lab-based)


<br>
<h2> Hw2. it is inside another branch named master_for_hw2 file </h2>
<br>
<br>

In the homework_2, we were supposed to change the rpm_pub.cpp and speed_calc.cpp files into Python version. I could successfully did this task of converting them into their python version. It is possible to check the source files inside the master branch named master_for_hw2, specifically inside src/hw2/src folders.    

However, I could not build the 2 python version files successfully.  
Steps I've done are:    
* At first I created the package using catkin_create_pkg hw2 rospy, which is not roscpp, and I thought everything would build smoothly because of making it rospy. But it was not all, I browsed online resources on what else to change more to build the files finely and I had to make some modifications inside CMakeLists.txt file, it's possible to check my modifications inside src/hw2/CMakeLists.txt file. In the end I failed to build the files successfully. I searched so many online resources on how to fix the problem, none of them could solve the issue. Now I have no idea of what changes I should make so that I can build the files without problems.   
The output:    

<img width="1280" alt="Screenshot 2023-04-03 at 12 50 45 PM" src="https://user-images.githubusercontent.com/90837231/229411342-c7ed1c0d-769f-4098-9b31-85afb3b2a5f9.png">
