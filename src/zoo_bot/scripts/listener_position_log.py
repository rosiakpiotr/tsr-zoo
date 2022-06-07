#!/usr/bin/env python

import rospy
from zoo_bot.msg import HardwareData

def callback(msg_position):
    msg = '%s\t[%s]\t%s\t%s\t%s\t%s\t%s\t%s' % (
        rospy.get_caller_id(),
        rospy.Time.now(),
        str(msg_position.robotPos.latitude),
        str(msg_position.robotPos.longitude),
        str(msg_position.robotPos.altitude),
        str(msg_position.robotPos.yaw),
        str(msg_position.robotPos.roll),
        str(msg_position.robotPos.pitch)
    )
    rospy.loginfo(msg)
    #logToFile()

def listener():
    rospy.init_node('hardware_listener', anonymous=True)
    rospy.loginfo('now listening to hardware_chatter')
    rospy.loginfo('caller_id\tdate_time\tlat\tlong\talt\tyaw\troll\tpitch')
    rospy.Subscriber('hardware_chatter', HardwareData, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()