#!/usr/bin/env python3
"""
.. module:: target_client
    :platform: Unix
    :synopsis: Python module to send the target position and retrieve plane velocity.

.. moduleauthor:: Gian Marco Balia

This module implements a service node that allows a user to set a target position for a plane
and track its velocity. The node interacts with an action server and publishes the plane's
position and velocity based on odometry data.

Services:
    - ``target_pos``: Provides the last target position set by the user.

Topics:
    - ``/plane_pos_vel`` (Publisher): Publishes the plane's position and velocity.
    - ``/odom`` (Subscriber): Listens for odometry messages to update plane position and velocity.

Action Client:
    - ``reaching_goal``: Sends a goal to the action server and receives feedback.

Global Variables:
    - ``pub`` (:class:`rospy.Publisher`): Publisher for plane position and velocity.
    - ``plane_pos_vel`` (:class:`first_part.msg.PlanePosVel`): Stores the plane's current position and velocity.
    - ``toggle`` (:class:`int`): Indicates whether a goal has been sent.
    - ``stat`` (:class:`str`): Stores the latest feedback status from the action server.

Functions:
    - :func:`pos_vel_callback` (msg: :class:`nav_msgs.msg.Odometry`):
        Callback function to update plane position and velocity based on odometry data.

    - :func:`feedback_callback` (feedback: :class:`assignment_2_2024.msg.PlanningFeedback`):
        Callback function to update the status of the action goal.

    - :func:`main` ():
        Initializes the ROS node, sets up publishers and subscribers, and manages user input to send/cancel targets.
"""

import rospy
from geometry_msgs.msg import Pose, PoseStamped, Point
from actionlib import SimpleActionClient, TerminalState
from assignment_2_2024.msg import PlanningAction, PlanningGoal, PlanningFeedback
from first_part.msg import PlanePosVel
from nav_msgs.msg import Odometry

pub: rospy.Publisher
plane_pos_vel: PlanePosVel = PlanePosVel()
toggle: int = 0
stat: str = ""


def pos_vel_callback(msg: Odometry) -> None:
    """
    Callback function for the odometry subscriber.
    Updates the plane's position and velocity.

    :param msg: Odometry message containing position and velocity data.
    :type msg: nav_msgs.msg.Odometry
    """
    plane_pos_vel.pos_x = msg.pose.pose.position.x
    plane_pos_vel.pos_y = msg.pose.pose.position.y
    plane_pos_vel.lin_vel_x = msg.twist.twist.linear.x
    plane_pos_vel.ang_vel_z = msg.twist.twist.angular.z

    pub.publish(plane_pos_vel)


def feedback_callback(feedback: PlanningFeedback) -> None:
    """
    Callback function for the action client feedback.
    Updates the global status variable with the latest feedback from the action server.

    :param feedback: Feedback message from the action server.
    :type feedback: assignment_2_2024.msg.PlanningFeedback
    """
    global stat
    stat = feedback.stat


def main() -> None:
    """
    Main function to initialize the ROS node, set up the publisher and subscriber,
    and handle user input to send and cancel target positions.
    """
    rospy.init_node("target_client")

    global pub, toggle, stat

    client: SimpleActionClient = SimpleActionClient("reaching_goal", PlanningAction)
    client.wait_for_server()

    pub = rospy.Publisher('plane_pos_vel', PlanePosVel, queue_size=10)
    rospy.Subscriber("odom", Odometry, pos_vel_callback)

    pose: Pose = Pose()
    goal: PlanningGoal = PlanningGoal()

    while not rospy.is_shutdown():
        if toggle:
            user_input = input("Do you want to cancel the target? [y/n] ")
            if user_input.lower() == 'y' and stat != "Target reached!" and stat != "Target cancelled!":
                client.cancel_goal()
                toggle = 0
        else:
            pose.position.x = float(input("Enter the x coordinate of the target: "))
            pose.position.y = float(input("Enter the y coordinate of the target: "))

            goal.target_pose.pose = pose
            client.send_goal(goal, feedback_cb=feedback_callback)
            toggle = 1


if __name__ == "__main__":
    main()
