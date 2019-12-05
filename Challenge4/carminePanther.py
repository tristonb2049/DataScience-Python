#ID: CarminePanther
#Last edited: 11/5/2019 
#Source: Course Wiki
#Source: Help from Mr. Coker
#Source: https://stackoverflow.com/questions/11559062/concatenating-string-and-integer-in-python
#Source: https://www.101computing.net/number-only/




import matplotlib.pyplot as mplot 
import numpy as np
import csv
import statistics
import math
import string


usX = []
usY = []

with open('Data/us_outline.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        usX.append(float(row[0]))
        usY.append(float(row[1]))


while True:
    try:
        kValue = int(input("Enter your k-value. (Cannot be less than 0)"))
    except ValueError:
        print("Input needs to be a number!")
        continue
    else:
        break

if(kValue < 0):
    print('K-value must also be greater than 0, please try again.')
else:
    x = [] 
    y = []
    z = []

    with open('Data/data.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            x.append(float(row[0]))
            y.append(float(row[1]))
            z.append(float(row[2]))

    #sqrt(pow[x2-x1]+pow[y2-y1])
    #Get distance function

    xList = []
    yList = []
    zList = []

    for a in range(0, 194):
        for b in range(0, 120):
            distanceList = []
            for c in range(len(x)):
                #a is x b is y coord - append this line
                distanceList.append([math.sqrt(math.pow(x[c]-a,2)+math.pow(y[c]-b,2)), c])
                #distanceList.append(math.sqrt((c-a)**2 + (c-b)**2))

            #sort dataList distance.sort
            distanceList.sort()

            #another for loop 0-user k valu
            total = 0.0
            for d in range(0, kValue):
                total = total + z[distanceList[d][1]]   

            kAverage = total/kValue
        

            xList.append(a)
            yList.append(b)
            zList.append(kAverage)

            #add d-value for average
            #leave forloop and divide by k





    mplot.plot(usX, usY, color="black", linestyle="-")
    mplot.scatter(xList, yList, c=zList, cmap="viridis")
    mplot.title('K-Value = ' + str(kValue))
    mplot.show()