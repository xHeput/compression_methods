from queue import PriorityQueue
from tabulate import tabulate


class Node:
    value = 0
    right = None
    left = None
    character = ""

    # Check if the node is a leaf node (contains a character)
    def isLeaf(self):
        return self.character != ""

    # Initialize a node with a value and character
    def __init__(self, val, ch):
        self.value = val
        self.character = ch

    # Define the less than comparison for nodes
    def __lt__(self, other):
        if self.value != other.value:
            return self.value > other.value
        if not self.isLeaf() and other.isLeaf():
            return True
        if self.isLeaf() and not other.isLeaf():
            return False
        if self.isLeaf() and other.isLeaf():
            return ord(self.character[0]) > ord(other.character[0])
        return True


def createTree(text):
    occurences = {}
    # Count the occurrences of each character in the text
    for c in text:
        if occurences.__contains__(c):
            occurences[c] += 1
        else:
            occurences[c] = 1

    nodes = PriorityQueue()
    # Create leaf nodes based on characters and their occurrences
    for c in occurences.keys():
        node = Node(occurences[c], c)
        nodes.put(node)
    root_node = None
    # Build the Huffman tree by combining nodes
    while nodes.qsize() > 1:
        n1 = nodes.get()
        n2 = nodes.get()

        parent = Node(n1.value + n2.value, "")
        root_node = parent
        parent.left = n1
        parent.right = n2
        nodes.put(parent)
    return root_node


def encodeValues(n, str_, txt, table_):
    if n is None:
        return txt
    if n.isLeaf():
        # Encode the values and populate the table with symbols, frequencies, and Huffman codes
        table_.append([n.character, n.value, str_])
        txt = txt.replace(n.character, str_)
    txt = encodeValues(n.left, str_ + "0", txt, table_)
    txt = encodeValues(n.right, str_ + "1", txt, table_)
    return txt


def decode(root, text):
    decoded = ""
    curr_node = root
    for char in text:
        # Decode the text based on the Huffman tree
        if char == '0':
            if curr_node.left.isLeaf():
                decoded += curr_node.left.character
                curr_node = root
            else:
                curr_node = curr_node.left
        else:
            if curr_node.right.isLeaf():
                decoded += curr_node.right.character
                curr_node = root
            else:
                curr_node = curr_node.right
    return decoded


word = input("Enter the text to encode:").rstrip()
root_node = createTree(word)
table = []
word = encodeValues(root_node, "", word, table)
print("Here is the encoding table:")
print(tabulate(table, headers=["Symbols", "Frequencies", "Huffman Codes"]))
print("Encoded text: " + word)

bit_count_before = len(word) * 8
bit_count_after = len(word)
compression_ratio = (bit_count_before - bit_count_after) / bit_count_before * 100

word = decode(root_node, word)
print("Decoded text: " + word)
print("Bit count before compression: " + str(bit_count_before))
print("Bit count after compression: " + str(bit_count_after))
print("Compression ratio: " + str(compression_ratio) + "%")
