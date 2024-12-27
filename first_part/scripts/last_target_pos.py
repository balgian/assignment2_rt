#!/usr/bin/env python

import rospy
from first_part.srv import TargetPos, TargetPosResponse


def pos_target(req: TargetPos) -> TargetPosResponse:
    res = TargetPosResponse()
    last_target_x: float = float(rospy.get_param("/des_pos_x"))
    last_target_y: float = float(rospy.get_param("/des_pos_y"))
    res.pos_message = f"Last target position: (x: {last_target_x}, y: {last_target_y})"
    return res


def main():
    rospy.init_node('last_target_pos_server')
    serv: rospy.Service = rospy.Service('target_pos', TargetPos, pos_target)
    rospy.spin()


if __name__ == "__main__":
    main()
