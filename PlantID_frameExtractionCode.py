# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 13:47:28 2021

@author: choco
"""
import cv2
import os


#README: set path for video + path to save extracted frames to. 
#Must also change the number of frames to skip in the function + naming of the extracted frames.


#~~~~~~~~~~~defining plant video paths~~~~~~~~~~~~~~~~~~~~~
#path were mp4 video is
plantVideoPath = 'C:/Users/choco/depthai-python/examples/frame_extraction/strawberry/strawberry_video.mp4'
#path to save the images
extractedFramesPathToSave ='C:/Users/choco/depthai-python/examples/frame_extraction/strawberry'

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#https://www.geeksforgeeks.org/python-program-extract-frames-using-opencv/

def frameCapture(path, pathToSaveTo):   
    # Path to video file
    vidObj = cv2.VideoCapture(path)
  
    # Used as counter variable
    count = 0
  
    # checks whether frames were extracted
    success = 1
  
    while success:
  
        # vidObj object calls read
        # function extract frames
        success, image = vidObj.read()

  
        count += 1
        
        #loop to save frame for every n frames (n = 10 in this case)
        if count % 10 == 0:
            #add name of plant in image labels for reference!!!!!
            cv2.imwrite(os.path.join(pathToSaveTo , "frameTEST%d.jpg" % count),image)

    print("DONE")
    
    
#~~~~~~~~~~~calling function:~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
frameCapture(plantVideoPath, extractedFramesPathToSave)   

