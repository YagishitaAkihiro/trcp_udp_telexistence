#!/usr/bin/env python
#-*- coding:utf-8 -*-

from __future__ import print_function
import socket
import time
from contextlib import closing
import rospy
from std_msgs.msg import String

global angle_data
angle_data = ""

def callback(data):
    global angle_data
    angle_data = data.data
#    a_d = a_d.replace('[', '')
#    anlge_data = a_d#.replace(']', '')
#    print (angle_data)
    
def main(host,port):
  hosts = host
  ports = port
  count = 0
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  rospy.Subscriber("angle_data",String,callback,queue_size=1)
  with closing(sock):
    while not rospy.is_shutdown():
      global angle_data
      print (angle_data)
      sock.sendto(angle_data, (hosts, ports))
      time.sleep(1)
  return

if __name__ == '__main__':
  rospy.init_node("udp_send")
  host = "10.254.21.23" #localhost'127.0.0.1'
  port = 4000
  main(host,port)
