__author__ = 'ArseneLupin'



def writeWeka(source,dest):
    #dest= '/home/edy/S3/weka/bimo.arff'
    #source = "/home/edy/S3/featuresnew/bimo_feat.csv"
    objectwrite = open(source)
    data=[]
    stringtemp=''
    comment = '%'+source
    relation= '@relation falls'
    attribute1 = '@attribute MinimumValue real'
    attribute2 = '@attribute MaximumValue real'
    attribute3 = '@attribute MeanPreImpact real'
    attribute4 = '@attribute MeanImpact real'
    attribute5 = '@attribute MeanPostImpact real'
    attribute6 = '@attribute RootMeanSquarePreImpact real'
    attribute7 = '@attribute RootMeanSquareImpact real'
    attribute8 = '@attribute RootMeanSquarePostImpact real'
    attribute9= '@attribute VariancePreImpact real'
    attribute10= '@attribute VarianceImpact real'
    attribute11= '@attribute VariancePostImpact real'
    attribute12= '@attribute VelocityPreImpact real'
    attribute13= '@attribute VelocityImpact real'
    attribute14= '@attribute VelocityPostImpact real'
    attribute15= '@attribute EnergyPreImpact real'
    attribute16= '@attribute EnergyImpact real'
    attribute17= '@attribute EnergyPostImpact real'
    attribute18= '@attribute SignalMagnitudeAreaPreImpact real'
    attribute19= '@attribute SignalMagnitudeAreaImpact real'
    attribute20= '@attribute SignalMagnitudeAreaPostImpact real'
    attribute21= '@attribute ExponentialMovingAveragePreImpact real'
    attribute22= '@attribute ExponentialMovingAverageImpact real'
    attribute23= '@attribute ExponentialMovingAveragePostImpact real'
    attribute24= '@attribute TiltAngleYPreImpact real'
    attribute25= '@attribute TiltAngleZPreImpact real'
    attribute26= '@attribute TiltAngleYImpact real'
    attribute27= '@attribute TiltAngleZImpact real'
    attribute28= '@attribute TiltAngleYPostImpact real'
    attribute29= '@attribute TiltAngleZPostImpact real'
    attribute30= '@attribute activestate real'
    attribute31= '@attribute annotation {0.0,2.0}'


    for line in objectwrite:
        datatemp = line.split()
        stringdata = ",".join(datatemp)
        data.append(stringdata)

    listWrite = [relation,attribute1,attribute2,attribute3,attribute4,attribute5,attribute6,attribute7,attribute8,attribute9,
                 attribute10,attribute11,attribute12,attribute13,attribute14,attribute15,attribute16,attribute17,attribute18,
                 attribute19,attribute20,attribute21,attribute22,attribute23,attribute24, attribute25, attribute26,
                 attribute27,attribute28, attribute29,attribute30,attribute31]

    #listWrite = [relation,attribute1,attribute2,attribute3,attribute4,attribute5,attribute6,attribute7,attribute8,attribute9,
     #            attribute10,attribute11,attribute12,attribute13,attribute14,attribute15,attribute16,attribute17,attribute18,
      #           attribute19,attribute20,attribute21,attribute22,attribute23,attribute30]

    fileopen = open(dest,'w')

    print 'Writing the features into arff file'
    for i in range(len(listWrite)):
        fileopen.write(listWrite[i]+'\n')

    fileopen.write('\n')
    fileopen.write('@data\n')
    fileopen.write('\n')

    for j in range(len(data)):
        fileopen.write(data[j]+'\n')

    fileopen.close()

    print 'Finish writing'


