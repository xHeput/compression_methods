from queue import PriorityQueue
import random
import matplotlib.pyplot as plt
import time
import string
from tabulate import tabulate


class Node:
    def __init__(self, val, ch):
        self.value = val
        self.character = ch
        self.right = None
        self.left = None

    def isLeaf(self):
        return self.character != ""

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
    for c in text:
        occurences[c] = occurences.get(c, 0) + 1

    nodes = PriorityQueue()
    for c in occurences.keys():
        node = Node(occurences[c], c)
        nodes.put(node)

    while nodes.qsize() > 1:
        parent = Node(0, "")
        parent.left = nodes.get()
        parent.right = nodes.get()
        parent.value = parent.left.value + parent.right.value
        nodes.put(parent)

    return nodes.get()


def encodeValues(node, code, text, table):
    if node is None:
        return text

    if node.isLeaf():
        table.append([node.character, node.value, code])
        text = text.replace(node.character, code)

    text = encodeValues(node.left, code + "0", text, table)
    text = encodeValues(node.right, code + "1", text, table)

    return text


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


def calculate_complex_area():
    xplotvalues = [10, 50, 100, 500, 1000]
    time_values = [[] for _ in range(len(xplotvalues))]
    compression_ratios = []

    for _ in range(1000):
        words = [''.join(random.choices(string.ascii_letters, k=length)) for length in xplotvalues]
        compressed_times = []

        for word in words:
            start_time = time.perf_counter_ns()
            root = createTree(word)
            compressed_times.append(time.perf_counter_ns() - start_time)

        for i in range(len(xplotvalues)):
            time_values[i].append(compressed_times[i])
        plt.plot(xplotvalues, compressed_times, color="k", marker='o', label='Complex Area')

        compression_ratios.append(calculate_compression_ratio(words, root))

    plot_mean_values = [sum(times) / 1000 for times in time_values]
    print(len(xplotvalues))
    print(len(plot_mean_values))
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


calculate_complex_area()
