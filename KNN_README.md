# PythonCodes

NOTE: YOU MUST HAVE ARGUMENTS TO PASS, preferably from Kaggle Datasets

Code for KNN.
Hello. I will be explaining what the KNN Code does.
First, it gathers all the necessary libraries by importing them. Ex. Import cv2
Second, it brings the argument parser with Argparse, and adds the three arguments: Jobs, Neighbours, and Images.
Third, the list of image paths will be stored in ImagePaths with data = [] and label = [] being lists.
Fourth, the for i in range will set up a loop, which will enumerate the imagepaths.
Fifth, it resizes and appends all the images inserted, which is this case was from Kaggle.
Sixth, the data and label will set them in a array from numpy(np) from one of the imports(import numpy as np) as the response.
Seventh, it reshapes all the data and stores it in a variable called data.
After that, they store the label encoder in a variable "le". Then, they transform and fit those labels, which gets stored in another variable called "labels".
Then, it stores the datas and labels that go through train_test_split into another variable called "(trainx, testx, trainy, testy)".
Next, it grabs KNeighborsClassifier and puts the arguments of Jobs and Neighbours and puts them through n_neighbors, which gets stored in another variable called "model".
Then, it fits trainx and trainy in model.fit(trainx, trainy) with no variable, because it is not required.
Finally, with the data gathered, it will print it out through the classification_report from testy and testx which is predicted.
