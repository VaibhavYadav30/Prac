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