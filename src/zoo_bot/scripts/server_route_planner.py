#!/usr/bin/env python

from zoo_bot.srv import RoutePlanner, RoutePlannerResponse
from zoo_bot.msg import GeoPosition
import rospy

def get_target_pos(targetName):
    # Based on given name it will return specyfic enclosure location
    return GeoPosition(51.7547403, 19.4519124, 0, 0, 0, 0)

def get_shortest_path(targetName):
    # Based on target location get_shortest_path function returns
    # array of nodes to which robot will move in order to get to
    # given location
    get_target_pos(targetName)
    return (
            GeoPosition(51.7522697, 19.4514236, 0, 0, 0, 0),
            GeoPosition(51.752422,  19.4514691, 0, 0, 0, 0),
            GeoPosition(51.7531896, 19.4513427, 0, 0, 0, 0),
            GeoPosition(51.7531895, 19.4513427, 0, 0, 0, 0),
            GeoPosition(51.7544393, 19.4509914, 0, 0, 0, 0),
            GeoPosition(51.7544391, 19.4509911, 0, 0, 0, 0)
    )

def route_planner(request):
    return RoutePlannerResponse(get_shortest_path(request.targetName))

def route_planner_server():
    rospy.init_node('route_planner_server')
    s = rospy.Service('route_planner_service', RoutePlanner, route_planner)
    print('Now route_planner_server is ready to work')
    rospy.spin()

if __name__ == "__main__":
    route_planner_server()