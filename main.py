import os
import cv2

from utils import entropy, psnr
from utils_epub import read_epub_text
from utils_text import normalize_text
from utils_result import ensure_dir, write_log, timestamp

# Text
from text.huffman import huffman_encode, huffman_decode
from text.lzw import lzw_encode, lzw_decode

# Image
from image.dct_image import compress_image, decompress_image

# Video
from video.video_compression import compress_video


# ===============================
# TEMA 1 – TEXT
# ===============================
def text_mode():
    path = input("Enter text file path (.txt / .epub): ").strip()
    if not os.path.exists(path):
        print("❌ File not found.")
        return

    ensure_dir("results/text")

    if path.lower().endswith(".epub"):
        print("📘 EPUB detected. Extracting text...")
        text = read_epub_text(path)
    else:
        text = open(path, encoding="utf-8", errors="ignore").read()

    ent = entropy(text)
    text_norm = normalize_text(text)

    # Huffman
    encoded, tree = huffman_encode(text_norm)
    decoded = huffman_decode(encoded, tree)

    with open("results/text/huffman.bin", "w") as f:
        f.write(encoded)

    # LZW
    lzw_encoded = lzw_encode(text_norm)
    lzw_decoded = lzw_decode(lzw_encoded)

    with open("results/text/lzw.txt", "w") as f:
        f.write(" ".join(map(str, lzw_encoded)))

    log = (
        f"[{timestamp()}]\n"
        f"Dataset: {path}\n"
        f"Entropy: {ent:.4f}\n"
        f"Huffman size: {len(encoded)//8} bytes\n"
        f"LZW codes: {len(lzw_encoded)}\n"
        f"Huffman OK: {decoded == text_norm}\n"
        f"LZW OK: {lzw_decoded == text_norm}\n"
        f"-------------------------"
    )
    write_log("results/text/log.txt", log)

    print("✅ Text results saved to results/text/")


# ===============================
# TEMA 2 – IMAGE
# ===============================
def image_mode():
    path = input("Enter image path (.png / .jpg): ").strip()
    if not os.path.exists(path):
        print("❌ File not found.")
        return

    ensure_dir("results/image")

    blocks, padded_shape, original_shape = compress_image(path)
    reconstructed = decompress_image(blocks, padded_shape, original_shape)

    original = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    value = psnr(original, reconstructed)

    cv2.imwrite("results/image/reconstructed.png", reconstructed)

    log = (
        f"[{timestamp()}]\n"
        f"Dataset: {path}\n"
        f"Original shape: {original.shape}\n"
        f"DCT blocks: {len(blocks)}\n"
        f"PSNR: {value:.2f} dB\n"
        f"-------------------------"
    )
    write_log("results/image/log.txt", log)

    print("✅ Image results saved to results/image/")


# ===============================
# TEMA 3 – VIDEO
# ===============================
def video_mode():
    path = input("Enter video path (.mp4): ").strip()
    if not os.path.exists(path):
        print("❌ File not found.")
        return

    ensure_dir("results/video")

    frames = compress_video(path)

    log = (
        f"[{timestamp()}]\n"
        f"Dataset: {path}\n"
        f"Frames processed: {len(frames)}\n"
        f"Method: Frame-based DCT (grayscale)\n"
        f"-------------------------"
    )
    write_log("results/video/log.txt", log)

    print("✅ Video results saved to results/video/")


# ===============================
# MAIN
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