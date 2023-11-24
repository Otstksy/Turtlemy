#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from pynput import keyboard

# Initialize linear speed as a global variable
linear_speed = 1.0

def on_key_release(key):
    try:
        global twist
        if key.char == 'w':
            twist.linear.x = 0.0
        elif key.char == 's':
            twist.linear.x = 0.0
        elif key.char == 'a':
            twist.angular.z = 0.0
        elif key.char == 'd':
            twist.angular.z = 0.0
    except AttributeError:
        pass

def on_key_press(key):
    global twist, linear_speed
    angular_speed = 1.0
    
    try:
        if key.char == 'w':
            twist.linear.x = linear_speed
        elif key.char == 's':
            twist.linear.x = -linear_speed
        elif key.char == 'a':
            twist.angular.z = angular_speed
        elif key.char == 'd':
            twist.angular.z = -angular_speed
        elif key.char == 'q':
            linear_speed += 1.0  # Increase linear speed by 1.0
        elif key.char == 'e':
            linear_speed -= 1.0  # Decrease linear speed by 1.0
    except AttributeError:
        pass

def teleop_turtlesim():
    rospy.init_node('teleop_turtlesim', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    global twist
    twist = Twist()

    print("Use W, A, S, D to move, Q to speed up, E to slow down, and Ctrl+C to stop")

    with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
        while not rospy.is_shutdown():
            pub.publish(twist)
            rospy.sleep(0.1)

if __name__ == '__main__':
    try:
        teleop_turtlesim()
    except rospy.ROSInterruptException:
        pass
