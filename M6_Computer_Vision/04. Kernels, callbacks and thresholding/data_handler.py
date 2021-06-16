from collections import OrderedDict

import numpy as np
import matplotlib.pyplot as plt
import time

import torch
from torch import nn
from torch import optim
import torch.nn.functional as F

from torchvision import datasets, transforms

def view_classify(img, ps):
    
    ps = ps.data.numpy().squeeze()

    fig, (ax1, ax2) = plt.subplots(figsize=(6,9), ncols=2)
    ax1.imshow(img.resize_(1, 28, 28).numpy().squeeze())
    ax1.axis('off')
    ax2.barh(np.arange(10), ps)
    ax2.set_aspect(0.1)
    ax2.set_yticks(np.arange(10))
    ax2.set_yticklabels(np.arange(10))
    ax2.set_title('Class Probability')
    ax2.set_xlim(0, 1.1)

def transformer():

    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5), (0.5)) ])
    return transform 

def train_transform():
    # Download and load the training data
    trainset    = datasets.MNIST('MNIST_data/', download=True, train=True, transform=transformer)
    trainloader = torch.utils.data.DataLoader(trainset, batch_size=32, shuffle=True)
    return trainset, trainloader

def test_transform():
    # Download and load the test data
    testset    = datasets.MNIST('MNIST_data/', download=True, train=False, transform=transformer)
    testloader = torch.utils.data.DataLoader(testset, batch_size=32, shuffle=True)

    return testset, testloader 

