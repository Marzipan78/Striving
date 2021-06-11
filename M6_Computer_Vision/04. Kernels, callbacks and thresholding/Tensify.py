import cv2
from collections import OrderedDict
import pickle

import numpy as np
import matplotlib.pyplot as plt
import time

import torch
from torch import nn
from torch import optim
import torch.nn.functional as F

from torchvision import datasets, transforms

class Tensify():

    def imagify(path,img):
        
        image = path + img
        number = cv2.imread(image,cv2.IMREAD_GRAYSCALE)
        img = cv2.blur(number, (9, 9))
        _, img = cv2.threshold(img, 175, 255, cv2.THRESH_TRUNC)
        img = cv2.resize(img, (28, 28), interpolation=cv2.INTER_LANCZOS4)
        
        img = cv2.bitwise_not(img)
        plt.figure(figsize = (10, 10))
        plt.imshow(img)
        return img 

    def tensed(number):
        tensed_number = torch.from_numpy(number).float()
        F.normalize(tensed_number)
        flat_number = tensed_number.reshape(-1,784)
        return flat_number

