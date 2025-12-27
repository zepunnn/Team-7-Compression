import cv2
import numpy as np
from scipy.fftpack import dct, idct
from utils import psnr

def dct2(block):
    return dct(dct(block.T, norm='ortho').T, norm='ortho')

def idct2(block):
    return idct(idct(block.T, norm='ortho').T, norm='ortho')

def compress_image(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    img = img.astype(np.float32)

    blocks = []
    for i in range(0, img.shape[0], 8):
        for j in range(0, img.shape[1], 8):
            block = img[i:i+8, j:j+8]
            if block.shape == (8, 8):
                blocks.append(dct2(block))

    return blocks, img.shape

def decompress_image(blocks, shape):
    img = np.zeros(shape)
    idx = 0
    for i in range(0, shape[0], 8):
        for j in range(0, shape[1], 8):
            if idx < len(blocks):
                img[i:i+8, j:j+8] = idct2(blocks[idx])
                idx += 1
    return np.clip(img, 0, 255)