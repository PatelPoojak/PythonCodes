import os
import cv2
import numpy as np
from imutils import paths
import argparse
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True)
ap.add_argument("-k", "--neighbours", required=True, type=int)
ap.add_argument("-j", "--jobs", required=True, type=int, default=-1)
args = vars(ap.parse_args())

imagepaths = list(paths.list_images(args["image"]))
data = []
labels = []

for i, imagepath in enumerate(imagepaths):
    image = cv2.imread(imagepath)
    image = cv2.resize(image, (32,32), interpolation=cv2.INTER_AREA)
    label = imagepath.split(os.path.sep)[-2]
    data.append(image)
    labels.append(label)

data = np.array(data)
labels = np.array(labels)

data = data.reshape(data.shape[0], 3072)
le = LabelEncoder()
labels = le.fit_transform(labels)
(trainx, testx, trainy, testy) = train_test_split(data, labels, test_size= 0.25, random_state=42)
model = KNeighborsClassifier(n_neighbors=args["neighbours"],n_jobs=args["jobs"])
model.fit(trainx, trainy)
print(classification_report(testy, model.predict(testx), target_names = le.classes_))
