# Research Track 1: Assignment 2

## Package Overview

This package consists of one ROS 2 node `odom_subscriber_vel_publisher` developed with ROS 2 Foxy. This node communicate with the package [**robot_urdf**](https://github.com/CarmineD8/robot_urdf.git) to control a robot simulation using **_Gazebo_** and to view the simulated robot model, sensor information with **_RViz_**.

### Node: `odom_subscriber_vel_publisher`

This node implements a subscriber to the topic `odom` to receive the robot’s position and a publisher to `cmd_vel` to pilot the robot along the linear velocity $x$ straight to the robot’s center and the angular velocity $z$ to turn it around. The robot will perform a winding along the $y$-axis.
Two distinct methodologies are implemented: the first is the conventional member function utilized in ROS 2; the second involves the member function not being registered as a callback from the timer.

The attached graph provides a detailed description of the package’s functionality. ![second_part](https://i.imgur.com/GTwcRYm.png)

### How to Use

1. In the terminal run the launch fil `gazebo.launch.py` of the package  [**robot_urdf**](https://github.com/CarmineD8/robot_urdf.git).
2. In a separate terminal run the node `odom_subscriber_vel_publisher` of the package **second_part**.

### Dependencies:

| `rclpy` | `robot_urdf` | `geometry_msgs` | `nav_msgs` |
|---------|:------------:|:---------------:|:----------:|
