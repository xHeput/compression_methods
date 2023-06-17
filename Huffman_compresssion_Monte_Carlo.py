from queue import PriorityQueue
import random
import matplotlib.pyplot as plt
import time
import string
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
print(tabulate(table, headers=["Symbols", "Frequencies", "Huffman Codes"], tablefmt="grid"))
print("Encoded text: " + word)

bit_count_before = len(word) * 8
bit_count_after = len(word)
compression_ratio = (bit_count_before - bit_count_after) / bit_count_before * 100

word = decode(root_node, word)
print("Decoded text: " + word)
print("Bit count before compression: " + str(bit_count_before))
print("Bit count after compression: " + str(bit_count_after))
print("Compression ratio: " + str(compression_ratio) + "%")


def calculate_compression_ratio(original, root):
    compression_ratio = []
    for i in range(len(original)):
        word = original[i]
        encoded_word = encodeValues(root, "", word, [])
        original_size = len(word) * 8
        compressed_size = len(encoded_word)
        ratio = compressed_size / original_size
        compression_ratio.append(ratio)
    return compression_ratio



# Function to calculate the complex area
def calculate_complex_area():
    # variables
    xplotvalues = [10, 50, 100, 500, 1000]
    time_10 = []
    time_50 = []
    time_100 = []
    time_500 = []
    time_1000 = []
    for _ in range(1000):
        table_compression = []
        compressed_time = []
        # words generator
        words1 = ''.join(random.choices(string.ascii_letters, k=10))
        words2 = ''.join(random.choices(string.ascii_letters, k=50))
        words3 = ''.join(random.choices(string.ascii_letters, k=100))
        words4 = ''.join(random.choices(string.ascii_letters, k=500))
        words5 = ''.join(random.choices(string.ascii_letters, k=1000))
        table_word = [words1, words2, words3, words4, words5]
        # loop for checking the complex area
        for values in table_word:
            start_time = time.perf_counter_ns()
            root = createTree(values)
            table_compression.append(root)
            end_time = time.perf_counter_ns()
            compressed_time.append(end_time - start_time)
        time_10.append(compressed_time[0])
        time_50.append(compressed_time[1])
        time_100.append(compressed_time[2])
        time_500.append(compressed_time[3])
        time_1000.append(compressed_time[4])
        # complex_area
        plt.plot(xplotvalues, compressed_time, color="k", marker='o', label='Complex Area')
        # calculate_compression_ratio
        compression_ratio = calculate_compression_ratio(table_word, root)
        compression_ratios.append(compression_ratio)

    # calc mean
    plot_mean_values = [sum(time_10) / 1000, sum(time_50) / 1000, sum(time_100) / 1000, sum(time_500) / 1000,
                        sum(time_1000) / 1000]
    # plotting chart
    plt.plot(xplotvalues, plot_mean_values, color="r", marker="o")
    plt.xlabel("Word Length")
    plt.ylabel("Time")
    plt.title("Complex Area for Random Words")
    plt.show()
    for compression_ratio in compression_ratios:
        plt.plot(xplotvalues, compression_ratio, marker="o")
    plt.xlabel("Word Length")
    plt.ylabel("Compression Ratio")
    plt.title("Compression Ratio for Random Words")
    plt.show()


# variables
compression_ratios = []

calculate_complex_area()
