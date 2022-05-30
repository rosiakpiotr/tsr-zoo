#!/usr/bin/env python
import rospy
from loggers.msg import SingleLogPosition

def callback(msg_position):
    msg = '%s\t[%s]\t%s\t%s\t%s\t%s' % (
        rospy.get_caller_id(),
        str(msg_position.logTime),
        str(msg_position.level),
        str(msg_position.message),
        str(msg_position.x),
        str(msg_position.y)
        #str(msg_position.latitude),
        #str(msg_position.longitude),
        #str(msg_position.yaw),
        #str(msg_position.roll),
        #str(msg_position.pitch)
    )
    rospy.loginfo(msg)
    #logToFile()

def listener():
    rospy.init_node('position_listener', anonymous=True)
    rospy.Subscriber('position_chatter', SingleLogPosition, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
