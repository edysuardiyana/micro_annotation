__author__ = 'ArseneLupin'

#this program is used to windowing the signal. The window width is 1 second (100Hz) and it will slide about 50%


import csv

from collections import deque

sourcefile = "/Users/ArseneLupin/Desktop/scaled/bimo.csv"
destfile = "/Users/ArseneLupin/Desktop/window/bimo.csv"
windowCounter = 0
flagwindow = True
winque = deque()

with open(sourcefile) as FileObject:

    for line in FileObject:
        if winque.__len__() == 1200:
            #print("masuk 12")
            outF = open(destfile, "a")
            csvWriter = csv.writer(outF, delimiter='\t')
            for n in range(1,1200):
                if n > 599:
                    output = winque.popleft()
                    csvWriter.writerow(output)
                    winque.append(output)
                else:
                    output = winque.popleft()
                    csvWriter.writerow(output)
            outF.close()
            windowCounter += 1
            if windowCounter == 100:
                break
        else:
            data = line.split()
            winque.append(data)







