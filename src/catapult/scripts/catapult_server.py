#!/usr/bin/env python

from catapult.srv import CatapultData, CatapultDataResponse
from catapult.msg import LanuchInfo
from msgPack.msg import *
from haversine import haversine, Unit
from loggers.msg import SingleLog
import rospy

def talker(success, reason):
    pub = rospy.Publisher('activity_chatter', SingleLog, queue_size=10)
    
    log_msg = SingleLog()
    log_msg.logTime = rospy.Time.now()
    log_msg.level = 1

    status = ('failed', 'succeed')[success]
    msg_reason = (' reason: %s' % (reason), '')[success]
    log_msg.message = 'from catapult: launch %s%s' % (status, msg_reason)
    pub.publish(log_msg)

def distace(robtPos, targetPos):
    return haversine((robtPos.latitude, robtPos.longitude), (targetPos.latitude, targetPos.longitude), unit=Unit.METERS)


def handle_catapult(request):
    response = LanuchInfo()
    response.inRange = not (distace(request.robotPos, request.targetPos) > 70)
    
    if not request.launch:
        response.tryingToLauch = False
        response.launched = False
        response.fail = False
        response.failMsg = ''
        return CatapultDataResponse(response)
    
    response.tryingToLauch = True
    # Chek if no one is standing in front of the robot
    # if some one is standing in front of the robot stop launch and retur fail

    if not response.inRange:
        response.launched = False
        response.fail = True
        response.failMsg = 'out of range'
        try:
            talker(False, response.failMsg)
        except rospy.ROSInterruptException:
            pass
        return CatapultDataResponse(response)

    # Launch!

    try:
        talker(True, '')
    except rospy.ROSInterruptException:
        pass

    response.launched = True
    response.fail = False
    response.failMsg = ''

    return CatapultDataResponse(response)

def catapult_server():
    rospy.init_node('catapult_server')
    s = rospy.Service('catapult', CatapultData, handle_catapult)
    print('Now catapult is ready to work')
    rospy.spin()

if __name__ == "__main__":
    catapult_server()