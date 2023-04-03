execute_process(COMMAND "/home/abdullokh/catkin_ws/hw2_ws/build/hw2/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/abdullokh/catkin_ws/hw2_ws/build/hw2/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
