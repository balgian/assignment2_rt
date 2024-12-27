#! /usr/bin/env python3

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
    plane_pos_vel.pos_x = msg.pose.pose.position.x
    plane_pos_vel.pos_y = msg.pose.pose.position.y
    plane_pos_vel.lin_vel_x = msg.twist.twist.linear.x
    plane_pos_vel.ang_vel_z = msg.twist.twist.angular.z

    pub.publish(plane_pos_vel)


def feedback_callback(feedback: PlanningFeedback) -> None:
    global stat
    stat = feedback.stat


def main() -> None:
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
