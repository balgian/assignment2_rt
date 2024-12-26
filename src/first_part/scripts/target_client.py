#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import Pose, PoseStamped, Point
from actionlib import SimpleActionClient, TerminalState
from assignment_2_2024.msg import PlanningAction, PlanningGoal, PlanningFeedback

toggle: int = 0
stat: str = ""


def feedback_callback(feedback: PlanningFeedback) -> None:
    global stat
    stat = feedback.stat


def main() -> None:
    global toggle, stat
    rospy.init_node("target_client")

    client: SimpleActionClient = SimpleActionClient("reaching_goal", PlanningAction)
    client.wait_for_server()

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