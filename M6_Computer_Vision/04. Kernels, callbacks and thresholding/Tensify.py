import cv2
from collections import OrderedDict
import numpy as np
import matplotlib.pyplot as plt
import time
import torch
from torch import nn
from torch import optim
import torch.nn.functional as F

from torchvision import datasets, transforms
from PIL import Image
import pytesseract

class Tensify():

    def image_reader(path,img):
        image = path + img
        numbers = cv2.imread(image,cv2.IMREAD_GRAYSCALE)
        plt.imshow(numbers, cmap='gray')
        return numbers
    
    # def rotator(img):
           
    #     img = Image.open(img)
    #     rotated_img = img.transpose(Image.ROTATE_270)
    #     plt.imshow(rotated_img)
    #     return  rotated_img       

    # def detector(img):
    #     imgheight=img.shape[0]
    #     imgwidth=img.shape[1]
    #     y1 = 0
    #     M = imgheight//20
    #     N = imgwidth//20
    #     for y in range(0,imgheight,M):
    #         for x in range(0, imgwidth, N):
    #             y1 = y + M
    #             x1 = x + N
    #             tiles = img[y:y+M,x:x+N]

    #             cv2.rectangle(img, (x, y), (x1, y1), (0, 255, 0))
    #             cv2.imwrite("save/" + str(x) + '_' + str(y)+".png",tiles)
        
    #     cv2.imwrite("digdiv.png",img)

    def imagify(path,img):
        
        image = path + img
        number = cv2.imread(image,cv2.IMREAD_GRAYSCALE)
        
        
        img = cv2.blur(number, (9, 9))
        _, img = cv2.threshold(img, 175, 255, cv2.THRESH_TRUNC)
        img = cv2.resize(img, (28, 28), interpolation=cv2.INTER_LANCZOS4)
        
        img = cv2.bitwise_not(img)
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
        ax1.imshow(number, cmap='gray');
        ax2.imshow(img);
        return img


    def tensed(number):
        tensed_number = torch.from_numpy(number).float()
        F.normalize(tensed_number)
        flat_number = tensed_number.reshape(-1,784)
        return flat_number

    def cnn_tensed(number):
       tensed_number = torch.from_numpy(number).float()
       F.normalize(tensed_number)
       cnn_number = tensed_number.reshape(-1,1,28,28)
       return cnn_number



