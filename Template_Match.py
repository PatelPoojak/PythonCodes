import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help="input source image path", required=True)
ap.add_argument("-t", "--template", help="input template image path", required=True)
args = vars(ap.parse_args())

srcImage = cv2.imread(args["image"])
cv2.imshow("srcImage", srcImage)
cv2.waitKey()
tempImage = cv2.imread(args["template"])
cv2.imshow("templateImage", tempImage)
cv2.waitKey()

imageGrey = cv2.cvtColor(srcImage, cv2.COLOR_BGR2GRAY)
tempGrey = cv2.cvtColor(tempImage, cv2.COLOR_BGR2GRAY)

result = cv2.matchTemplate(imageGrey, tempGrey, cv2.TM_CCOEFF_NORMED)
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)

(startX, startY) = maxLoc
endX = startX + tempImage.shape[1]
endY = startY + tempImage.shape[0]

cv2.rectangle(srcImage, (startX, startY), (endX, endY), (255,0, 0), 2)
cv2.imshow("Image", srcImage)
cv2.waitKey(0)
