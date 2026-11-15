import heapq

class Node:
    def __init__(self, freq, char):
        self.freq = freq
        self.char = char
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def print_codes(root, code=""):
    if root.left is None and root.right is None:
        print(root.char, ":", code)
        return

    print_codes(root.left, code + "0")
    print_codes(root.right, code + "1")


chars = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [5, 9, 12, 13, 16, 45]

heap = []

for i in range(len(chars)):
    heapq.heappush(heap, Node(freq[i], chars[i]))

while len(heap) > 1:
    left = heapq.heappop(heap)
    right = heapq.heappop(heap)

    new = Node(left.freq + right.freq, "")

    new.left = left
    new.right = right

    heapq.heappush(heap, new)

print("Huffman Codes:")
print_codes(heap[0])





"""
Theory & Code Overview:
This script implements Huffman Coding, a greedy lossless data compression algorithm that assigns
variable-length binary codes to characters based on their frequencies—giving shorter codes to
more frequent characters to minimize overall bit length. It defines a custom 'Node' class with
a less-than (__lt__) comparator so Python's 'heapq' module can maintain a min-heap prioritized
by frequency. After pushing all initial character-frequency pairs into the heap, a 'while' loop
repeatedly extracts the two lowest-frequency nodes, merges them into a new internal parent node
with their combined frequency, and pushes it back until a single root node remains. Finally, the
recursive 'print_codes' function traverses the resulting binary tree from the root to each leaf
node—appending '0' for left branches and '1' for right branches—to generate and display the
prefix-free Huffman codes in O(n log n) time complexity and O(n) space complexity.
"""