#!/usr/bin/env python
import rospy
from loggers.msg import SingleLogPosition

def talker():
    pub = rospy.Publisher('position_chatter', SingleLogPosition, queue_size=10)
    rospy.init_node('position_test_talker', anonymous=True)
    rate = rospy.Rate(1)

    msg_position = SingleLogPosition()
    while not rospy.is_shutdown():
        msg_position.logTime = rospy.Time.now()
        msg_position.level = 1
        msg_position.message = 'ok'
        msg_position.latitude = 0
        msg_position.longitude = 0
        msg_position.yaw = 0
        msg_position.roll = 0
        msg_position.pitch = 0

        pub.publish(msg_position)
        rospy.loginfo('sent')
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
