import heapq
from collections import Counter
from utils_progress import progress


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_tree(text):
    heap = [Node(c, f) for c, f in Counter(text).items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        parent = Node(None, a.freq + b.freq)
        parent.left, parent.right = a, b
        heapq.heappush(heap, parent)

    return heap[0]


def build_codes(node, prefix="", table=None):
    if table is None:
        table = {}
    if node.char is not None:
        table[node.char] = prefix
    else:
        build_codes(node.left, prefix + "0", table)
        build_codes(node.right, prefix + "1", table)
    return table


def huffman_encode(text):
    tree = build_tree(text)
    codes = build_codes(tree)

    encoded = ""
    for ch in progress(text, "Huffman Encoding", "char"):
        encoded += codes[ch]

    return encoded, tree


def huffman_decode(encoded, tree):
    decoded = ""
    node = tree

    for bit in progress(encoded, "Huffman Decoding", "bit"):
        node = node.left if bit == "0" else node.right
        if node.char is not None:
            decoded += node.char
            node = tree

    return decoded