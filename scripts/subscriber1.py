#!/usr/bin/env python3

import ropsy

from Turtlecontrol.msg import kp
from Turtlecontrol.msg import xd

from turtlesim.msg import Pose

def new_position(data):
	error = xd - data.x
	vel = error * kp
	#figure out what to do with vel now
	print("this is the velocity: ")
	print(vel)

if __name__ == '__main__':
	rospy.init_node('subscriber1', anonymous = True)
	rospy.Subscriber('/turtle1/pose', Pose, new_position)
	rospy.spin()
	
