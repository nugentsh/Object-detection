Allows for pictures to be taken with camera module and then image is processed to find some objects that the neural network
has been trained to recognise.
Image Resizing file exists if an image which has not been taken by the camera is used and is too large to be displayed
with raspberry pi.

Uses pre-trained Mobilenet SSD neural network, developed by Google

Files have not yet been brought together into one final program yet.

With files in folder called 'object-detection' on the desktop
Use command:
python3.5 /home/pi/Desktop/object-detection/object_detection.py \
--prototxt /home/pi/Desktop/object-detection/MobileNetSSD_deploy.prototxt.txt \
--model /home/pi/Desktop/object-detection/MobileNetSSD_deploy.caffemodel \
--image /home/pi/Desktop/object-detection/image.jpg


---update----
Now runs object detection through a trigger program
'myTrigger' takes button input, then calls the updated object detection function
main function now has the picture taking task within its script
no more need for calling through commands
removed parsing of arguments
program now has model manually inputted
