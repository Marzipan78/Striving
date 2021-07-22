import torch

x =  torch.randn(3, requires_grad=False) # requires_grad=True, pytorch to save the gradient function used to compute the gradients
print(x)

y = x+2
print(y)

z = y*y*2
z = z.mean()    
print(z)

z.backward()    # dz/dx
print(x.grad)