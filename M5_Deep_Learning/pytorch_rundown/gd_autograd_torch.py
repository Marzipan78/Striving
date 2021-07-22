"""USING NUMPY """
import numpy as np

# f = w * x
# f = 2 * x

X = np.array([1, 2, 3, 4], dtype=np.float32)
Y = np.array([2, 4, 6, 8], dtype=np.float32)	# y = 2 * x

w = 0.0

# model prediction
def forward(x):
    return w * x

# loss = MSE
def loss(y, y_predicted):
    return ((y - y_predicted) ** 2).mean()

# gradient
# MSE = 1/N * (w*x - y)^2
# d/dw = 1/N * x * (w*x - y)

def gradient(x, y, y_predicted):
    return np.dot(2 * x , y_predicted-y).mean() 

print(f'Prediction before training: f(5) = {forward(5):.3f}')

# Training loop
lr = 0.01
n_iters = 10

for epoch in range(n_iters):
    # prediction forwards pass
    y_pred = forward(X)

    # loss
    l = loss(Y, y_pred) 

    # gradients
    dw = gradient(X, Y, y_pred)

    # update weights
    w -= lr * dw

    if epoch % 1 == 0:
        print(f'epoch: {epoch +1}, w: {w:.3f}, loss = {l:.8f}')

print(f'Prediction after training: f(5) = {forward(5):.3f}')