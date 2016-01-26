__author__ = 'ArseneLupin'

import source_var

def angularinteg(gyro_x, gyro_y, gyro_z):

    samp_rate = 100 #source_var.sampling_rate()
    s_freq = 1/ float(samp_rate) #0.01 for 100 Hz; 0.1 for 10 Hz


    angle_x = gyro_x[0] + gyro_x[1] * s_freq
    angle_y = gyro_y[0] + gyro_y[1] * s_freq
    angle_z = gyro_z[0] + gyro_z[1]* s_freq

    result = [angle_x, angle_y, angle_z]

    return result
