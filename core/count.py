import os
import cv2
import random
import numpy as np
import tensorflow as tf
from core.utils import read_class_names
from core.config import cfg

# function to count objects, can return total classes or count per class
def count_persons(data):#, by_class = False, allowed_classes = list(read_class_names(cfg.YOLO.CLASSES).values())):

    #boxes, scores, classes, num_objects = data
    classes, num_objects = data[2], data[3]
    #create dictionary to hold count of objects
    count_val = 0

    # if by_class = True then count objects per class
    #if by_class:
    #    class_names = read_class_names(cfg.YOLO.CLASSES)
    class_names = read_class_names(cfg.YOLO.CLASSES)
    # loop through total number of objects found
    for i in range(num_objects):
        # grab class index and convert into corresponding class name
        class_index = int(classes[i])
        class_name = class_names[class_index]
        if class_name == 'person':
          count_val += 1
        #if class_name in allowed_classes:
        #    counts[class_name] = counts.get(class_name, 0) + 1
        #else:
        #    continue
    
    return count_val
