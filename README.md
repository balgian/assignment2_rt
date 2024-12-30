# Research Track 1: Assignment 2

## Package Overview

This package consists of two ROS nodes: `target_client` and `last_target_pos` developed with ROS Noetic. These nodes communicate together with the package [**assignment_2_2024**](https://github.com/CarmineD8/assignment_2_2024.git) to control a robot simulation using **_Gazebo_** and to view the simulated robot model, sensor information with **_RViz_**.

### Node: `target_client`

This node implements an _action client_, allowing the user to set a target via terminal or to cancel it. It also publishes the robot position and velocity in the topic `plane_pos_vel` as a custom message `PlanePosVel`.

### Node: `last_target_pos`

It is a service node that, when called, returns the coordinates of the last target sent by the user.
For this node, there are implemented two methods to retrieve the most recent target with a schematic representation of the communication between the nodes of both methods:

1. By getting the `des_pos_x` and `des_pos_y` parameters defined in the launch file `assignment1.launch`; ![first_part_parameters](https://i.imgur.com/8sdvycK.png)
2. By subscribing to the topic `reaching_goal/goal`. ![first_part_topic](https://i.imgur.com/BQm7v9c.png)

### How to Use

1. In the terminal run the launch file `assignment1.launch` of the package [**assignment_2_2024**](https://github.com/CarmineD8/assignment_2_2024.git).
2. In a separate terminal run the launch file `first_part.launch` of the package **first_part**.

### Dependencies:

|     `rospy`     |  `assignment_2_2024`   |  `geometry_msgs`  |
| :-------------: |:----------------------:|:-----------------:|
|   `actionlib`   |  `message_generation`  |    `std_msgs`     |
