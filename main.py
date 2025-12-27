import os
import time
import cv2

from utils import entropy, psnr
from utils_epub import read_epub_text
from utils_text import normalize_text
from utils_result import (
    ensure_dir,
    write_log,
    write_analysis,
    timestamp
)

# ===== TEXT =====
from text.huffman import huffman_encode, huffman_decode
from text.lzw import lzw_encode, lzw_decode

# ===== IMAGE =====
from image.dct_image import compress_image, decompress_image

# ===== VIDEO =====
from video.video_compression import (
    compress_video,
    reconstruct_frames,
    calculate_psnr_frames
)

# ======================================================
# TEXT COMPRESSION
# ======================================================
def text_mode():
    path = input("Enter text file path (.txt / .epub): ").strip()
    if not os.path.exists(path):
        print("❌ File not found.")
        return

    ensure_dir("results/text")

    # Load text
    if path.lower().endswith(".epub"):
        text = read_epub_text(path)
    else:
        with open(path, encoding="utf-8", errors="ignore") as f:
            text = f.read()

    original_size = len(text.encode("utf-8"))
    ent = entropy(text)

    text_norm = normalize_text(text)

    # Huffman
    t0 = time.time()
    encoded, tree = huffman_encode(text_norm)
    enc_time = time.time() - t0

    t0 = time.time()
    decoded = huffman_decode(encoded, tree)
    dec_time = time.time() - t0

    compressed_size = max(1, len(encoded) // 8)
    ratio = original_size / compressed_size

    # Save compressed
    with open("results/text/huffman.bin", "w") as f:
        f.write(encoded)

    # LZW (backup / learning)
    lzw_encoded = lzw_encode(text_norm)
    with open("results/text/lzw.txt", "w") as f:
        f.write(" ".join(map(str, lzw_encoded)))

    # Log
    write_log(
        "results/text/log.txt",
        f"[{timestamp()}] Dataset={path} Ratio={ratio:.2f}"
    )

    # Analysis
    analysis = f"""
TEXT COMPRESSION ANALYSIS
Dataset                 : {path}

Source Entropy           : {ent:.4f}
Original File Size       : {original_size} bytes
Compressed File Size     : {compressed_size} bytes
Compression Ratio        : {ratio:.2f}

Encoding Time            : {enc_time:.4f} seconds
Decoding Time            : {dec_time:.4f} seconds

Trade-off Analysis:
Lossless compression preserves text integrity while reducing
file size. Higher compression efficiency increases computational
overhead during encoding and decoding.
"""
    write_analysis("results/text/analysis.txt", analysis.strip())

    print("✅ Text compression & analysis completed.")


# ======================================================
# IMAGE COMPRESSION
# ======================================================
def image_mode():
    path = input("Enter image path (.png / .jpg): ").strip()
    if not os.path.exists(path):
        print("❌ File not found.")
        return

    ensure_dir("results/image")

    original = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    original_size = os.path.getsize(path)

    t0 = time.time()
    blocks, padded_shape, original_shape = compress_image(path)
    reconstructed = decompress_image(blocks, padded_shape, original_shape)
    proc_time = time.time() - t0

    cv2.imwrite("results/image/reconstructed.png", reconstructed)
    compressed_size = os.path.getsize("results/image/reconstructed.png")

    ratio = original_size / compressed_size
    value = psnr(original, reconstructed)

    write_log(
        "results/image/log.txt",
        f"[{timestamp()}] Dataset={path} PSNR={value:.2f}"
    )

    analysis = f"""
IMAGE COMPRESSION ANALYSIS
Dataset                 : {path}

PSNR                     : {value:.2f} dB
Original File Size       : {original_size} bytes
Compressed File Size     : {compressed_size} bytes
Compression Ratio        : {ratio:.2f}

Trade-off Analysis:
Block-based DCT reduces spatial redundancy but may introduce
blocking artifacts, especially in high-frequency regions.

Visual Artifact:
Visible block boundaries may appear after reconstruction.
"""
    write_analysis("results/image/analysis.txt", analysis.strip())

    print("✅ Image compression & analysis completed.")


# ======================================================
# VIDEO COMPRESSION
# ======================================================
def video_mode():
    path = input("Enter video path (.mp4): ").strip()
    if not os.path.exists(path):
        print("❌ File not found.")
        return

    ensure_dir("results/video")

    original_size = os.path.getsize(path)

    t0 = time.time()
    dct_frames, original_frames = compress_video(path)
    reconstructed_frames = reconstruct_frames(dct_frames)
    proc_time = time.time() - t0

    compressed_size = sum(
    sum(block.nbytes for block in blocks)
    for blocks, _ in dct_frames
    )
    ratio = original_size / compressed_size

    avg_psnr = calculate_psnr_frames(original_frames, reconstructed_frames)

    fps = 30
    duration = len(dct_frames) / fps
    bitrate = (compressed_size * 8) / duration

    write_log(
        "results/video/log.txt",
        f"[{timestamp()}] Dataset={path} PSNR={avg_psnr:.2f}"
    )

    analysis = f"""
VIDEO COMPRESSION ANALYSIS
Dataset                 : {path}

Frames Processed         : {len(dct_frames)}
Original File Size       : {original_size} bytes
Compressed File Size     : {compressed_size} bytes
Compression Ratio        : {ratio:.2f}

Average PSNR (Frames)    : {avg_psnr:.2f} dB
Estimated Bit Rate       : {bitrate:.2f} bps

Trade-off Analysis:
Frame-based transform compression removes spatial redundancy
but lacks temporal motion compensation, resulting in lower
efficiency compared to modern video codecs.
"""
    write_analysis("results/video/analysis.txt", analysis.strip())

    print("✅ Video compression & analysis completed.")


# ======================================================
# MAIN MENU
# ======================================================
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