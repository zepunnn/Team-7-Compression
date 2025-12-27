import cv2
import numpy as np
from scipy.fftpack import dct, idct
from utils_progress import progress


def dct2(block):
    return dct(dct(block.T, norm="ortho").T, norm="ortho")


def idct2(block):
    return idct(idct(block.T, norm="ortho").T, norm="ortho")


def compress_image(path, block_size=8):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    h, w = img.shape

    pad_h = (block_size - h % block_size) % block_size
    pad_w = (block_size - w % block_size) % block_size
    padded = np.pad(img, ((0, pad_h), (0, pad_w)), mode="constant")

    blocks = []
    for i in progress(
        range(0, padded.shape[0], block_size),
        "Image DCT Compression",
        "row"
    ):
        for j in range(0, padded.shape[1], block_size):
            block = padded[i:i+block_size, j:j+block_size]
            blocks.append(dct2(block.astype(np.float32)))

    return blocks, padded.shape, img.shape


def decompress_image(blocks, padded_shape, original_shape, block_size=8):
    img = np.zeros(padded_shape, dtype=np.float32)
    idx = 0

    for i in progress(
        range(0, padded_shape[0], block_size),
        "Image Reconstruction",
        "row"
    ):
        for j in range(0, padded_shape[1], block_size):
            img[i:i+block_size, j:j+block_size] = idct2(blocks[idx])
            idx += 1

    return np.clip(img[:original_shape[0], :original_shape[1]], 0, 255).astype(np.uint8)