import torch

x =  torch.randn(3, requires_grad=True) # requires_grad=True, pytorch to save the gradient function used to compute the gradients
print(x)

y = x+2
print(y)