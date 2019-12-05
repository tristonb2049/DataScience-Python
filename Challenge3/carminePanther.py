 #ID: CarminePanther
#Last edited: 10/21/2019 
#https://stackoverflow.com/questions/26392336/importing-images-from-a-directory-python
#https://blackboard.olemiss.edu/webapps/blackboard/execute/content/file?cmd=view&content_id=_1401611_1&course_id=_54148_1
#https://honingds.com/blog/python-standard-deviation/
#https://snakify.org/en/lessons/print_input_numbers/

import matplotlib.pyplot as mplot 
import numpy as np
from PIL import Image
import glob
import collections
from statistics import stdev
import statistics

userThreshold = int(input("Enter your threshold. (Must be between 0 and 255) "))

if userThreshold > 255 or userThreshold < 0:
    print('Error, invalid range')
else:

    path = 'Images/*.jpg'
    image_list = []
    image_list2 = []

    files = glob.glob(path)
    for fle in files:
        img = Image.open(fle)
        img = np.float64(img)
        image_list.append(img)
        image_list2.append(img)

    averageImage = 0
    standardDeviation = 0

    
    #calculate average image
    for index in range(0, len(image_list)):
        averageImage+=image_list[index]

    averageImage/=len(image_list)



    #Display average image
    #averageImage = np.clip(averageImage, 0.0, 255.0)
    #averageImage = np.uint8(averageImage)
    '''
    mplot.imshow(averageImage)
    mplot.title('Average Image')
    mplot.show()
    '''
    
    #Calculate standard deviation
    imageArray = np.array(image_list2)
    standardDeviation = np.std(imageArray)

    print('Standard Devation:')
    print(standardDeviation)
    '''
    standardDeviation = np.clip(standardDeviation, 0.0, 255.0)
    standardDeviation = np.uint8(standardDeviation)
    
    mplot.imshow(standardDeviation)
    mplot.title('Standard Deviation')
    mplot.show()
    '''
    imageArray2 = np.std(image_list, axis=0)
    
    #loop thru image pixels and if the SD of the pixel is > the user input, change the pixel to red
    for row in range(0, len(averageImage)):
       for col in range(0, len(averageImage[row])):
            if(imageArray2[row][col] > userThreshold).any():
               averageImage[row][col]=[255.0, 0.0, 0.0]


    #Display image with red shaded in from user input
    averageImage = np.clip(averageImage, 0.0, 255.0)
    averageImage = np.uint8(averageImage)
    mplot.imshow(averageImage)
    mplot.title('Average image with user threshold')
    mplot.show()
