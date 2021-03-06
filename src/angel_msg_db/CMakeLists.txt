###############################
## cmake and project setting ##
###############################
cmake_minimum_required(VERSION 3.5)
project(angel_msg_db)


if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()


if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
#find_package(ament_cmake_ros REQUIRED)
find_package(rosidl_default_generators REQUIRED)

find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(ament_lint_auto REQUIRED)
ament_lint_auto_find_test_dependencies()
#find_package(message_package REQUIRED)






################################################
## Declare ROS messages, services and actions ##
################################################
rosidl_generate_interfaces(angel_msg_db
  "msg/Angeltest.msg"
  "msg/Angelrobottest.msg"
  "msg/Angeldb.msg"
  "msg/AngeldbStamped.msg"
  "msg/AngelData.msg"
  "msg/AngelDataStamped.msg"

  "srv/AngeldbGetData.srv"
  "srv/AngelRos.srv"
  # "srv/Tmsdbgetfurnituresinfo.srv"
  # "srv/Tmsdbgetmovablefurnituresinfo.srv"
  # "srv/Tmsdbgetobjectsinfo.srv"
  # "srv/Tmsdbgetpersoninfo.srv"
  # "srv/Tmsdbgetrobotsinfo.srv"
  # "srv/Tmsdbgetrobotinfo.srv"
  # "srv/Tmsdbgetpersonbehaviorinfo.srv"
  # "srv/Tmsdbgetpcdinfo.srv"
  # "srv/Tmsdbgettasklist.srv"
  # "srv/Tmsdbmissingobjectschecker.srv"
  # "srv/Tmsdbobjdt.srv"
  # "srv/TmsdbPlanning.srv"
  # "srv/Tmsdbfileconservation.srv"
  # "srv/TmsdbObjectsdata.srv"
  # "srv/Tmsdbgetunknownobject.srv"

  DEPENDENCIES 
  std_msgs
  sensor_msgs
  geometry_msgs
)




###################################
## ament specific configuration ##
###################################
ament_package(
  #  INCLUDE_DIRS include
  #  LIBRARIES tms_msg_db
#  ament_export_dependencies.
# std_msgs
# sensor_msgs
# geometry_msgs
  #  DEPENDS system_lib
)



###########
## Build ##
###########

# none
