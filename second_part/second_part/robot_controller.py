#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

# * First way to do the Subscriber and Publisher

class OdomSubscriberVelPublisher(Node):

    def __init__(self):
        super().__init__('odom_subscriber_vel_publisher')

        self.robot_pos: Odometry = Odometry()

        self.subscription = self.create_subscription(Odometry, 'odom', self.listener_callback, 10)

        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def listener_callback(self, msg: Odometry) -> None:
        self.robot_pos = msg

    def timer_callback(self) -> None:
        msg: Twist = Twist()
        msg.linear.x = 1.0
        msg.angular.z = 0.0
        if self.robot_pos.pose.pose.position.x > 9.0:
            msg.linear.x = 1.0
            msg.angular.z = 1.4
        if self.robot_pos.pose.pose.position.x < 1.5:
            msg.linear.x = 1.0
            msg.angular.z = -1.4

        self.publisher_.publish(msg)

# * Second way to do the Subscriber and Publisher

# class OdomSubscriberVelPublisher(Node):
#
#     def __init__(self):
#         super().__init__('odom_subscriber_vel_publisher')
#
#         self.create_subscription(Odometry, 'odom', self.listener_callback, 10)
#         self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
#
#     def listener_callback(self, msg: Odometry) -> None:
#         cmd: Twist = Twist()
#         cmd.linear.x = 1.0
#         cmd.angular.z = 0.0
#         if msg.pose.pose.position.x > 9.0:
#             cmd.linear.x = 1.0
#             cmd.angular.z = 1.4
#         if msg.pose.pose.position.x < 1.5:
#             cmd.linear.x = 1.0
#             cmd.angular.z = -1.4
#
#         self.publisher_.publish(cmd)


def main(args=None):
    rclpy.init(args=args)

    odom_subscriber_vel_publisher: OdomSubscriberVelPublisher = OdomSubscriberVelPublisher()
    rclpy.spin(odom_subscriber_vel_publisher)
    odom_subscriber_vel_publisher.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()