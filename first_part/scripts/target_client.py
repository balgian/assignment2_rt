import roslib
roslib.load_manifest('my_pkg_name')
import rospy
import actionlib
from actionlib import SimpleActionClient, TerminalState
from assignment_2_2024.msg
from assignment_2_2024.msg import PlanningAction, PlanningActionGoal, PlanningActionFeedback, PlanningActionResult


def main() -> None:
    client: SimpleActionClient = SimpleActionClient('/reaching_goal', PlanningAction)
    client.wait_for_server()

    fdbk = rospy.wait_for_message('/reaching_goal/feedback', PlanningActionFeedback)

    while not rospy.is_shutdown():
        if fdbk.stat != "Target reached!" and fdbk.stat != "Target cancelled!":
            user_input = input("Do you want to cancel the target? [y/n] ")
            if user_input.lower() == 'y':
                client.cancel_goal()
            continue

        target_x = float(input("Enter the x coordinate of the target: "))
        target_y = float(input("Enter the y coordinate of the target: "))
        orientation = float(input("Enter the orientation of the target: "))

        target = PlanningActionGoal()
        target.goal.target_pose.pose.position.x = target_x
        target.goal.target_pose.pose.position.y = target_y
        target.goal.target_pose.pose.orientation.z = orientation
        client.send_goal(target)

if __name__ == "__main__":
    main()
