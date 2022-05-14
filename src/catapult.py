#!/usr/bin/env python

import rospy
import rosparam
import rosgraph

if not rosgraph.is_master_online():
    print("Rosmaster is not online, aborting.")
    exit(1)

node_name = 'catapult'
rospy.init_node(node_name, anonymous=True)


class Catapult:
    # This class receives parameters
    # from ros param server
    # params such as max angle
    # or etc..
    barrel_length = rosparam.get_param(node_name, 1000)

    def setup_launcher():
        pass

    def calculate_trajectory():
        pass

    def shoot():
        pass
