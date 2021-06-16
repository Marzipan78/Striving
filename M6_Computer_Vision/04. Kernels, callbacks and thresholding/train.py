#model
from numpy.random import gamma
from torch import device
import torch
from model import Net 
import time 
#Data
import data_handler as dh
import numpy as np
from matplotlib import pyplot as plt

#torch
from torch.autograd import Variable
from torch.nn import CrossEntropyLoss, L1Loss, BCELoss, Softmax
from torch import optim
from torchsummary import summary

#metrics
from sklearn.metrics import accuracy_score

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")




def train(model, optimizer, criterion):

    train_loss = []
    val_loss = []

    epochs = 5
    print_every = 50

    #optimizer = optim.SGD(model.parameters(), lr=0.1)
    start_time = time.time()
    for e in range(epochs):
        running_loss = 0
        total = 0
        correct = 0
        print(f"Epoch: {e+1}/{epochs}")

        model.train()

        for i, (images, labels) in enumerate(iter(dh.train_transform())):

        
            images.resize_(images.size()[0], 1,28,28).cuda()
            
            optimizer.zero_grad()
            
            output = model.forward(images.cuda())   # 1) Forward pass
            loss = criterion(output.cuda(), labels.cuda()) # 2) Compute loss
            loss.backward()                  # 3) Backward pass
            optimizer.step()                 # 4) Update model
            
            running_loss += loss.item()

            train_loss.append(loss)
        
            
            if i % print_every == 0:
                print(f"\tIteration: {i}\t Loss: {running_loss/print_every:.4f}")
                running_loss = 0
            

        model.eval()
        with torch.no_grad():
            for i, (images, labels) in enumerate(iter(dh.test_transform())):
                images.resize_(images.size()[0], 1,28,28)
                outputs = model(images.cuda())
                _, predicted = torch.max(outputs.data, 1)
                total += labels.size(0)
                correct += (predicted == labels.cuda()).sum().item()
                #loss_val = criterion(output_val, y_val)
                #val_loss.append(loss_val)
        print('Accuracy of the network: %d %%' % (
            100 * correct / total))

    end_time = time.time()

    print(end_time-start_time)

    
model = Net()
criterion = CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)
if torch.cuda.is_available():
    model.cuda()
    criterion.cuda()

summary(model,(1, 28, 28))

train(model,optimizer,criterion)