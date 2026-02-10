This repo is for a ROS 2 Humble–based Autonomous Mobile Robot (AMR) featuring custom URDF, differential-drive control via ros2_control, real-time SLAM, AMCL localization, Nav2 motion planning, and full simulation integration.

Implementation of Navigation is left, rest everything is done.

DEPENDENCIES
Ubuntu 22.04
ROS 2 Humble Hawksbill

Install required ROS packages:
sudo apt update
sudo apt install -y
ros-humble-ros2-control
ros-humble-ros2-controllers
ros-humble-diff-drive-controller
ros-humble-joint-state-broadcaster
ros-humble-robot-localization
ros-humble-slam-toolbox
ros-humble-navigation2
ros-humble-nav2-bringup
ros-humble-gazebo-ros
ros-humble-xacro

Additional tools:
sudo apt install -y python3-colcon-common-extensions

BUILD WORKSPACE
cd ~/amr_ws
colcon build
source install/setup.bash
