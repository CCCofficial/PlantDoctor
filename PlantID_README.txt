 == Contributors ==
Johana Aleman, Patra Holmes 

 == Module Description ==
The Plant Identification module is responsible for identifying 8 plant species which includes apple, bell pepper, grape, orange, peach, raspberry, strawberry, tomato.
We used transfer learning to train two different models: MobileNetv2-SSD and VGG16.
MobileNetv2-SSD can be ran on the OAK-D because it's an SSD model, but VGG16 cannot because it is a traditional CNN and therefore too large to be ran on the OAK-D camera.

 == Data Folder ==
This folder stores the Kaggle datasets of plant leaves where each image has the class type in the file name. It contains two subfolders:training and testing. 
The images were split 70-20, where 70% were placed in the training folder and 20% in the testing folder.
The training folder has the images that were used to train both MobileNetv2-SSD and VGG16 model.
The testing folder has the images used for the testing of the CNNs to get accuracy scores. 

== SSD_model_files ==
Contains the saved_model.pb, frozen_inference_graph.pb, and pipeline.config files for the MobileNetv2-SSD that was trained on 300 color images per class.

== SSD_matrix.png ==
Confusion matrix from training and testing MobileNetv2-SSD on the Kaggle dataset. Inference was run on CoLab using the plantDocMobilenet.ipnyb file. 

== IR-and_blob ==
Contains .blob, .bin, and .xml files of SSD_model_files after conversion with openVINO

== oak_d_test ==
Contains images taken with the OAK-D of whole plants. Model could not classify them accurately. 


 == test_inference Folder ==
This folder stores screenshots of the MobileNetv2-SSD model identifying plant species from the Kaggle dataset on collar with the ipynb file, not from the OAK-D camera.
Each subdirectory is labeled by the plant species. Each image is named by true plant species and if it is classified as a true or false positive. 
The class name label identified by the model inside the screenshot sometimes is out of bounds, but the color of the bounding box is the same for each class.
If the class label in the image is not shown, use the bounding box color to determine what class the model identified the leaf image as.

We used this folder to create the confusion matrix for the MobileNetv2-SSD model ourselves since the VGG16 model already created the confusion matrix when training the model.

== Data ==
Contains the images from Kaggle that we trained our first VGG-16 with. 300 images per class for training, and 45 for testing.


== ssd.tfrecord.zip ==
Contains the training dataset made from the original Kaggle dataset using Roboflow. Contains the original 300 color images per class, plus 245 with -25% brightness, 245 either rotated or inverted, and 150 black and white. This was done to allow for more flexibility in the orientation and lighting when performing inference.

== oakd_testing == 
Contains the 15 images per class taken with the OAK-D that were used to check inference abilities of the MobileNetv2-SSD trained on the ssd.tfrecord.zip dataset. Only 6 plants were available to get images of in our gardens out of the total 8 classes the model was trained on. Inference was run on CoLab using these.

== inf_oakd_20100 ==
Contains the inference from the .ipynb file on CoLab. Inference was on the images from oakd_testing folder. Inference was done after training the MobileNetv2-SSD after training for 20100 steps. Inference data was then used to generate the oakd_ssd_matrix.png confusion matrix.

== oakd_ssd_matrix.png ==
The confusion matrix generated after running inference on OAK-D images on CoLab of the trained MobileNetv2-SSD. Misclassified bell peppers as orange, and did not detect a few images - which is why it looks as if there were not 15 images per class. Results show that either model was under/over-trained or that the dataset must be curated further for the model to perform better. 

== codeToRunCNN_onCamea_TESTING.py ==
This python file is what our team used to run the saved trained models onto the OAK-D cameras to test our models.
We do this by connecting the OAK-D to our computer then running this script from the command prompt. 


 == frameExtractionCode.py ==
This python file can be used to extract frames from recorded video taken with the OAK-D camera. 
You must first set the paths for the video directory at the top of the script and input the number of frames to skip inside the frameCapture function.
Once this code is ran the extracted images will be saved to the directory specified at the top of the script inside the variable extractedFramesPathToSave. 
Each image file will be named based on the plant species name inside the text of the frameCapture function.

This code is particularly helpful when wanting to obtain many images from a plant to do machine learning. 


 == plantDocVGG16.ipynb ==
This is the script that was used to train and save the VGG16 model. We ran this script on Google Colab. 

 == plantDocMobilenet.ipynb ==
This is the script that was used to train and save the MobileNetv2-SSD model. It also has the inference code after training which output the images inside the test_inference folder.
We ran this script on Google Colab. 

 == SSD_matrix.png == 
This image is the confusion matrix of our trained MobileNetv2-SSD model. The diagonal line shows that our trained model has high accuracy levels.

 == vgg16_matrix.png == 
This image is the confusion matrix of our trained VGG16 model. The diagonal line shows that our trained model has high accuracy levels.
