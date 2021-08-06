import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

rootdir = r'/Users/ablej/Downloads/Spring 2021/Microscopy/PD-Spectral/ScreenShots used for NDVI'
dict={}
for subdir, dirs, files in os.walk(rootdir): #loop through files and folder
    eachday=[]
    if subdir[-2] == 'D': #how we identy the days folder
        #print(subdir[-2:])
    #if subdir[-2:] == 'D1':
        #print('newloop')
        L1 = [os.path.join(subdir, file) for file in files if file[-5] == "1"] #identify each leaf in folder
        L2 = [os.path.join(subdir, file) for file in files if file[-5] == "2"]
        L3 = [os.path.join(subdir, file) for file in files if file[-5] == "3"]
        L4 = [os.path.join(subdir, file) for file in files if file[-5] == "4"]
        eachday.extend([L1,L2,L3,L4])
        dict[subdir[-2:]] = eachday #pairs directory of each leaf (rgb,ir) for each pair in a list per day

def getndvi(pic1,pic2): #this function gets the ndvi for each image pair for each day
    if 'RGB' in pic1:
        rgb = cv2.imread(pic1)
        ir = cv2.imread(pic2)
    if 'RGB' in pic2:
        rgb = cv2.imread(pic2)
        ir = cv2.imread(pic1)
    rgb_avg_color_per_row = np.average(rgb, axis=0)
    rgb_avg_color = np.average(rgb_avg_color_per_row, axis=0)  #returns in [b.g,r]
    ir_avg_color_per_row = np.average(ir, axis=0)
    ir_avg_color = np.average(ir_avg_color_per_row, axis=0)  #returns in [b.g,r]
    ndvi = ((ir_avg_color[0]-rgb_avg_color[2])/(ir_avg_color[0]+rgb_avg_color[2]))
    #print('NDVI:', ndvi,' Red Channel:',rgb_avg_color[2],' IR Channel:',ir_avg_color[0])
    return ndvi

NDVIdict={}
for day in dict:
    ndviperday=[]
    for leaves in dict[day]:
        print(leaves)
        ndvi = getndvi(leaves[0],leaves[1])
        ndviperday.append(ndvi)
    NDVIdict[day] = ndviperday

#create plot
testl=[]
days=[]
x=1
tmp =[]
def recursivetry(x,days): #this function sorts the keys in the NDVIdict (D1,D4,D5..D7) from D1 to D7
    if len(days) == 7:
        print(days)
        return
    for day in NDVIdict:
        if int(day[-1]) == x:
            days.append(day)
            x = x + 1
    return recursivetry(x,days)

#call the function and create the plot
recursivetry(x,days)
for d in days:
    testl.append(tuple(NDVIdict[d]))
for xe, ye in zip(days, testl):
    plt.scatter([xe] * len(ye), ye)
plt.savefig('Graph of NDVI over 7 days.png')

