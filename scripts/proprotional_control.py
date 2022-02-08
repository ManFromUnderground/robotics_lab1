#!/usr/bin/env python3

#By Trey Castle

# import ROS for developing the node
import rospy

# import geometry_msgs/Twist for control commands
from geometry_msgs.msg import Twist
from robotics_lab1.msg import Turtlecontrol
#from Turtlecontrol.msg import kp
#from Turtlecontrol.msg import xd


from turtlesim.msg import Pose

#current/most recent input
cur = Turtlecontrol()
#current location, kept updated bellow
loc = float()
#new = Turtlecontrol()

#call back to update the position
def pos_callback(data):
	global loc
	loc = data.x

#updates the input
def update_input(data):
	global cur
	cur.xd = data.xd
	cur.kp = data.kp


if __name__ == '__main__':
	# declare a publisher to publish in the velocity command topic
	cmd_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
	# initialize the command node
	rospy.init_node('proprotional_control', anonymous = True)
	# set a 10Hz frequency for this loop
	loop_rate = rospy.Rate(10)
	rospy.Subscriber('turtle1/pose', Pose, pos_callback)
	#rospy.Subscriber()
	# declare a variable of type Twist for sending control commands
	vel_cmd = Twist()
	
	#make updater subscribe to new topic to recieve inputs
	rospy.Subscriber('/turtle1/control_params', Turtlecontrol, update_input)
	
	# repeats the loop
	while not rospy.is_shutdown():
		# takes the desired input and substracts it from the location, then multiplies it by the desired velocity
		error = cur.xd - loc
		vel = error * cur.kp
		vel_cmd.linear.x = vel
		# publish the command to the defined topic
		cmd_pub.publish(vel_cmd)
		# wait for 0.1 seconds until the next loop and repeat
		loop_rate.sleep()



