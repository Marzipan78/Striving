import torch

x =  torch.randn(3, requires_grad=True) # requires_grad=True, pytorch to save the gradient function used to compute the gradients
print(x)

y = x+2
print(y)

z = y*y*2   # will return multi-dimensional tensor, therefore it is important to specify the arg in the backward() function
#z = z.mean()    # will return one value, since z is a scalar value there is no need to specify the arg in the backward() function
print(z)

z.backward()    # dz/dx  
print(x.grad)