'''
This module contains logic of pixel transforation.
which include gamma correction factor calualtion and transformation 
logic.
Adaptive gamma correction techinqe
'''
import cv2
import numpy as np
import math
import logging

logger=logging.getLogger(__name__)


def calculate_gamma_factor(image):
    '''
    calculate gamma factor value of each frame using mean of HSR image
    '''
    gamma = 1
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hue, sat, val = cv2.split(hsv)
    mid = 0.53
    mean = np.mean(val) 
    meanLog = math.log(mean)
    midLog = math.log(mid*255)
    gamma =meanLog/midLog
    logger.debug("mean: %s, meanlog: %s, midLog: %s, gamma: %s", mean,meanLog,midLog, gamma)
    return gamma


def apply_brightness_adjustment_gamma(image):
    """
    Adaptive gamma correction technique for brighness improvement
    """
    gamma = calculate_gamma_factor(image)
    
    #create lookup table for pixel trasnformation
    lookUpTable = np.empty((1,256), np.uint8)
    for i in range(256):
        lookUpTable[0,i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)
    
    #Transformae the image
    image_gamma = cv2.LUT(image, lookUpTable)
    #logger.debug("Input Image: %s", image_gamma)
    return image_gamma
