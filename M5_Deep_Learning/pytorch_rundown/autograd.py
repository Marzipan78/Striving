import torch

x =  torch.randn(3, requires_grad=True) # requires_grad=True, pytorch to save the gradient function used to compute the gradients
#print(x)

# y = x+2
# print(y)

# z = y*y*2   # will return multi-dimensional tensor, therefore it is important to specify the arg in the backward() function
# #z = z.mean()    # will return one value, since z is a scalar value there is no need to specify the arg in the backward() function
# print(z)

# v = torch.tensor([0.1, 1.0, 0.0001], dtype=torch.float32) # vector quant as the tchekovian multiplication requires it, the backward function is based on this.
# z.backward(v)    # dz/dx  
# print(x.grad)

"""Ways to stop the gadient tracking"""

# x.requires_grad_(False)
x.requires_grad_(False)
#print(x)

# x.detach() , creates a new tensor
p = x.detach()
#print(p)

# with torch.no_grad():  # this is a context manager, it is used to disable the gradient tracking

with torch.no_grad():
    q = x + 2
    #print(q)

"""Dummy train"""

weights = torch.ones(4, requires_grad=True)

for epoch in range(6):
    model_output = (weights * 3).sum()
    
    model_output.backward()
    
    print(weights.grad)

    weights.grad.zero_()  #  to avoid the gradient from accumulating

"""Using the Optimizer

optimizer = torch.optim.SGD(weights, lr=0.01)
optimizer.step()
optimizer.zero_grad()  # this is to clear the gradients, avoiding the accumulation of the gradients

"""