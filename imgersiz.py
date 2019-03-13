import PIL
from PIL import Image


basewidth = 600
img = Image.open('image.jpg')
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
img.save('image.jpg')


deep_learning_object_detection.py --prototxt 'MobileNetSSD_deploy.prototxt.txt' \
                                  --model 'MobileNetSSD_deploy.caffemodel' \
                                  --image 'image.jpg'


#python3.5 /home/pi/Desktop/obdet/object-detection-deep-\
#learning/deep_learning_object_detection.py \
#--prototxt /home/pi/Desktop/obdet/object-detection-deep-learning/MobileNetSSD_deploy.prototxt.txt \
#--model /home/pi/Desktop/obdet/object-detection-deep-learning/MobileNetSSD_deploy.caffemodel \
#--image /home/pi/Desktop/obdet/object-detection-deep-learning/images/doge.jpeg
