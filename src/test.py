__author__ = 'ArseneLupin'

import searchmax,numpy,integrator,math,arff

from numpy import mean, arange
import numpy,emafit
from scipy import signal
import butterfilt
import mytilt
import time

from collections import namedtuple

import searchmax
import operator


import source_var

def main():
    data = [[0.5, 0.6, 0.7, 0.8, 1.4, 1.0, 0.9, 1.6 ], [0.5, 0.6, 0.7, 0.8, 1.4, 2.0, 0.9, 1.5 ], [0.5, 0.6, 0.7, 0.8, 1.4, 0.8, 0.9, 1.6 ],
                      [0.5, 0.6, 0.7, 100, 1.4, 1.1, 0.9, 0.7 ] ]

    print(find_max_index(data))
    print(max_index(data))



def find_max_index(data_array):

    #n_array = numpy.array(data_array)
    #x = n_array.argmax(axis=0)
    index, value = max(enumerate(data_array), key= operator.itemgetter(1))

    return index

def max_index(data_array):
    maxIndex = 0
    newData=[]

    initValue = data_array[0]
    maxVal = initValue[6]
    for i in range(len(data_array)):
        tempVal = data_array[i]

        if tempVal[6]>maxVal:
            maxVal = tempVal[6]
            maxIndex = i

    return maxIndex
if __name__ == '__main__':
    main()