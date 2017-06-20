__author__ = 'ArseneLupin'


#this is the function for calculate tilt angle
#this calculation will combine accelerometer values and gyro values to get tilt angle using Kalman Filter
#Before combining it, the gyro values must be filtered using second order Butterworth (high pass filter) with cut-off frequency 0.05 Hz

from scipy import signal
import acceltilt
import butterfilt
import angularinteg
import kalman_filt
import source_var

R1 = 2352.5
R2 = 1519.9

def mytilt(acc_x,acc_y,acc_z,gyr_x,gyr_y,gyr_z):



    #============== Butterworth Filter =======================================================
    # This function is to calculate Wn for butterworth function: cut_off_frequency/ (sampling-rate/2)
    samp_rate = source_var.sampling_rate()
    WN = 0.05/(samp_rate/2)
    a,b = signal.butter(2,WN,'high') # calculate Butterworth Filter coefficient


    #initial Kalman Filter values

    p1=0 #error covariance update
    p2=0
    x_est_z=[0,0]
    x_est_y=[0,0]

    gyro_x=[0,0,0]
    gyro_filx=[0,0]

    gyro_y=[0,0,0]
    gyro_fily =[0,0]

    gyro_z=[0,0,0]
    gyro_filz=[0,0]

    gyrofilValx=0
    gyrofilValy=0
    gyrofilValz=0

    gyro_savex=[0,0]
    gyro_savey=[0,0]
    gyro_savez=[0,0]

    error_cov1 = 0
    error_cov2 = 0

    angle_y_final=[]
    angle_z_final=[]

    for i in range(0,len(acc_x)):

        #compute tilt angle from accelerometer values

        angle_acc = acceltilt.acceltilt(acc_x[i],acc_y[i],acc_z[i])

        #========== High Pass Filter for gyro data =============================================

        # x axis
        gyro_x[2] = gyr_x[i]
        gyro_filx[1] = gyrofilValx
        gyrofilValx = butterfilt.butterfilt(gyro_x,gyro_filx,a,b)

        gyro_x[0]= gyro_x[1]
        gyro_x[1]= gyro_x[2]
        gyro_filx[0] = gyro_filx[1]
        gyro_savex[1] = gyrofilValx

        # y axis
        gyro_y[2] = gyr_y[i]
        gyro_fily[1] = gyrofilValy
        gyrofilValy = butterfilt.butterfilt(gyro_y,gyro_fily,a,b)

        gyro_y[0] = gyro_y[1]
        gyro_y[1] = gyro_y[2]
        gyro_fily[0] = gyro_fily[1]
        gyro_savey[1] = gyrofilValy

        # z axis
        gyro_z[2] = gyr_z[i]
        gyro_filz[1] = gyrofilValz
        gyrofilValz = butterfilt.butterfilt(gyro_z,gyro_filz,a,b)

        gyro_z[0] = gyro_z[1]
        gyro_z[1] = gyro_z[2]
        gyro_filz[0] = gyro_filz[1]
        gyro_savez[1] = gyrofilValz

        # angular velocity integration
        angles = angularinteg.angularinteg(gyro_savex,gyro_savey,gyro_savez)

        #update the value of integrated gyro for next iteration
        gyro_savex[0] = angles[0]
        gyro_savey[0] = angles[1]
        gyro_savez[0] = angles[2]

        #========== Kalman Filter ============================#

        # Kalman Filter for y axis
        x_est_y[0] = angle_acc[1] #tilt angle from accelerometer z axis
        meas_sens_y = angle_acc[0]

        k_val_y = kalman_filt.kalmanfilt(x_est_y, error_cov2,R2,meas_sens_y)

        x_est_y[1] = k_val_y[0]
        error_cov2 = k_val_y[1]
        angle_y = k_val_y[0]

        #======================================================
        # Kalman Filter for Z axis

        # TODO this looks wrong. The x_est should only be updated by the kalman filter
        x_est_z[0] = angle_acc[2] # tilt angle from accelerometer z axis
        meas_sens_z= angles[1] # tilt angle from filtered gyro y axis

        k_val_z = kalman_filt.kalmanfilt(x_est_z, error_cov1, R1, meas_sens_z) #Kalman Implementation

        x_est_z[1] = k_val_z[0] #kalman value for next iteration
        error_cov1 = k_val_z[1]
        angle_z = k_val_z[0]
        #======================================================
        # input value into array

        angle_z_final.append(angle_z)
        angle_y_final.append(angle_y)

    result = [angle_y_final, angle_z_final]

    return result















