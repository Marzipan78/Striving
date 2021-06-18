from collections import OrderedDict

import numpy as np
import matplotlib.pyplot as plt
import time

import torch
from torch import nn
from torch import optim
import torch.nn.functional as F

from torchvision import datasets, transforms

class Net(nn.Module):
    def __init__(self):
        super(Net,self).__init__()

        self.layer1 = nn.Sequential(
            nn.Conv2d(1,16,5),
            nn.BatchNorm2d(16),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2))
        self.layer2 = nn.Sequential(
            nn.Conv2d(16,32,5),
            nn.BatchNorm2d(32),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2))
     
        self.fc = nn.Sequential(
            nn.Linear(32 *4 *4,128),
            nn.ReLU(inplace =True),
            nn.Linear(128,64),
            nn.ReLU(inplace=True),
            nn.Linear(64,32),
            nn.Linear(32,10))
    
    def forward(self,x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
      

        return x

