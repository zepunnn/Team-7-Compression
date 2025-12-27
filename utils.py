import math
import time
import numpy as np

def entropy(data):
    values, counts = np.unique(list(data), return_counts=True)
    probs = counts / counts.sum()
    return -np.sum(probs * np.log2(probs))

def timer(func, *args):
    start = time.time()
    result = func(*args)
    return result, time.time() - start

def psnr(original, reconstructed):
    mse = np.mean((original - reconstructed) ** 2)
    if mse == 0:
        return 100
    return 20 * math.log10(255.0 / math.sqrt(mse))