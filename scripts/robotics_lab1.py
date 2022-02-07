#!/usr/bin/env python3
#add more comments later
# import ROS for developing the node
import rospy

import ropsy

# import geometry_msgs/Twist for control commands
from geometry_msgs.msg import Twist
from robotics_lab1.msg import Turtlecontrol
from Turtlecontrol.msg import kp
from Turtlecontrol.msg import xd


from turtlesim.msg import Pose

if __name__ == '__main__':
	# declare a publisher to publish in the velocity command topic
	cmd_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
	# initialize the node
	rospy.init_node('vel_publisher_node', anonymous = True)
	# set a 10Hz frequency for this loop
	loop_rate = rospy.Rate(10)
	# declare a variable of type Twist for sending control commands
	vel_cmd = Twist()
	pos_publisher()
	# run this control loop regularly
	while not rospy.is_shutdown():
		#var = input("give me a desired location")
		# set the linear (forward/backward) velocity command
		error = xd - data.x
		vel = error * kp
		vel_cmd.linear.x = vel
		# set the angular (heading) velocity command
		#vel_cmd.angular.z = 0.5
		# publish the command to the defined topic
		cmd_pub.publish(vel_cmd)
		# wait for 0.1 seconds until the next loop and repeat
		loop_rate.sleep()

def pos_callback(data):
	thing1 = Turtlecontrol()
	global thing1
	get_input()

def pos_publisher():
	rospy.init_node('pos_pub', anonymous = True)
	rospy.Subscriber('turtle1/pose', Pose, pos_callback)
	pos_pub = rospy.Publisher('turtle1/control_params', Turtlecontrol, queue_size = 10)
	loop_rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		pos_pub.publish(thing1)
		loop_rate.sleep()
	

def get_input():
	new_msg = Turtlecontrol()
	var1 = input("give me a location value for x")
	var2 = input("give me a control gain")
	new_msg.xd = float(var1)
	new_msg.kd = float(var2)
	return new_msg
