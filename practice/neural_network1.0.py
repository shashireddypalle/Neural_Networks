import numpy as np

def neunet(m1, m2, m3, w1, w2, w3, b):
    z = ((m1*w1) + (m2*w2) + (m3*w3) + b)
    return sigmoid(z)

def sigmoid(z):
    return (1/(1+np.exp(-z)))

def cost(b):
    return (b-4)**2

# Random variable generated to create random initial weights
w1 = np.random.randn()
w2 = np.random.randn()
w3 = np.random.randn()
b = np.random.randn()

np.random.rand()