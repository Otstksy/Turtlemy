#!/usr/bin/env python

import rospy
from turtlesim.srv import Spawn

def spawn_turtle(name, x, y):
    rospy.wait_for_service('/spawn')
    try:
        spawn_turtle = rospy.ServiceProxy('/spawn', Spawn)
        spawn_turtle(x, y, 0, name)
    except rospy.ServiceException as e:
        print("Service call failed: {}".format(e))

def main():
    rospy.init_node('turtle_spawn_script', anonymous=True)
    rospy.sleep(1)  # Wait for the node to fully initialize

    # Spawn turtles at specific locations
    spawn_turtle("turtle1", 1.0, 1.0)
    spawn_turtle("turtle2", 10.0, 10.0)
    spawn_turtle("turtle3", 1.0, 10.0)
    spawn_turtle("turtle4", 10.0, 1.0)

    rospy.spin()

if __name__ == '__main__':
    main()

