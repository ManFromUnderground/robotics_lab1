#!/usr/bin/env python3
#add more comments later
# import ROS for developing the node
import rospy
# import geometry_msgs/Twist for control commands
from geometry_msgs.msg import Twist

if __name__ == '__main__':
	# declare a publisher to publish in the velocity command topic
	cmd_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
	# initialize the node
	rospy.init_node('vel_publisher_node', anonymous = True)
	# set a 10Hz frequency for this loop
	loop_rate = rospy.Rate(10)
	# declare a variable of type Twist for sending control commands
	vel_cmd = Twist()
	# run this control loop regularly
	while not rospy.is_shutdown():
		var = input("give me a desired location")
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
