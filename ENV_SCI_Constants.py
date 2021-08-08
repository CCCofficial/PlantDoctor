########Constants#########
from glob import glob
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
W=8
WS=16
import os

###################################choose either list of images or single image input#######################################################################
##img= []
##for filename in os.listdir(r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/images'):
##    if filename.endswith(".jpg"): 
##         img.append('images/'+filename)
##         continue
##    else:
##         continue
#img = r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/images/OAK_D-04-19-15-06-13_pH_no_direct_pH6.jpg'
#img = r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/images/OAK_D-04-19-15-05-13_pH_white_direct_pH6.jpg'
#img= r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/images/OAK_D-04-19-14-59-13_N_white_direct_surplus.jpg'
#img = r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/images/OAK_D-04-19-13-25-38_N_no_indirect_surplus.jpg'
#img=r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/images/OAK_D-04-19-14-56-37_N_no_direct_surplus.jpg'
#img =r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/images/OAK_D-04-19-13-25-04_white_indirect_surplus.jpg'
img=r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/images/food_coloring_daisy.jpg'
#img =r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/images/OAK_D-04-19-15-07-47_K_white_indirect_deficient.jpg'
####################################choose either list of xy_files or single file input ########################################################################
##PIXEL_COORDINATES=[]
##for filename in os.listdir(r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files'):
##   if filename.endswith(".csv"):
##            if filename.startswith("xy_values_O"):
##                PIXEL_COORDINATES.append('xy_files/'+filename)
##                continue
##            else:
##                continue
##
#PIXEL_COORDINATES = r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_OAK_D-04-19-15-06-13_pH_no_direct_pH6.jpg.csv'
#PIXEL_COORDINATES =r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_OAK_D-04-19-15-05-13_pH_white_direct_pH6.jpg.csv'
#PIXEL_COORDINATES=r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_OAK_D-04-19-14-59-13_N_white_direct_surplus.jpg.csv'
#PIXEL_COORDINATES= r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_OAK_D-04-19-13-25-38_N_no_indirect_surplus.jpg.csv'
#PIXEL_COORDINATES=r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_OAK_D-04-19-14-56-37_N_no_direct_surplus.jpg.csv'
#PIXEL_COORDINATES= r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_OAK_D-04-19-13-25-04_white_indirect_surplus.jpg.csv'
PIXEL_COORDINATES=r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_food_coloring_daisy.jpg.csv'
##SAMPLE_PIXEL_COORDINATES=[]
##for filename in os.listdir(r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files'):
##   if filename.endswith(".csv"):
##            if filename.startswith("xy_values_sample"):
##                SAMPLE_PIXEL_COORDINATES.append('xy_files/'+filename)
##                continue
##            else:
##                continue
#SAMPLE_PIXEL_COORDINATES=r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_sample_OAK_D-04-19-15-06-13_pH_no_direct_pH6.jpg.csv'
#SAMPLE_PIXEL_COORDINATES =r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_sample_OAK_D-04-19-15-05-13_pH_white_direct_pH6.jpg.csv'
#SAMPLE_PIXEL_COORDINATES=r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_sample_OAK_D-04-19-14-59-13_N_white_direct_surplus.jpg.csv'
#SAMPLE_PIXEL_COORDINATES= r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_sample_OAK_D-04-19-13-25-38_N_no_indirect_surplus.jpg.csv'
#SAMPLE_PIXEL_COORDINATES=r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_sample_OAK_D-04-19-14-56-37_N_no_direct_surplus.jpg.csv'
#SAMPLE_PIXEL_COORDINATES= r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_sample_OAK_D-04-19-13-25-04_white_indirect_surplus.jpg.csv'
SAMPLE_PIXEL_COORDINATES=r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_sample_food_coloring_daisy.jpg.csv'

##
##


#BLANK_PIXEL_COORDINATES= r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_blank_values_OAK_D-04-19-15-07-47_K_white_indirect.jpg.csv'





















###4/19###
##N_Test_HSV =('C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_OAK_D_12-15-03_N_white_indirect.jpeg.csv', 
##              'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_OAK_D_14-16-02_N_white_indirect.jpg.csv',
##              'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_OAK_D-04-19-12-50-35_N_no_indirect.jpg.csv',
##'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_OAK_D-04-19-13-04-31_N_white_indirect.jpg.csv',
##'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_OAK_D-04-19-14-58-36_N_no_direct.jpg.csv',
##'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_OAK_D-04-19-14-59-13_N_white_direct.jpg.csv',
##'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_OAK_D-04-19-15-00-13_N_white_direct.jpg.csv',
##'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_OAK_D-04-19-15-00-53_N_white_direct.jpg.csv',
##'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_OAK_D-04-12-12-15-03_N_white_indirect.jpeg.csv',
##'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_OAK_D-04-12-14-16-02_N_white_indirect.jpg.csv',
##'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_OAK_D-04-13-12-04-05 _N_white_indirect.jpg.csv',
##'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_OAK_D-04-13-12-04-05_N_white_indirect.jpg.csv',
##'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_OAK_D-04-19_13-04-31_N_white_indirect.jpg.csv')
##
##files_N=np.empty((0, 6),int)
##for f in N_Test_HSV:
##    files = np.loadtxt(f, delimiter = ',' ,dtype = "int")
##    files_N = np.append(files_N, files, axis = 0)

#PIXEL_COORDINATES=r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_OAK_D-04-19-13-04-31_N_white_indirect.jpg.csv'
#PIXEL_COORDINATES=r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_OAK_D-04-19-14-58-36_N_no_direct.jpg.csv'
#PIXEL_COORDINATES=r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_OAK_D-04-19-14-59-13_N_white_direct.jpg.csv'
#PIXEL_COORDINATES=r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_OAK_D-04-19-15-00-13_N_white_direct.jpg.csv'
#PIXEL_COORDINATES=r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_OAK_D-04-19-15-00-53_N_white_direct.jpg.csv'
#PIXEL_COORDINATES=r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_OAK_D-04-12-12-15-03_N_white_indirect.jpeg.csv'
#PIXEL_COORDINATES=r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_OAK_D-04-12-14-16-02_N_white_indirect.jpg.csv'
#PIXEL_COORDINATES=r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_OAK_D-04-13-12-04-05 _N_white_indirect.jpg.csv'
#PIXEL_COORDINATES=r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_OAK_D-04-13-12-04-05_N_white_indirect.jpg.csv'
#PIXEL_COORDINATES=r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_OAK_D-04-19_12-50-35_N_no_indirect.jpg.csv'
#PIXEL_COORDINATES=r'C:/Users/Familie Moeller/Desktop/Files/College/SFSU/2021 Spring/CSC 698/Plant Doctor/code/xy_files/xy_values_OAK_D-04-19_13-04-31_N_white_indirect.jpg.csv'
