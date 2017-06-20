__author__ = 'ArseneLupin'

#this program implements second order Butterworth Filter

def butterfilt(gyro_data, gyro_filt, a, b):

    filtdata = a[0] * gyro_data[2] + a[1] * gyro_data[1] + a[2] * gyro_data[0] - b[1] * gyro_filt[1] - b[2] * gyro_filt[0]

    return filtdata