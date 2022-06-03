#!/usr/bin/env python
import rospy
from zoo_bot.msg import HardwareData, GeoPosition, SensorData, SingleLog

def log_collision(sensorID):
    pub = rospy.Publisher('activity_chatter', SingleLog, queue_size=10)
    pub.publish(
        SingleLog(
                rospy.Time.now(),
                2,
                'collision detected sensorID: %d' % sensorID
        )
    )

def collision(sensorsData):
    collision = False
    for sensorData in sensorsData:
        if sensorData.sensorID > 50 and sensorData.sensorID < 80:
            if not sensorData.read < 1:
                collision = True
                log_collision(sensorData.sensorID)

    return collision


def talker():
    pub = rospy.Publisher('hardware_chatter', HardwareData, queue_size=10)
    rospy.init_node('hardware_talker', anonymous=True)
    rate = rospy.Rate(1)

    msg_hardware = HardwareData()
    while not rospy.is_shutdown():
        msg_hardware.batteryLevel = 73.4141
        msg_hardware.robotPos = GeoPosition(0, 0, 0, 0, 0, 0)
        msg_hardware.velocity = 0

        # simulating sensors
        sensorsData = [
            # collision sensors
            #         read            sensorID
            SensorData(1,               51),
            SensorData(0,               52),
            SensorData(0.4,             53),
            SensorData(1.53,            54),

            # distance sensors
            SensorData(float('inf'),    101),
            SensorData(float('inf'),    102),
            SensorData(256.352,         103),
            SensorData(float('inf'),    104),
            SensorData(144.125,         105),
        ]
        msg_hardware.sensorData = sensorsData

        collision(sensorsData)

        pub.publish(msg_hardware)
        rospy.loginfo('sent')
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
