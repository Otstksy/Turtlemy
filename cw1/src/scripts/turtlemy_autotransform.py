#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import atan2, sqrt

class TurtleController:
    def __init__(self): #Initializing function
        rospy.init_node('turtle_controller', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.update_pose)
        self.pose = Pose()

    def update_pose(self, data):
        self.pose = data	#maps location to data

    def euclidean_distance(self, goal_pose):
        return sqrt(pow((goal_pose.x - self.pose.x), 2) + pow((goal_pose.y - self.pose.y), 2))

    def linear_vel(self, goal_pose, constant=1.5):
        return constant * self.euclidean_distance(goal_pose)

    def steering_angle(self, goal_pose):
        return atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)

    def angular_vel(self, goal_pose, constant=6):
        return constant * (self.steering_angle(goal_pose) - self.pose.theta)

    def move_turtle_to_goal(self, x, y):
        goal_pose = Pose()
        goal_pose.x = x
        goal_pose.y = y

        while self.euclidean_distance(goal_pose) > 0.01:
            # Linear velocity
            vel_msg = Twist()
            vel_msg.linear.x = self.linear_vel(goal_pose)
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0

            # Angular velocity
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = self.angular_vel(goal_pose)

            self.velocity_publisher.publish(vel_msg)

        # Stop the turtle when the goal is reached
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        turtle_controller = TurtleController()

        while not rospy.is_shutdown():
            x_goal = float(input("x-coordinate"))
            y_goal = float(input("y-coordinate"))

            turtle_controller.move_turtle_to_goal(x_goal, y_goal)

    except rospy.ROSInterruptException:
        pass
