#!/usr/bin/env python3
"""
.. module:: last_target_pos
    :platform: Unix
    :synopsis: Python module to get the last target position sent by the user

.. moduleauthor:: Gian Marco Balia

This module implements a service node that, when called, returns the coordinates of the last target sent by the user.

Service:
    ``target_pos``
"""

import rospy
from first_part.srv import TargetPos, TargetPosResponse

def pos_target(req: TargetPos) -> TargetPosResponse:
    """
    Service callback function to return the last target position.

    :param req: Empty request sent by the user.
    :type req: TargetPos
    :return: Response containing the last target position.
    :rtype: TargetPosResponse

    The target position is retrieved using two ``float`` parameters defined in the launch file ``assignment1.launch``
    in the package `assignment_2_2024 <https://github.com/CarmineD8/assignment_2_2024.git>`_.
    """
    res: TargetPosResponse = TargetPosResponse()
    last_target_x: float = float(rospy.get_param("/des_pos_x"))
    last_target_y: float = float(rospy.get_param("/des_pos_y"))
    res.pos_message = f"Last target position: (x: {last_target_x}, y: {last_target_y})"
    return res

def main():
    """
    Initializes the ROS node and service ``target_pos``.

    The service returns the last target position sent by the user when called.
    """
    rospy.init_node('last_target_pos_server')
    rospy.Service('target_pos', TargetPos, pos_target)
    rospy.spin()


# * Alternative way to get the last target position

# from assignment_2_2024.msg import PlanningActionGoal
#
# target: PlanningActionGoal = PlanningActionGoal()
#
#
# def copy_target_callback(msg: PlanningActionGoal) -> TargetPosResponse:
#     global target
#     target = msg
#
#
# def pos_target(req: TargetPos) -> TargetPosResponse:
#     res: TargetPosResponse = TargetPosResponse()
#     res.pos_message = (f"Last target position: (x: {target.goal.target_pose.pose.position.x}, "
#                            f"y: {target.goal.target_pose.pose.position.y})")
#     return res
#
#
# def main():
#     rospy.init_node('last_target_pos_server')
#     rospy.Subscriber('reaching_goal/goal', PlanningActionGoal, copy_target_callback)
#     rospy.Service('target_pos', TargetPos, pos_target)
#     rospy.spin()


if __name__ == "__main__":
    main()
