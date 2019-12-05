#ID: CarminePanther
#Last edited: 11/18/2019 
#Source: Course Wiki
#Source: Help from Mr. Coker
#Source: https://stackoverflow.com/questions/30156098/how-to-get-unique-values-from-a-csv-file?rq=1




import matplotlib.pyplot as mplot 
import numpy as np
import csv
import statistics
import math
import string




dataTime=[]
dataX=[]
dataY=[]


#Re-Open the csv file to get fresh data for calculations
with open('Data/CarminePanther.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        dataTime.append(float(row[0]))
        dataX.append(float(row[1]))
        dataY.append(float(row[2]))


uniqueFreq = []

for x in dataX:
    key = x
    if key not in uniqueFreq:
        uniqueFreq.append(x)
 
print(uniqueFreq)




for y in uniqueFreq:


    xlist=[]
    ylist=[]

    for x in range(0, len(dataTime)):
        if dataX[x] == y:
            xlist.append(dataTime[x])
            ylist.append(dataY[x])

    mplot.scatter(xlist, ylist)

    if(np.corrcoef(xlist, ylist)[0][1] < -.95 or np.corrcoef(xlist, ylist)[0][1] > .28):

        print(np.corrcoef(xlist, ylist)[0][1])
    
            #LinearRegression
        slope = np.corrcoef(xlist, ylist)[0][1] * np.std(ylist) / np.std(xlist)
        b = np.mean(ylist) - (np.mean(xlist) * slope)

        yslope=[]
        for x in xlist:
            yslope.append((slope * x) + b)

        mplot.plot(xlist, yslope, color="red")



        #polynomial regression
        degree = 3
        model_params = np.polyfit(xlist, ylist, degree)
        xnew = np.float32(range(0,1000))
        xnew = xnew/10.0
        y_predicted = np.polyval(model_params, xnew)
        mplot.plot(xnew, y_predicted, color="blue")

        #General Scatter plot
        mplot.title('Challenge 5')
        mplot.xlabel('Time (ms)')
        mplot.ylabel('Signal Intensity')

mplot.show()
