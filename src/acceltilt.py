__author__ = 'ArseneLupin'


import math

def acceltilt(accel_x, accel_y, accel_z):

    #pitch calculation
    x_angle = math.degrees(math.atan2(accel_x, math.hypot(accel_y, accel_z)))

    #roll calculation
    y_angle = math.degrees(math.atan2(accel_y, math.hypot(accel_x, accel_z)))

    #theta calculation
    z_angle = math.degrees(math.atan2(accel_z, math.hypot(accel_x, accel_y)))

    return (x_angle, y_angle, z_angle)
