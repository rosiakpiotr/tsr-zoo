#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from catapult.srv import CatapultData
from msgPack.msg import GeoPosition
from catapult.msg import *

def launch(lat1, lon1, lat2, lon2):
    rospy.wait_for_service('catapult')
    try:
        robotPos = GeoPosition(lat1, lon1, 0, 0, 0, 0)
        targetPos = GeoPosition(lat2, lon2, 0, 0, 0, 0)
        catapult = rospy.ServiceProxy('catapult', CatapultData)
        resp = catapult('bazanty', robotPos, targetPos, True)
        return resp
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [lat1, lon1, lat2, lon2]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 5:
        lat1 = float(sys.argv[1])
        lon1 = float(sys.argv[2])
        lat2 = float(sys.argv[3])
        lon2 = float(sys.argv[4])
    else:
        print(usage())
        sys.exit(1)
    print('request sent')
    print(launch(lat1, lon1, lat2, lon2))