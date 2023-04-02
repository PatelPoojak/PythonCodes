from imagesearch.nms import non_max_suppression
from imagesearch import config
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import argparse
import imutils
import pickle
import cv2
import winsound
from imutils.video import VideoStream
from imutils.video import FPS
import time


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

print("[INFO] loading model and label binarizer...")
model = load_model(config.MODEL_PATH)
lb = pickle.loads(open(config.ENCODER_PATH, "rb").read())

image = cv2.imread(args["image"])
image = imutils.resize(image, width=500)


#print("[INFO] starting video stream...")
#vs = VideoStream(src=0).start()
#time.sleep(2.0)
#fps = FPS().start()

#while True:
# grab the frame from the threaded video stream and resize it
# to have a maximum width of 400 pixels
#frame = vs.read()
#image = imutils.resize(frame, width=400)


print("[INFO] running selective search...")
ss = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()
ss.setBaseImage(image)
ss.switchToSelectiveSearchFast()
rects = ss.process()

proposals = []
boxes = []

for (x, y, w, h) in rects[:config.MAX_PROPOSALS_INFER]:
	# extract the region from the input image, convert it from BGR to
	# RGB channel ordering, and then resize it to the required input
	# dimensions of our trained CNN
	roi = image[y:y + h, x:x + w]
	roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
	roi = cv2.resize(roi, config.INPUT_DIMS,
		interpolation=cv2.INTER_CUBIC)

	# further preprocess by the ROI
	roi = img_to_array(roi)
	roi = preprocess_input(roi)

	# update our proposals and bounding boxes lists
	proposals.append(roi)
	boxes.append((x, y, x + w, y + h))


proposals = np.array(proposals, dtype="float32")
boxes = np.array(boxes, dtype="int32")
proba = model.predict(proposals)
labels = lb.classes_[np.argmax(proba, axis=1)]
idxs = np.where(labels == "raccoon")[0]

boxes = boxes[idxs]
proba = proba[idxs][:, 1]

idxs = np.where(proba >= config.MIN_PROBA)
boxes = boxes[idxs]
proba = proba[idxs]
clone = image.copy()
for (box, prob) in zip(boxes, proba):

	(startX, startY, endX, endY) = box
	cv2.rectangle(clone, (startX, startY), (endX, endY),
		(0, 255, 0), 2)
	y = startY - 10 if startY - 10 > 10 else startY + 10
	text= "Gun: {:.2f}%".format(prob * 100)
	cv2.putText(clone, text, (startX, y),
		cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 2)


#cv2.imshow("Before NMS", clone)


boxIdxs = non_max_suppression(boxes, proba)


for i in boxIdxs:

	winsound.Beep(440, 500)
	(startX, startY, endX, endY) = boxes[i]
	cv2.rectangle(image, (startX, startY), (endX, endY),
		(0, 255, 0), 2)
	y = startY - 10 if startY - 10 > 10 else startY + 10
	text= "Gun: {:.2f}%".format(proba[i] * 100)
	cv2.putText(image, text, (startX, y),
		cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 2)


cv2.imshow("After NMS", image)
cv2.waitKey(0)

	# show the output frame
	#cv2.imshow("Frame", frame)
	#key = cv2.waitKey(1) & 0xFF

	# if the `q` key was pressed, break from the loop
	#if key == ord("q"):
	#	break

	# update the FPS counter
	#fps.update()

#fps.stop()
#cv2.destroyAllWindows()
#vs.stop()