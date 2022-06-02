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
        msg_position.robotPos.latitude = 1
        msg_position.robotPos.longitude = 2
        msg_position.robotPos.altitude = 3
        msg_position.robotPos.yaw = 4
        msg_position.robotPos.roll = 5
        msg_position.robotPos.pitch = 6

        pub.publish(msg_position)
        rospy.loginfo('sent')
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
