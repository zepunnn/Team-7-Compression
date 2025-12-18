# 📦 Coding and Compression Final Project

## Overview

This project was developed as part of the **Coding and Compression** course. The objective of this assignment is to implement and evaluate several **lossless data compression algorithms** applied to textual documents. The project focuses on practical implementation, performance comparison, and understanding the trade-offs between compression efficiency and computational cost.

The system is implemented using **Python** and supports multiple compression techniques based on entropy coding and dictionary-based methods.

---

## Objectives

* Implement lossless data compression algorithms
* Compare compression performance across different methods
* Analyze compression ratio, entropy, and processing time
* Demonstrate practical applications of coding and compression theory

---

## Implemented Methods

The following compression techniques are implemented in this project:

* **Huffman Coding** (Entropy Coding)
* **LZW (Lempel–Ziv–Welch)** (Dictionary-Based Compression)
* **Shannon–Fano Coding** *(optional / comparative method)*

Each method supports both **encoding** and **decoding** to ensure lossless reconstruction of the original data.

---

## Project Structure

```
compression-project/
│
├── main.py            # Main execution script
├── huffman.py         # Huffman coding implementation
├── lzw.py             # LZW compression implementation
├── shannon_fano.py    # Shannon-Fano coding (optional)
├── utils.py           # Helper functions
├── dataset/           # Text datasets
└── results/           # Compression results and logs
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
4. View the results in the terminal or inside the `results/` folder

---

## Contributors

This project was developed collaboratively by a group of four students:

* **Fakhri Muhammad Al Hisyam** – Compression algorithm implementation & system integration
* **Contributor 2** – Data preparation & testing
* **Contributor 3** – Performance evaluation & result analysis
* **Contributor 4** – Documentation & validation

*(Contributor roles may overlap as part of collaborative development.)*

---

## Notes

* This project is intended for **academic purposes only**.
* All algorithms are implemented from scratch for learning objectives.
* No external compression libraries are used for core implementations.

---

## License

This project is created as part of a university assignment. Licensing is optional and may be added if the repository is made public.

---

© 2025 Coding and Compression Final Project
