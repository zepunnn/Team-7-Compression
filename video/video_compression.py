import cv2
from image.dct_image import compress_image, decompress_image
from utils import psnr

def compress_video(path, max_frames=30):
    cap = cv2.VideoCapture(path)
    frames = []
    count = 0

    while cap.isOpened() and count < max_frames:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blocks, shape = compress_image_from_frame(gray)
        frames.append((blocks, shape))
        count += 1

    cap.release()
    return frames

def compress_image_from_frame(frame):
    import numpy as np
    from scipy.fftpack import dct

    blocks = []
    for i in range(0, frame.shape[0], 8):
        for j in range(0, frame.shape[1], 8):
            block = frame[i:i+8, j:j+8]
            if block.shape == (8, 8):
                blocks.append(dct(dct(block.T).T))
    return blocks, frame.shape