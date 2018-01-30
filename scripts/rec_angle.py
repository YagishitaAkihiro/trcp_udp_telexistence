#!/usr/bin/env python
#-*- coding:utf-8 -*-

from __future__ import print_function
from nextage_ros_bridge import nextage_client

from hrpsys import rtm
from hironx_ros_bridge.ros_client import ROS_Client
import argparse
import rospy

#from __future__ import print_function
import socket
from contextlib import closing

def worker(angle_list):
    if len(angle_list) == 24:
#       print (angle_list)
       body_joint = [0.0]#[float(angle_list[1])]
       head_joint = [float(angle_list[2]),float(angle_list[3])]
       rarm_joint = [float(angle_list[4]),float(angle_list[5]),float(angle_list[6]),
                     float(angle_list[7]),float(angle_list[8]),float(angle_list[9])]
       larm_joint = [float(angle_list[14]),float(angle_list[15]),float(angle_list[16]),
                     float(angle_list[17]),float(angle_list[18]),float(angle_list[19])]
#       print (head_joint)
#       print (rarm_joint)
#       print (larm_joint)
#       ros.set_joint_angles_deg("rarm",rarm_joint,2.0,wait=False)
       ros.set_joint_angles_deg("larm",larm_joint,2.0,wait=False)
    else:
       print ("error")
       pass 

def main(host,port,bufsize):
      hosts = host
      ports = port
      bufsizes = bufsize
      
      sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      with closing(sock):
        sock.bind((hosts,ports))
        while not rospy.is_shutdown():
          ang_list = sock.recv(bufsizes).replace('[','')
          ang_list = ang_list.replace(']','')
          ang_list = ang_list.split(",")
#          print (ang_list)
          worker(ang_list)
      return

if __name__ == '__main__':
#-------------------------------------------initial_setting------------------------------------------
#    """
    parser = argparse.ArgumentParser(description='NEXTAGE Open command line interpreters')
    parser.add_argument('--host', help='corba name server hostname')
    parser.add_argument('--port', help='corba name server port number')
    parser.add_argument('--modelfile', help='robot model file nmae')
    parser.add_argument('--robot', help='robot modlule name (RobotHardware0 for real robot, Robot()')
    args, unknown = parser.parse_known_args()
  
    if args.host:
       rtm.nshost = args.host
    if args.port:
       rtm.nsport = args.port
    if not args.robot:
       args.robot = "RobotHardware0" if args.host else "HiroNX(Robot)0"
    if not args.modelfile:
       args.modelfile = ""
  
    if len(unknown) >= 2:
       args.robot = unknown[0]
       args.modelfile = unknown[1]
    robot = nxc = nextage_client.NextageClient()
    robot.init(robotname=args.robot, url=args.modelfile)
    ros = ROS_Client()
#    """
    host = '10.254.21.23'
    port = 4000
    bufsize = 4096
#--------------------------------------------end_initial_setting------------------------------------------
#   主処理
    main(host,port,bufsize)
