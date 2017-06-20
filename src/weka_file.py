__author__ = 'ArseneLupin'

#this program will call the features extraction calculation function and generate file for weka

import csv
import writeWeka
import source_var
import threshold_function

def featCalc(sourceFile,sourceFeatures, dest_runtime):


    chestData =[]
    chestList=[]

    thighData=[]
    thighList=[]

    waistData=[]
    waistList=[]

    chestWeka=[]
    counter = 0

    print('The system start to calculate the features ')
    print sourceFile
    with open(sourceFile) as objectFile:

        for line in objectFile:

            data = line.split()

            chestData = [float(data[0]),float(data[1]),float(data[2]),float(data[3]),float(data[4]),float(data[5]),float(data[6]),float(data[7]),float(data[8]),float(data[9])]
            chestList.append(chestData)

            #################################### FUTURE WORK ######################################################
            #thighData = [data[9], data[10], data[11], data[12], data[13], data[14], data[15], data[16], data[17]]
            #thighList.append(thighData)

            #waistData = [data[18], data[19], data[20], data[21], data[22], data[23], data[24], data[25], data[26]]
            #waistList.append(waistData)
            #######################################################################################################

    threshold_function.threshold_function(chestList,sourceFeatures, dest_runtime)
    #writeWeka.writeWeka(sourceFeatures,wekadest)

    print("Finish")
