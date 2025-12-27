import cv2
import numpy as np
from scipy.fftpack import dct, idct
from utils_progress import progress
from utils import psnr


def dct2(block):
    return dct(dct(block.T, norm="ortho").T, norm="ortho")


def idct2(block):
    return idct(idct(block.T, norm="ortho").T, norm="ortho")


def process_blocks(img, block_size=8):
    h, w = img.shape
    blocks = []

    for i in range(0, h - block_size + 1, block_size):
        for j in range(0, w - block_size + 1, block_size):
            blocks.append(dct2(img[i:i+block_size, j:j+block_size]))

    return blocks, (h, w)


def reconstruct_blocks(blocks, shape, block_size=8):
    h, w = shape
    img = np.zeros(shape, dtype=np.float32)
    idx = 0

    for i in range(0, h - block_size + 1, block_size):
        for j in range(0, w - block_size + 1, block_size):
            img[i:i+block_size, j:j+block_size] = idct2(blocks[idx])
            idx += 1

    return np.clip(img, 0, 255).astype(np.uint8)


def compress_video(path, frame_skip=3):
    cap = cv2.VideoCapture(path)
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    compressed = []
    originals = []

    for idx in progress(range(total), "Video Compression", "frame"):
        ret, frame = cap.read()
        if not ret:
            break

        if idx % frame_skip != 0:
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY).astype(np.float32)
        blocks, shape = process_blocks(gray)

        compressed.append((blocks, shape))
        originals.append(gray.astype(np.uint8))

    cap.release()
    return compressed, originals


def reconstruct_frames(compressed_frames):
    return [
        reconstruct_blocks(blocks, shape)
        for blocks, shape in progress(
            compressed_frames, "Video Reconstruction", "frame"
        )
    ]


def calculate_psnr_frames(originals, reconstructed):
    values = [
        psnr(o, r)
        for o, r in progress(
            zip(originals, reconstructed),
            "PSNR Calculation",
            "frame"
        )
    ]
    return sum(values) / len(values)