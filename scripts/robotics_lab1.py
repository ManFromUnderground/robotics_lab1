#!/usr/bin/env python3
#add more comments later
# import ROS for developing the node
import rospy

# import geometry_msgs/Twist for control commands
from geometry_msgs.msg import Twist
from robotics_lab1 import Turtlecontrol
from Turtlecontrol.msg import kp
from Turtlecontrol.msg import xd


from turtlesim.msg import Pose

#current/most recent input
cur = Turtlecontrol()
#current location, kept updated bellow
loc = Pose()
#new = Turtlecontrol()

def pos_callback(data):
	loc.__dict__ = data.__dict__.copy()

def get_loc():
	return loc

def update_input(data):
	global cur
	cur.xd = data.xd
	cur.kd = data.kd

def get_input():
	global cur
	#global new
	new_msg = Turtlecontrol()
	var1, var2 = input("Give me a position and control gain respectively, seperated with a space.")
	#var1 = input("give me a location value for x")
	#var2 = input("give me a control gain")
	new_msg.xd = float(var1)
	new_msg.kd = float(var2)
	pub2 = rospy.Publisher('/turtle1/control_params', Turtlecontrol, queue_size=10)
	pub2.publish(new_msg)
	#return new_msg

if __name__ == '__main__':
	# declare a publisher to publish in the velocity command topic
	cmd_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
	# initialize the command node
	rospy.init_node('robotics_lab1', anonymous = True)
	# set a 10Hz frequency for this loop
	loop_rate = rospy.Rate(10)
	rospy.Subscriber('turtle1/pose', Pose, pos_callback)
	#rospy.Subscriber()
	# declare a variable of type Twist for sending control commands
	vel_cmd = Twist()
	
	#new topic for inputs
	pub2 = rospy.Publisher('/turtle1/control_params', Turtlecontrol, queue_size=10)
	#make updater subscribe to the new topic
	rospy.Subscriber('/turtle1/control_params', Turtlecontrol, update_input)
	
	# run this control loop regularly
	while not rospy.is_shutdown():
		#var = input("give me a desired location")
		# set the linear (forward/backward) velocity command
		error = cur.xd - getloc.x
		vel = error * cur.kp
		vel_cmd.linear.x = vel
		# set the angular (heading) velocity command
		#vel_cmd.angular.z = 0.5
		# publish the command to the defined topic
		cmd_pub.publish(vel_cmd)
		if error == 0:
			get_input()
		# wait for 0.1 seconds until the next loop and repeat
		loop_rate.sleep()

"""def pos_callback(data):
	thing1 = Turtlecontrol()
	global thing1
	get_input()"""

"""def pos_publisher():
	rospy.init_node('pos_pub', anonymous = True)
	rospy.Subscriber('turtle1/pose', Pose, pos_callback)
	pos_pub = rospy.Publisher('turtle1/control_params', Turtlecontrol, queue_size = 10)
	loop_rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		pos_pub.publish(thing1)
		loop_rate.sleep()"""
	


