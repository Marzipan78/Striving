# Forward pass :  compute loss
# compute local gradients
# backward pass :  compute gradients using chain rule
 
import torch 

x = torch.tensor(1.0)
y = torch.tensor(2.0)

w = torch.tensor(1.0, requires_grad=True)

#forward pass to compute loss
y_hat = w * x
loss = (y - y_hat)**2  
print(loss)

#backward pass to compute gradients
loss.backward()
print(w.grad)

#update weights
#next run forward pass with new weights