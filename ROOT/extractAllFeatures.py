import os
from PIL import Image
from numpy import *
import numpy as np
import imutils
from os.path import exists
from matplotlib import pyplot as plt
import cv2


DIR_DATA = "data"
DIR_FEATURES = os.path.join(DIR_DATA,"features")
DIR_SAMPLES = os.path.join(DIR_DATA,"samples")
DIR_DATASET = os.path.join(DIR_DATA,"dataset")
NAME_DEFINE = "define.txt"
NAME_TEST_LABEL = "test_label.txt"
NAME_TEST_DIR = "test_dir.txt"
NAME_TRAIN_LABEL = "train_label.txt"
NAME_TRAIN_DIR = "train_dir.txt"
#extract sift features of an image
def extract_features(path):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sift = cv2.xfeatures2d.SIFT_create()
    (kps, descs) = sift.detectAndCompute(gray, None)
    return descs

def define_label():
    file_define = open(os.path.join(DIR_DATA,NAME_DEFINE),"w")
    list_dir = os.listdir(DIR_DATASET)
    print(len(list_dir))
    num = 0
    for each_dir in range(0,len(list_dir)):
        count = 0
        list_img = os.listdir(os.path.join(DIR_DATASET,list_dir[each_dir]))
        for each_img in range(0, len(list_img)):
            file_define.write(str(os.path.join(DIR_DATASET,list_dir[each_dir],list_img[each_img]))+"\t"+str(list_dir[each_dir])+"\n")
            count +=1
        num += count
    print (num)
    file_define.close()
define_label()