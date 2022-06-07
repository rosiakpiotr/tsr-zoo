#!/usr/bin/env python

from zoo_bot.srv import Move, MoveResponse
import rospy

def move_robot(request):
    rospy.loginfo('seting yaw to: %s an moving %sm' % (str(request.setAngles.yaw), str(request.distance) ))
    # robot i moving :D
    return MoveResponse(True)

def movement_service():
    rospy.init_node('movement_server')
    s = rospy.Service('movement_service', Move, move_robot)
    print('Now movement_service is ready to work')
    rospy.spin()

if __name__ == "__main__":
    movement_service()