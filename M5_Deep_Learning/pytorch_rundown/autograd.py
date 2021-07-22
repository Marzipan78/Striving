import torch

x =  torch.randn(3, requires_grad=True) # requires_grad=True, pytorch to save the gradient function used to compute the gradients
print(x)

y = x+2
print(y)

z = y*y*2   # will return multi-dimensional tensor, therefore it is important to specify the arg in the backward() function
#z = z.mean()    # will return one value, since z is a scalar value there is no need to specify the arg in the backward() function
print(z)

v = torch.tensor([0.1, 1.0, 0.0001], dtype=torch.float32) # scalar quant as the tchekovian multiplication requires it, the backward function is based on this.
z.backward(v)    # dz/dx  
print(x.grad)