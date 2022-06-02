#!/usr/bin/env python
import rospy
from loggers.msg import SingleLog

def talker():
    pub = rospy.Publisher('activity_chatter', SingleLog, queue_size=10)
    rospy.init_node('activity_test_talker', anonymous=True)
    rate = rospy.Rate(1)

    log_msg = SingleLog()
    while not rospy.is_shutdown():
        log_msg.logTime = rospy.Time.now()
        log_msg.level = 1
        log_msg.message = 'Test activity :D'

        pub.publish(log_msg)
        rospy.loginfo('sent')
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
