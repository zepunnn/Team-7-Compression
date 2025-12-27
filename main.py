from text.huffman import huffman_encode, huffman_decode
from text.lzw import lzw_encode, lzw_decode
from image.dct_image import compress_image, decompress_image
from video.video_compression import compress_video
from utils import entropy, psnr
import cv2
import os

def text_mode():
    path = input("Enter text file path: ")
    if not os.path.exists(path):
        print("File not found.")
        return

    text = open(path, encoding="utf-8").read()

    encoded, tree = huffman_encode(text)
    decoded = huffman_decode(encoded, tree)

    print("Entropy:", entropy(text))
    print("Original size:", len(text.encode()), "bytes")
    print("Compressed size:", len(encoded) // 8, "bytes")
    print("Decoded correct:", decoded == text)

def image_mode():
    path = input("Enter image path: ")
    if not os.path.exists(path):
        print("File not found.")
        return

    blocks, shape = compress_image(path)
    recon = decompress_image(blocks, shape)

    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    print("PSNR:", psnr(img, recon))

def video_mode():
    path = input("Enter video path: ")
    if not os.path.exists(path):
        print("File not found.")
        return

    frames = compress_video(path)
    print("Total frames compressed:", len(frames))

def main():
    print("Select Compression Theme:")
    print("1. Text Compression")
    print("2. Image Compression")
    print("3. Video Compression")

    choice = input("Choose (1/2/3): ")

    if choice == "1":
        text_mode()
    elif choice == "2":
        image_mode()
    elif choice == "3":
        video_mode()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()