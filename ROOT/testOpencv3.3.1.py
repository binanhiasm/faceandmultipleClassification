import os
from PIL import Image
from numpy import *
import numpy as np
import cv2
import imutils
from os.path import exists
from matplotlib import pyplot as plt

print (cv2.__version__)

(major, minor, ac) = cv2.__version__.split(".")
img = cv2.imread("D:/test/IMG_0383.JPG",0)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 3:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.jpg',img)
    cv2.destroyAllWindows()
