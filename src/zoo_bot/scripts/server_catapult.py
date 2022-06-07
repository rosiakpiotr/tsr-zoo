#!/usr/bin/env python

from zoo_bot.srv import CatapultData, CatapultDataResponse, HardwareReq
from zoo_bot.msg import LanuchInfo, SingleLog, HardwareData
from haversine import haversine, Unit

import rospy, rosparam

def hardware_clitent():
    rospy.wait_for_service('hardware')
    try:
        request = rospy.ServiceProxy('hardware', HardwareReq)
        response = request()
        return response.hardwareData
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)

def clear_shoot():
    hardware_data = hardware_clitent()
    for sensor in hardware_data.sensorData:
        if sensor.sensorID > 100 and sensor.read < rosparam.get_param('catapult_save_lauch_range'):
            return False
    return True

def talker(response, targetName):
    pub = rospy.Publisher('activity_chatter', SingleLog, queue_size=10)
    
    log_msg = SingleLog()
    log_msg.logTime = rospy.Time.now()
    log_msg.level = 1

    status = ('failed', 'succeed')[not response.fail]
    msg_reason = ('reason: %s' % response.failMsg, '')[not response.fail]
    log_msg.message = 'from catapult: launch to %s %s, %s' % (targetName, status, msg_reason)
    pub.publish(log_msg)

def log(response, targetName):
    try:
        talker(response, targetName)
    except rospy.ROSInterruptException:
        rospy.loginfo(rospy.ROSInterruptException)

def distace(robtPos, targetPos):
    return haversine((robtPos.latitude, robtPos.longitude), (targetPos.latitude, targetPos.longitude), unit=Unit.METERS)


def handle_catapult(request):
    hardware_data = hardware_clitent()
    response = LanuchInfo()
    response.inRange = distace(hardware_data.robotPos, request.targetPos) < rosparam.get_param('catapult_range')
    
    if not request.launch:
        response.tryingToLauch = False
        response.launched = False
        response.fail = False
        response.failMsg = ''
        return CatapultDataResponse(response)
    
    response.tryingToLauch = True

    if not response.inRange:
        response.launched = False
        response.fail = True
        response.failMsg = 'out of range'
        log(response, request.targetName)
        return CatapultDataResponse(response)

    # Chek if no one is standing in front of the robot
    # if some one is standing in front of the robot stop launch and retur fail

    if not clear_shoot():
        response.launched = False
        response.fail = True
        response.failMsg = 'an object in launch range'
        log(response, request.targetName)
        return CatapultDataResponse(response)

    # Launch!

    response.launched = True
    response.fail = False
    response.failMsg = ''
    log(response, request.targetName)

    return CatapultDataResponse(response)

def catapult_server():
    rospy.init_node('catapult_server')
    s = rospy.Service('catapult', CatapultData, handle_catapult)
    print('Now catapult is ready to work')
    rospy.spin()

if __name__ == "__main__":
    catapult_server()
