import numpy as np
import cv2
import matplotlib.pyplot as plt # for plotting histogram
import os
import Constants as C
import analyze_color_subtract_5 as acs
import plot_color_0 as plt0
#import get_mouse_subtract_2 as gms

header= 'FILENAME, H_VARIANCE, S_VARIANCE, S_MONOTINICITY, V_MONOTINICITY, S_DYNAMIC_RANGE, S_PREDICTED, USERVALUE'
Data ='C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/Soil_Data_File.csv'
soil_data=np.genfromtxt((Data),delimiter=',', dtype="object")



Dataset= str(os.path.split(C.PIXEL_COORDINATES)[-1])
print("Dataset: ", Dataset)
##HSV_values=
##S_HSV_values=
##hsv_v=np.genfromtxt(HSV_values,delimiter=',', dtype="int")
##s_hsv_v=np.genfromtxt(S_HSV_values,delimiter=',', dtype="int")
print('h', acs.h)
print('v', acs.v)
print('s', acs.s)

#check linearity
##calculate variance


h_variance= np.var(acs.h, dtype='int')
s_variance = np.var(acs.s, dtype='int')
print('variance in h: ', h_variance)
#print('variance in s' , s_variance)
#print('variance in h', h_variance)



#check monotinicity
ds = np.diff(acs.s)
s_m=np.all(ds <= 0) or np.all(ds >= 0)
print('Monotinicity in S', s_m)


dv = np.diff(acs.v)
v_m = np.all(dv <= 0) or np.all(dv >= 0)

print('Monotinicity in V', v_m)

#check dynamic range
dyn_range_s = np.amax(acs.s)-np.amin(acs.s)
dyn_range_h = np.amax(acs.h)-np.amin(acs.h)
print('dynamic range in s ', dyn_range_s)
print('dynamic range in h', dyn_range_h)

#What value is sample closest too
absolute_val_array = np.abs(acs.s - acs.ss[2])
#print(absolute_val_array)
smallest_difference_index = absolute_val_array.argmin()
closest_element_s = acs.s[smallest_difference_index]
#print('closest element in s: ', closest_element_s)
print('calclated x value in h: ', plt0.hx)

#print('calclated x value in s: ', plt0.sx)

##
absolute_val_array = np.abs(acs.v - acs.vs[2])
#print(absolute_val_array)
smallest_difference_index = absolute_val_array.argmin()
closest_element_v = acs.v[smallest_difference_index]
#print('closest element in v: ', closest_element_v)
#print('calclated x value in v: ', plt0.vx)


absolute_val_array = np.abs(acs.h - acs.hs[2])
#print(absolute_val_array)
smallest_difference_index = absolute_val_array.argmin()
closest_element_h = acs.h[smallest_difference_index]
#print('closest element in h: ', closest_element_h)



if len(acs.h)==7:
    my_xticks = ['pH 4.5','pH 5.0', 'pH 5.5', 'pH 6.0', 'pH 6.5', 'pH 7.0', 'pH 7.5']
    if closest_element_h==acs.h[0]:
        print('closest element in h: ', closest_element_h, my_xticks[0])
    elif closest_element_h==acs.h[1]:
        print('closest element in h: ', closest_element_h, my_xticks[1]) 
    elif closest_element_h==acs.h[2]:
        print('closest element in h: ', closest_element_h, my_xticks[2])
    elif closest_element_h==acs.h[3]:
        print('closest element in h: ', closest_element_h, my_xticks[3])
    elif closest_element_h==acs.h[4]:
       print('closest element in h: ', closest_element_h, my_xticks[4])
    elif closest_element_h==acs.h[5]:
        print('closest element in h: ', closest_element_h, my_xticks[5])
    elif closest_element_h==acs.h[6]:
       print('closest element in h: ', closest_element_h, my_xticks[6])
    if closest_element_s==acs.s[0]:
        print('closest element in s: ', closest_element_s, my_xticks[0])
    elif closest_element_s==acs.s[1]:
        print('closest element in s: ', closest_element_s,my_xticks[1]) 
    elif closest_element_s==acs.s[2]:
        print('closest element in s: ', closest_element_s,my_xticks[2])
    elif closest_element_s==acs.s[3]:
        print('closest element in s: ', closest_element_s,my_xticks[3])
    elif closest_element_s==acs.s[4]:
       print('closest element in s: ', closest_element_s,my_xticks[4])
    elif closest_element_s==acs.s[5]:
        print('closest element in s: ', closest_element_s,my_xticks[5])
    elif closest_element_s==acs.s[6]:
       print('closest element in s: ', closest_element_s,my_xticks[6])
    if closest_element_v==acs.v[0]:
        print('closest element in v ', closest_element_v, my_xticks[0])
    elif closest_element_v==acs.v[1]:
        print('closest element in v: ', closest_element_v,my_xticks[1]) 
    elif closest_element_v==acs.v[2]:
        print('closest element in s: ', closest_element_s,my_xticks[2])
    elif closest_element_v==acs.v[3]:
        print('closest element in s: ', closest_element_s,my_xticks[3])
    elif closest_element_v==acs.v[5]:
       print('closest element in v: ', closest_element_v,my_xticks[5])
    elif closest_element_v==acs.v[3]:
        print('closest element in s: ', closest_element_s,my_xticks[3])
    elif closest_element_v==acs.v[6]:
       print('closest element in v: ', closest_element_v,my_xticks[6])
elif len(acs.h)==5:
    #conc= [i in range len(pc[1,:])]
    my_xticks = ['Depleted','Deficient','Adequate', 'Sufficient', 'Surplus']
    if closest_element_h==acs.h[0]:
        print('closest element in h: ', closest_element_h, my_xticks[0])
    elif closest_element_h==acs.h[1]:
        print('closest element in h: ', closest_element_h, my_xticks[1]) 
    elif closest_element_h==acs.h[2]:
        print('closest element in h: ', closest_element_h, my_xticks[2])
    elif closest_element_h==acs.h[3]:
        print('closest element in h: ', closest_element_h, my_xticks[3])
    elif closest_element_h==acs.h[4]:
       print('closest element in h: ', closest_element_h, my_xticks[4])
    if closest_element_s==acs.s[0]:
        print('closest element in s: ', closest_element_s, my_xticks[0])
    elif closest_element_s==acs.s[1]:
        print('closest element in s: ', closest_element_s,my_xticks[1]) 
    elif closest_element_s==acs.s[2]:
        print('closest element in s: ', closest_element_s,my_xticks[2])
    elif closest_element_s==acs.s[3]:
        print('closest element in s: ', closest_element_s,my_xticks[3])
    elif closest_element_s==acs.s[4]:
       print('closest element in s: ', closest_element_s,my_xticks[4])
    if closest_element_v==acs.v[0]:
        print('closest element in v ', closest_element_v, my_xticks[0])
    elif closest_element_v==acs.v[1]:
        print('closest element in v: ', closest_element_v,my_xticks[1]) 
    elif closest_element_v==acs.v[2]:
        print('closest element in s: ', closest_element_s,my_xticks[2])
    elif closest_element_v==acs.v[3]:
        print('closest element in s: ', closest_element_s,my_xticks[3])
    elif closest_element_v==acs.v[4]:
       print('closest element in v: ', closest_element_v,my_xticks[4])



########## linear fit prediction #######################

userprediction="surplus"


header= 'FILENAME, H_VARIANCE, S_VARIANCE, S_MONOTINICITY, V_MONOTINICITY, S_DYNAMIC_RANGE, S_PREDICTED, USERVALUE'
features=np.array([[Dataset, h_variance, s_variance, s_m, v_m, dyn_range_s, closest_element_s, userprediction]], dtype="object")
####create array to save too##

FILENAME=0; H_VARIANCE=1; S_VARIANCE=2; S_MONOTINICITY=3; V_MONOTINICITY= 4; S_DYNAMIC_RANGE=5; S_PREDICTED=6; USERVALUE=7; MaxFeatures=8;
img_quality=np.empty((0,MaxFeatures), dtype='int')
img_quality=np.append(img_quality, features, axis=0 )
soil_data=np.append(soil_data, features, axis=0 )


c = np.savetxt('Soil_Data_File'+'.csv', features, header = header,fmt='%s',  delimiter = ',')
c = np.savetxt('Soil_Data_all'+'.csv', soil_data, header = header,fmt='%s',  delimiter = ',')
##

