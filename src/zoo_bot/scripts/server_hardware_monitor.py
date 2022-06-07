#!/usr/bin/env python

from zoo_bot.srv import HardwareReq, HardwareReqResponse
from zoo_bot.msg import GeoPosition, SensorData, HardwareData
import rospy

def hardware_server_res(req):
    res_hardware = HardwareData()
    res_hardware.batteryLevel = 73.4141
    
    # :)
    res_hardware.robotPos = GeoPosition(51.7524835, 19.4527542, 0, 0, 0, 0)
    res_hardware.velocity = 0

    # simulating sensors
    sensorsData = [
        # collision sensors
        #         read            sensorID
        SensorData(0,               51),
        SensorData(0,               52),
        SensorData(0,               53),
        SensorData(0,               54),

        # distance sensors
        SensorData(float('inf'),    101),
        SensorData(float('inf'),    102),
        SensorData(256.352,         103),
        SensorData(float('inf'),    104),
        SensorData(50.125,          105),
    ]
    res_hardware.sensorData = sensorsData

    return HardwareReqResponse(res_hardware)

def hardware_server():
    rospy.init_node('hardware_server')
    s = rospy.Service('hardware', HardwareReq, hardware_server_res)
    print('Now ready to send hardware data')
    rospy.spin()

if __name__ == "__main__":
    hardware_server()