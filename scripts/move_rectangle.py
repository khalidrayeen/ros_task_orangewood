#!/usr/bin/env python3

import rospy
from turtlesim.srv import TeleportRelative
from math import pi


def move_turtle():
    """Teleport to turn and move"""
    rospy.init_node('move_turtle_rectangle_node', anonymous=True)
    rate = rospy.Rate(10)

    length = 2
    width = 4

    rospy.wait_for_service('/turtle1/teleport_relative')
    teleport = rospy.ServiceProxy('/turtle1/teleport_relative', TeleportRelative)

    def mv_fwd(distance):
        teleport(distance, 0.0)
        rate.sleep()

    def trn_r():
        """Teleport at the same position but at a 90 deg angle in the right direction"""
        teleport(0, -pi/2)
        rate.sleep()

    while not rospy.is_shutdown():
        mv_fwd(length)
        trn_r()
        mv_fwd(width)
        trn_r()
        mv_fwd(length)
        trn_r()
        mv_fwd(width)
        trn_r()


if __name__ == '__main__':
    try:
        move_turtle()
    except rospy.ROSInterruptException:
        pass