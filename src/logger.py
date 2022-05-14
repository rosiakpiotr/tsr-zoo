#!/usr/bin/env python

import rospy
import rosgraph

if not rosgraph.is_master_online():
    print("Rosmaster is not online, aborting.")
    exit(1)
