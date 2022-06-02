#!/usr/bin/env python
import rospy
from loggers.msg import SingleLogPosition

def callback(msg_position):
    msg = '%s\t[%s]\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (
        rospy.get_caller_id(),
        str(msg_position.logTime),
        str(msg_position.level),
        str(msg_position.message),
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
    rospy.init_node('position_listener', anonymous=True)
    rospy.loginfo('now listening to position_chatter')
    rospy.loginfo('caller_id\tdate_time\tlevel\tmsg\tlat\tlong\talt\tyaw\troll\tpitch')
    rospy.Subscriber('position_chatter', SingleLogPosition, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()