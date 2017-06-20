__author__ = 'ArseneLupin'

import math

A_VAL = 1 # Kalman matrix
H_VAL = 1 # Kalman Matrix
I_VAL = 1 # Kalman MAtrix
Q = 0.012
TEST_X = 0.1

def kalmanfilt(x_est, error_cov, R, gyrodat ):


    x_temp_est = (A_VAL - TEST_X) * x_est[1] + TEST_X * x_est[0] # Predict the next value

    p_temp = A_VAL * error_cov * A_VAL + Q

    tempcalc = math.pow(( H_VAL * p_temp * H_VAL + R ),-1) #temporary variable to do power

    kal = p_temp * H_VAL *tempcalc  # Kalman Gain

    x_est = x_temp_est + kal * (gyrodat - H_VAL * x_temp_est)

    error_cov_update = (I_VAL - kal * H_VAL) * p_temp

    result = [x_est, error_cov_update]

    return result