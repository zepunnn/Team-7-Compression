import cv2
import numpy as np
from scipy.fftpack import dct, idct

# =========================
# DCT helpers
# =========================
def dct2(block):
    return dct(dct(block.T, norm="ortho").T, norm="ortho")

def idct2(block):
    return idct(idct(block.T, norm="ortho").T, norm="ortho")


# =========================
# Padding helpers
# =========================
def pad_image(img):
    h, w = img.shape
    pad_h = (8 - h % 8) % 8
    pad_w = (8 - w % 8) % 8

    padded = np.pad(
        img,
        ((0, pad_h), (0, pad_w)),
        mode="edge"
    )
    return padded, (h, w)


# =========================
# Compression
# =========================
def compress_image(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    img = img.astype(np.float32)

    padded, original_shape = pad_image(img)
    h, w = padded.shape

    blocks = []
    for i in range(0, h, 8):
        for j in range(0, w, 8):
            block = padded[i:i+8, j:j+8]
            blocks.append(dct2(block))

    return blocks, padded.shape, original_shape


# =========================
# Decompression
# =========================
def decompress_image(blocks, padded_shape, original_shape):
    h, w = padded_shape
    img = np.zeros((h, w), dtype=np.float32)

    idx = 0
    for i in range(0, h, 8):
        for j in range(0, w, 8):
            img[i:i+8, j:j+8] = idct2(blocks[idx])
            idx += 1

    # Crop back to original size
    oh, ow = original_shape
    return np.clip(img[:oh, :ow], 0, 255)