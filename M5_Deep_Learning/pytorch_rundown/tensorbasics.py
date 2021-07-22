import torch 
import numpy as np

a = np.ones(5)
# print(a)

b = torch.from_numpy(a)
# print(b)

a +=1
# print(a)
# print(b)

x = torch.ones(5,requires_grad=True)
print(x)