#!/usr/bin/env python
import rospy
from zoo_bot.msg import SingleLog

def callback(msg_log):
    rospy.loginfo('%s\t[%s]\t%s\t%s' % (str(rospy.get_caller_id()), str(msg_log.logTime), str(msg_log.level), str(msg_log.message)) )
    #logToFile()

def listener():
    rospy.init_node('activity_listener', anonymous=True)
    rospy.loginfo('now listening')
    rospy.Subscriber('activity_chatter', SingleLog, callback)
    rospy.spin()

if __name__ == '__main__':
    rospy.loginfo('now logging activity :D')
    listener()
