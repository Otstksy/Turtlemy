#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import atan2, sqrt

current_pose = Pose()

def pose_callback(data):
    global current_pose
    current_pose = data

def move_to_position(target_x, target_y):
    global current_pose

    rospy.init_node('turtle_controller', anonymous=True)
    vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    pose_sub = rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        distance = sqrt((current_pose.x - target_x)**2 + (current_pose.y - target_y)**2)

        if distance < 0.5:
            break

        angle_to_target = atan2(target_y - current_pose.y, target_x - current_pose.x)

        cmd_vel = Twist()
        cmd_vel.linear.x = 1.0
        cmd_vel.angular.z = 4.0 * (angle_to_target - current_pose.theta)

        vel_pub.publish(cmd_vel)
        rate.sleep()

    vel_pub.publish(Twist())

if __name__ == '__main__':
    try:
        #roomba bath positions
        move_to_position(1, 1)
        move_to_position(10, 1)
        move_to_position(10, 10)
        move_to_position(1, 10)
        move_to_position(1, 2)
        move_to_position(9, 2)
        move_to_position(9, 9)
        move_to_position(2, 9)
        move_to_position(2, 3)
        move_to_position(8, 3)
        move_to_position(8, 8)
        move_to_position(3, 8)
        move_to_position(3, 4)
        move_to_position(7, 4)
        move_to_position(7, 7)
        move_to_position(4, 7)
        move_to_position(4, 5)
        move_to_position(5.54 , 5.54)
        print("I survived") #this was a lot ngl


    except rospy.ROSInterruptException:
        pass
