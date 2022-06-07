#!/usr/bin/env python

import rospy
import sys
from zoo_bot.srv import CatapultData
from zoo_bot.msg import GeoPosition

def catapult_client(name, launch, lat, lon):
    rospy.wait_for_service('catapult')
    try:
        request = rospy.ServiceProxy('catapult', CatapultData)
        response = request(
            name,
            GeoPosition(lat, lon, 0, 0, 0, 0),
            launch
        )

        return response.launchInfo
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)

def usage():
    return "%s [name launch lat lon]" % sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 5:
        name =      str(sys.argv[1])
        launch =    int(sys.argv[2])
        lat =       float(sys.argv[3])
        lon =       float(sys.argv[4])
    else:
        print(usage())
        sys.exit(1)

    resp = catapult_client(name, launch, lat, lon)
    print(
        'Launch info:\n\ttryingToLauch: %s\n\tlaunched: %s\n\tinRange: %s\n\t'
        'fail: %s\n\tfailMsg: %s\nEND\n' % (
            resp.tryingToLauch,
            resp.launched,
            resp.inRange,
            resp.fail,
            resp.failMsg
        )
    )