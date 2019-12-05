#ID: CarminePanther
#Last edited: 9/13/2019 
#Source: https://realpython.com/python-csv/
#Source: https://appdividend.com/2019/01/28/python-statistics-tutorial-mean-function-example/




import matplotlib.pyplot as mplot 
import numpy as np
import csv
import statistics


#Create list to hold the correct data from 
correctData = []

#Loop thru the file and only store correct data to the created list
with open('CarminePanther_ch1.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if row[2] != ' 36.644939':
            correctData.append(row)
            

map(float, correctData)

xaxis = []
yaxis = []

for x in correctData:
    xaxis.append(float(x[0]))

for y in correctData:
    yaxis.append(float(y[1]))

count = 0.0
meanCount = 0.0
amplitude = 0.0
mean = 0.0
meanList = []
uniqueTimeStamp = []
uniqueTimeStamp.append(0.0)

for x in correctData:
    if float(x[0]) == count:
        amplitude += float(x[1])
        meanCount += 1.0
    else:       
        mean = amplitude/meanCount
        meanList.append(mean)
        count = float(x[0])
        meanCount = 1.0
        amplitude = float(x[1])
        uniqueTimeStamp.append(count)
        
meanList.append(amplitude/meanCount)



mplot.plot(uniqueTimeStamp, meanList, color="blue", linestyle="-")
mplot.scatter(xaxis, yaxis, color = 'red')
mplot.show()






    

        
    



