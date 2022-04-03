# USAGE
# python image_drawing.py

# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="blacknwhite.jpg",
   help="path to the input image")
args = vars(ap.parse_args())

# load the input image from disk
image = cv2.imread(args["image"])

# draw a circle around my face, two filled in circles covering my
# eyes, and a rectangle over top of my mouth
cv2.circle(image, (620, 370), 180, (0, 0, 255), 4)
cv2.circle(image, (580, 380), 10, (0, 0, 255), -1)
cv2.circle(image, (680, 380), 10, (0, 0, 255), -1)
cv2.rectangle(image, (580, 470), (680, 500), (0, 0, 255), 7)

# show the output image
cv2.imshow("Output", image)
cv2.waitKey(0)
