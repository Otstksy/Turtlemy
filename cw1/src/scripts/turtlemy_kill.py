#!/usr/bin/env python

import rospy
from turtlesim.srv import Kill

def kill_turtle(turtle_name):
    rospy.wait_for_service('/kill')
    try:
        kill_turtle_service = rospy.ServiceProxy('/kill', Kill)
        kill_turtle_service(turtle_name)
        print("Turtle {} killed.".format(turtle_name))
    except rospy.ServiceException as e:
        print("Service call failed: {}".format(e))

if __name__ == '__main__':
    rospy.init_node('kill_turtle_script', anonymous=True)

    # Specify the name of the turtle you want to kill
    turtle_to_kill = "turtle1"

    # Call the function to kill the turtle
    kill_turtle(turtle_to_kill)
