#!/usr/bin/env python

import rospy
from first_part.srv import TargetPos, TargetPosResponse

# * First way to get the last target position

def pos_target(req: TargetPos) -> TargetPosResponse:
    res: TargetPosResponse = TargetPosResponse()
    last_target_x: float = float(rospy.get_param("/des_pos_x"))
    last_target_y: float = float(rospy.get_param("/des_pos_y"))
    res.pos_message = f"Last target position: (x: {last_target_x}, y: {last_target_y})"
    return res


def main():
    rospy.init_node('last_target_pos_server')
    rospy.Service('target_pos', TargetPos, pos_target)
    rospy.spin()


# * Second way to get the last target position

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
#     sub: rospy.Subscriber = rospy.Subscriber('reaching_goal/goal', PlanningActionGoal, copy_target_callback)
#     serv: rospy.Service = rospy.Service('target_pos', TargetPos, pos_target)
#     rospy.spin()
#
#
# if __name__ == "__main__":
#     main()
