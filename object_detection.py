import numpy as np
import cv2
from picamera import PiCamera
from time import sleep

# take picture with camera module and save as 'image.jpg'
# 2 second delay added to allow camera to focus
PiCamera().start_preview()
sleep(2)
PiCamera().capture('image.jpg')
PiCamera().stop_preview()

desired_detect = False

# initialize the list of class labels MobileNet SSD was trained to detect
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]

# then generate a random set of bounding box colors for each class
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

# load the MobileNet pre-trained model
print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe('MobileNetSSD_deploy.prototxt.txt', 'MobileNetSSD_deploy.caffemodel')

# load the input image
# resize to 300x300 pixels and then normalize
# normalization is done by MobileNet SSD
image = cv2.imread('im3.jpeg')
(h, w) = image.shape[:2]
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)

# pass the blob through the network and obtain the detections with predictions
print("[INFO] computing object detections...")
net.setInput(blob)
detections = net.forward()

# set threshhold for detections to 50% confidence
threshhold = 0.5

# loop over the detections
for i in np.arange(0, detections.shape[2]):
    # extract the confidence in the prediction
    confidence = detections[0, 0, i, 2]


    # filter out weak detections by ensuring the confidence is
    # greater than the threshhold confidence (50%)
    if confidence > threshhold:
        # extract the index of the class label from the detections,
        # then compute the (x, y)-coordinates of the bounding box for
        # the object
        idx = int(detections[0, 0, i, 1])
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")

        # display the prediction
        label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
        print("[INFO] {}".format(label))
        cv2.rectangle(image, (startX, startY), (endX, endY),
                      COLORS[idx], 2)
        y = startY - 15 if startY - 15 > 15 else startY + 15
        cv2.putText(image, label, (startX, y),
                    cv2.FONT_HERSHEY_TRIPLEX, 2, COLORS[idx], 2)

# has a person been detected
if 'person' in label:
    desired_detect = True
    import pygame as pg
    pg.mixer.init()
    pg.mixer.music.load("belltone.mp3")
    pg.mixer.music.play()
else:
    desired_detect = False




# resize output and show the output image
image = cv2.resize(image, (0,0), fx=0.25, fy=0.25)
cv2.imshow("Output", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


