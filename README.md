# 📦 Coding and Compression Final Project

## Overview

This project was developed as part of the **Coding and Compression** course. The objective of this assignment is to **implement, evaluate, and analyze data compression techniques** applied to **text, image, and video data**.

The project emphasizes **algorithmic correctness, performance evaluation, and trade-off analysis** between compression efficiency, data quality, and computational cost.  
All implementations are written in **pure Python** for educational purposes.

---

## Objectives

- Implement data compression algorithms for different data types
- Analyze compression performance using quantitative metrics
- Compare efficiency, quality, and computational cost
- Demonstrate practical applications of coding and compression theory
- Provide reproducible experimental results and analysis

---

## Compression Themes & Implemented Methods

### 📄 Text Compression (Lossless)
- **Huffman Coding** (Entropy-based compression)
- **LZW (Lempel–Ziv–Welch)** (Dictionary-based compression)

Both methods support **encoding and decoding** to ensure **lossless reconstruction** of the original text.  
Text input supports **`.txt` and `.epub`** formats.

---

### 🖼️ Image Compression (Lossy)
- **Block-based DCT (Discrete Cosine Transform)**

Images are converted to grayscale and compressed using **8×8 DCT blocks**, following the basic principle of JPEG compression.  
Reconstructed images are evaluated to analyze quality degradation.

---

### 🎥 Video Compression (Lossy, Frame-Based)
- **Frame-level DCT Compression**

Videos are processed frame-by-frame:
- Each frame is converted to grayscale
- Block-based DCT is applied
- Optional frame skipping is used to reduce computational cost

This approach focuses on **spatial redundancy reduction** without motion compensation.

---

## Evaluation Metrics

### Text Compression
- Source Entropy
- Compression Ratio
- File Size Before & After Compression
- Encoding Time
- Decoding Time
- Trade-off between compression efficiency and computational cost

---

### Image Compression
- PSNR (Peak Signal-to-Noise Ratio)
- Compression Ratio
- Visual Artifacts (blocking effects)
- Trade-off between image quality and compression efficiency

---

### Video Compression
- Compression Ratio
- Average PSNR across frames
- Estimated Bit Rate
- Final Compressed Data Size
- Trade-off between quality, efficiency, and processing time

All experimental results and analyses are automatically saved in the `results/` directory.

---

## Project Structure

```
Team-7-Compression/
│
├── LICENSE
├── README.md
├── utils.py
├── utils_epub.py
├── utils_text.py
├── utils_result.py
├── main.py
│
├── text/
│   ├── huffman.py
│   ├── lzw.py
│
├── image/
│   ├── dct_image.py
│
├── video/
│   ├── video_compression.py
│
├── dataset/
│   ├── pg11-images-3.epub
│   ├── pg2701-images-3.epub
│   ├── pg77546-images-3.epub
│   ├── image1.jpg
│   ├── image2.jpg
│   ├── image3.jpg
│   ├── kodim01.png
│   ├── kodim02.png
│   ├── kodim16.png
│   ├── kodim19.png
│   ├── kodim21.png
│   ├── kodim22.png
│   ├── kodim23.png
│   ├── berubah.mp4
│   ├── malumalu.mp4
│   └── kachuusha.mp4
```

---

## Evaluation Metrics

The performance of each compression method is evaluated using:

* **Compression Ratio**
* **Source Entropy**
* **Encoding Time**
* **Decoding Time**
* **File Size Before and After Compression**

All evaluations are performed on text-based datasets.

---

## How to Run

1. Clone the repository or download the source code
2. Place text files inside the `dataset/` directory
3. Run the main program:

   ```bash
   python main.py
   ```
4. Select the compression theme:
 - Text Compression
 - Image Compression
 - Video Compression
5. View results and analysis inside the results/ directory
Progress bars are displayed during execution to visualize long-running compression processes.

---

## Notes & Limitations

* This project prioritizes clarity and correctness over execution speed
* Implementations are not optimized for real-time performance
* Video experiments are conducted on short clips due to computational constraints
* No industrial compression codecs (e.g., H.264, JPEG libraries) are used

---

## Contributors

This project was developed collaboratively by a group of four students:

* **Fakhri Muhammad Al Hisyam** – Compression algorithm implementation & system integration
* **Contributor 2** – Data preparation & testing
* **Contributor 3** – Performance evaluation & result analysis
* **Contributor 4** – Documentation & validation

*(Contributor roles may overlap as part of collaborative development.)*

---

## License

This project is created for academic purposes only.
An open-source license (e.g., MIT License) may be added if the repository is made public.

© 2025 Coding and Compression Final Project
