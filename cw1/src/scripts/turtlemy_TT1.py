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

    rospy.init_node('TT1', anonymous=True)
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
        move_to_position(5, 1)
        move_to_position(5, 2)
        move_to_position(1, 2)
        move_to_position(1, 3)
        move_to_position(5, 3)
        move_to_position(5, 4)
        move_to_position(1, 4)
        move_to_position(1, 5)
        move_to_position(5, 5)
        
        print("I survived") #this was a lot ngl


    except rospy.ROSInterruptException:
        pass
