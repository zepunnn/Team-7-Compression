import heapq
from collections import Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_encode(text):
    freq = Counter(text)
    heap = [Node(c, f) for c, f in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        parent = Node(None, a.freq + b.freq)
        parent.left, parent.right = a, b
        heapq.heappush(heap, parent)

    tree = heap[0]
    codes = {}

    def build(node, code=""):
        if node.char:
            codes[node.char] = code
            return
        build(node.left, code + "0")
        build(node.right, code + "1")

    build(tree)
    encoded = "".join(codes[c] for c in text)
    return encoded, tree

def huffman_decode(encoded, tree):
    out, node = [], tree
    for bit in encoded:
        node = node.left if bit == "0" else node.right
        if node.char:
            out.append(node.char)
            node = tree
    return "".join(out)