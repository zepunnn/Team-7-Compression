from text.huffman import huffman_encode, huffman_decode
from text.lzw import lzw_encode, lzw_decode
from image.dct_image import compress_image, decompress_image
from video.video_compression import compress_video
from utils import entropy, psnr

# TEMA 1
text = open("dataset/text.txt").read()
encoded, tree = huffman_encode(text)
decoded = huffman_decode(encoded, tree)
print("Text Entropy:", entropy(text))

# TEMA 2
blocks, shape = compress_image("dataset/image.png")
recon = decompress_image(blocks, shape)
print("Image PSNR:", psnr(recon, recon))

# TEMA 3
frames = compress_video("dataset/video.mp4")
print("Video Frames Compressed:", len(frames))