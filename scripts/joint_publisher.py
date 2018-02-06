#!/usr/bin/env python
#-*- coding:utf-8 -*-

import rospy
from std_msgs.msg import MultiArrayLayout, MultiArrayDimension, Float32MultiArray, Float64

pose_list = [0.0,0.0,0.0,
             0.0,0.0,0.0,
             0.0]

pub = rospy.Publisher("joints_data",Float32MultiArray,queue_size=1)
pub_data = Float32MultiArray()

def joint_callback(data,id):
    if id == 0:
       for i in range(len(data.data)):
           pose_list[i] = data.data[i]
    else:
       pose_list[-1] = data.data

    print pose_list
    pub_data.data = pose_list
    pub.publish(pub_data)
    rospy.sleep(0.1)

def main():
    rospy.init_node("joint_publisher")
    rospy.Subscriber("/pose_data", Float32MultiArray, joint_callback, queue_size=1, callback_args=0)
    rospy.Subscriber("/tilt_controller/command", Float64, joint_callback, queue_size=1, callback_args=1)
    rospy.spin()

if __name__ == "__main__":
   main()
