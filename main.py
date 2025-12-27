import os
import cv2

from utils import entropy, psnr
from utils_epub import read_epub_text

# Text compression
from text.huffman import huffman_encode, huffman_decode
from text.lzw import lzw_encode, lzw_decode

# Image compression
from image.dct_image import compress_image, decompress_image

# Video compression
from video.video_compression import compress_video


# ===============================
# TEMA 1 – TEXT COMPRESSION
# ===============================
def text_mode():
    path = input("Enter text file path (.txt / .epub): ").strip()

    if not os.path.exists(path):
        print("❌ File not found.")
        return

    # Handle TXT vs EPUB
    if path.lower().endswith(".epub"):
        print("📘 EPUB detected. Extracting text...")
        text = read_epub_text(path)
    else:
        text = open(path, encoding="utf-8", errors="ignore").read()

    print("\n--- TEXT COMPRESSION ---")
    print("Text length:", len(text))
    print("Entropy:", round(entropy(text), 4))

    # Huffman
    encoded, tree = huffman_encode(text)
    decoded = huffman_decode(encoded, tree)

    print("\n[Huffman Coding]")
    print("Compressed size:", len(encoded) // 8, "bytes")
    print("Decoded correct:", decoded == text)

    # LZW
    lzw_encoded = lzw_encode(text)
    lzw_decoded = lzw_decode(lzw_encoded)

    print("\n[LZW Compression]")
    print("Compressed codes:", len(lzw_encoded))
    print("Decoded correct:", lzw_decoded == text)


# ===============================
# TEMA 2 – IMAGE COMPRESSION
# ===============================
def image_mode():
    path = input("Enter image path (.png / .jpg): ").strip()

    if not os.path.exists(path):
        print("❌ File not found.")
        return

    print("\n--- IMAGE COMPRESSION ---")
    blocks, shape = compress_image(path)
    reconstructed = decompress_image(blocks, shape)

    original = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    value = psnr(original, reconstructed)

    print("Image shape:", original.shape)
    print("Total DCT blocks:", len(blocks))
    print("PSNR:", round(value, 2), "dB")


# ===============================
# TEMA 3 – VIDEO COMPRESSION
# ===============================
def video_mode():
    path = input("Enter video path (.mp4): ").strip()

    if not os.path.exists(path):
        print("❌ File not found.")
        return

    print("\n--- VIDEO COMPRESSION ---")
    frames = compress_video(path)

    print("Frames processed:", len(frames))
    print("Compression method: Frame-based DCT (grayscale)")


# ===============================
# MAIN MENU
# ===============================
def main():
    print("\n=== Coding & Compression Final Project ===")
    print("1. Text Compression")
    print("2. Image Compression")
    print("3. Video Compression")

    choice = input("Choose (1/2/3): ").strip()

    if choice == "1":
        text_mode()
    elif choice == "2":
        image_mode()
    elif choice == "3":
        video_mode()
    else:
        print("❌ Invalid choice.")


if __name__ == "__main__":
    main()