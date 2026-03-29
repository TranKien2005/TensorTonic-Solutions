import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x = np.array(x)
    # Write code here
    res = 1 / (np.exp(-x) + 1)
    return res