import cv2
import numpy as np
import os


def OpenCVCheck(x,y):
    tempx = '<ADD FIRST FILE PATH>'+ x
    tempy = '<ADD SECOND FILE PATH>'+y
    i1 = cv2.imread(tempx)
    i2 = cv2.imread(tempy)
    if i1 is None:
        print("Nonetype: ", tempx)
        return
    elif i2 is None:
        print("Nonetype: ", tempy)
        return
    if i1.shape == i2.shape:
        difference = cv2.subtract(i1, i2)
        b, g, r = cv2.split(difference)
        if(cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0):
            print(x)
            return
    return
    
first_filepath = os.listdir('<ADD FIRST FILE PATH>')
second_filepath = os.listdir('<ADD SECOND FILE PATH>')
Total = len(first_filepath)*len(second_filepath)
countDown = 0
progress = 0
for i in first_filepath:
    for j in second_filepath:
        if(i == j):
            print(i, '\n')
        if(progress != (countDown*100)//Total):
            progress = (countDown*100)//Total
            print('Progress: %', (countDown*100)//Total)
        OpenCVCheck(i,j)
        countDown += 1
print("process ended")
