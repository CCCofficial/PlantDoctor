Code Instruction for Analyzing Images

5 scripts, ran from 1-5

1.Constants
2.get_mouse_subtract_2
3.analyze_color_subtract_5
4.plot_color_0
5.image_quality_check

Task 1: 
create a "xy_files" folder in the folder you code lives. 
You will need this "xy_files" folder in order to save 
the hsv value coordinates from your clicks

Create a "plot_results" folder in the folder you code lives. 
You will need this "plot_results" folder in order to save 
your plots

Create a "image_quality_results" folder in the folder you code lives. 
You will need this "image_quality_results" folder in order to save 
your image quality metrics

Specific Instructions for Running Code 

Before running Constants
-make sure to update the path to
    1.img

Then run Constants

Open get_mouse_subtract_2
 
-run and perform your clicks
-hit c to save your clicks and close the program
... check your "xy_files" at this point you should have
2 excel files,

one containing: the coordinates to the referance color chart clicks,
one containing: the coordinates to the sample clicks 

In order to organize your files 
in "xy_files" create two folders 

1. "reference_colorchart_coordinates"
2. "sample_coordinates"

Move your newly created excel files 
into their corresponding subfolders.

Return to Constants
Update the paths to 
    1.PIXEL_COORDINATES
    2.SAMPLE_PIXEL_COORDINATES
for your image, save and run


 
Open and Run analyze_color_subtract_5
Open plot_color_0
- change, axis_spacing to either...

          axis_spacing = [1,2,3,4,5]
          axis_spacing = [1,2,3,4,5,6,7]
          axis_spacing = [1,2,3,4,5,6,7,8,9,10]

depending on the number of clicks you performed,
usually it's 5 or 7 depending on the test.

IMPORTANT!!!!
Your number 
of clicks has to match the number of ticks for the 
axis spacing so each click can be plotted 


Run and get your plot, save in "plot_ results" 

Open and run image_quality_check, save in "image_quality_results"

Repeat this process for each new image.

We have organized our images by 
creating a folder(named the same as image name)
for each image and storing there the image and it's 
corresponding data. 

Each folder has the following 
1. image
2. xy_values(contains xy coordinates of reference)
3. xy_values_sample(contains the xy coordinates of sample and reference)
4. Fig.1 (plot1)
5. Fig.2 (plot2)
6. SoilData (metrics)

