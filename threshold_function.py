__author__ = 'ArseneLupin'

import csv
import featurescom
import source_var
import timeit

def threshold_function(array, dest, runtime_path):

    samp_rate = source_var.sampling_rate()
    pre_impact_win = samp_rate - 1
    post_impact_win = samp_rate * 11
    destFile = dest
    featureRes=[]
    runtime=[]
    outF = open(destFile, "w")
    csvWriter = csv.writer(outF, delimiter='\t')

    print('Calculate Features')
    #print(samp_rate)
    #print(len(array))

    # i is the active state point in the window
    for i in range(pre_impact_win, len(array) - post_impact_win):

        data = array[i]
        #if data[9] == 1:


        act_state = data[9]
        microanno = data[8]

        dataFeatures = array[i - pre_impact_win : i + post_impact_win]
        x = timeit.default_timer()
        featureRes = featurescom.featurescom(dataFeatures, microanno,act_state)
        y = timeit.default_timer()

        run = y-x
        runtime.append(run)
        #print runtime
        csvWriter.writerow(featureRes)

    write_runtime(runtime, runtime_path)
    print('Finish Calculate Features')


def write_runtime(array_run, dest_file):
    outF = open(dest_file, "w")
    csvWriter = csv.writer(outF)

    for i in range(len(array_run)):
        runtime = array_run[i]
        csvWriter.writerow([runtime])




####################################### James Brusey's Code ##
#from collections import namedtuple                          #
#import copy                                                 #
#MyTuple = namedtuple('MyTuple', 'active, value')            #
                                                             #
#def grab_windows_from_stream(src, pre_win, post_win):       #
    #win = []                                                #
    #for tup in src:                                         #
        #if len(win) >= pre_win + post_win:                  #
            #win.pop(0)                                      #
        #win.append(tup)                                     #

        #if len(win) == pre_win + post_win:
            #if win[pre_win].active:
                #yield copy.deepcopy(win)

                
