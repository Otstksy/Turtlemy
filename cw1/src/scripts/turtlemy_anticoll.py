#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class TurtleController:
    def __init__(self):
        rospy.init_node('turtle_controller', anonymous=True)
        self.rate = rospy.Rate(1)  # 1 Hz, adjust as needed
        self.turtle_pose = Pose()
        self.target_x, self.target_y = 5, 5

        rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    def pose_callback(self, data):
        self.turtle_pose = data

    def move_turtle(self):
        while not rospy.is_shutdown():
            if self.turtle_pose.x < 0.5 or self.turtle_pose.x > 10.5 or \
               self.turtle_pose.y < 0.5 or self.turtle_pose.y > 10.5:
                self.move_to_target()
            else:
                self.stop_turtle()

            self.rate.sleep()

    def move_to_target(self):
        twist = Twist()
        twist.linear.x = 1.0  # Move forward
        angle_to_target = self.calculate_angle_to_target()
        twist.angular.z = angle_to_target
        self.velocity_publisher.publish(twist)

    def calculate_angle_to_target(self):
        angle = 0.0
        if self.turtle_pose.x < 0.5:
            angle = -1.0  # Turn left
        elif self.turtle_pose.x > 10.5:
            angle = 1.0  # Turn right
        elif self.turtle_pose.y < 0.5:
            angle = 0.0  # Move straight (no rotation)
        elif self.turtle_pose.y > 10.5:
            angle = 3.14  # Turn 180 degrees (pi radians)

        return angle

    def stop_turtle(self):
        twist = Twist()
        self.velocity_publisher.publish(twist)

if __name__ == '__main__':
    try:
        controller = TurtleController()
        controller.move_turtle()
    except rospy.ROSInterruptException:
        pass
