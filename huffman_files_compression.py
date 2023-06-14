import time
from queue import PriorityQueue
import matplotlib.pyplot as plt
from tabulate import tabulate


class Node:
    value = 0
    right = None
    left = None
    character = ""

    def isLeaf(self):
        return self.character != ""

    def __init__(self, val, ch):
        self.value = val
        self.character = ch

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
    occurrences = {}
    for c in text:
        if c in occurrences:
            occurrences[c] += 1
        else:
            occurrences[c] = 1

    nodes = PriorityQueue()
    for c in occurrences.keys():
        node = Node(occurrences[c], c)
        nodes.put(node)
    root_node = None
    while nodes.qsize() > 1:
        n1 = nodes.get()
        n2 = nodes.get()

        parent = Node(n1.value + n2.value, "")
        root_node = parent
        parent.left = n1
        parent.right = n2
        nodes.put(parent)
    return root_node


def encodeValues(n, string, txt):
    if n is None:
        return txt
    if n.isLeaf():
        print(n.character + " : " + string)
        txt = txt.replace(n.character, string)
    txt = encodeValues(n.left, string + "0", txt)
    txt = encodeValues(n.right, string + "1", txt)
    return txt


def decode(root, text):
    decoded = ""
    curr_node = root
    for bit in text:
        if curr_node is None:
            break
        if bit == '0':
            if curr_node.left is None:
                break
            if curr_node.left.isLeaf():
                decoded += curr_node.left.character
                curr_node = root
            else:
                curr_node = curr_node.left
        else:
            if curr_node.right is None:
                break
            if curr_node.right.isLeaf():
                decoded += curr_node.right.character
                curr_node = root
            else:
                curr_node = curr_node.right
    return decoded


def compress_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read().rstrip()

    start_time = time.time()
    root_node = createTree(text)
    encoded_text = encodeValues(root_node, "", text)
    end_time = time.time()

    compression_ratio = (len(encoded_text) / len(text)) * 100
    compression_time = end_time - start_time

    with open(f"{file_path}_compressed.txt", 'w') as file:
        file.write(encoded_text)

    return len(text), len(encoded_text), compression_ratio, compression_time


def decompress_file(file_path):
    compressed_text = ""
    with open(file_path, 'r') as file:
        compressed_text = file.read()

    encoded_text = ""
    for char in compressed_text:
        encoded_text += bin(ord(char))[2:].zfill(8)

    root_node = createTree("")
    decoded_text = decode(root_node, encoded_text)

    return decoded_text, None


def generate_plots(text_lengths,
                   original_sizes,
                   compressed_sizes,
                   compression_ratios,
                   compression_times,
                   decompression_times):
    plt.figure(1)
    plt.plot(text_lengths, original_sizes, label='Original Size')
    plt.plot(text_lengths, compressed_sizes, label='Compressed Size')
    plt.xlabel('Text Length')
    plt.ylabel('Size (in bits)')
    plt.title('Original Size vs Compressed Size')
    plt.legend()

    plt.figure(2)
    plt.plot(text_lengths, compression_times, label='Compression Time')
    plt.plot(text_lengths, decompression_times, label='Decompression Time')
    plt.xlabel('Text Length')
    plt.ylabel('Time (in seconds)')
    plt.title('Compression Time vs Decompression Time')
    plt.legend()

    plt.figure(3)
    plt.plot(text_lengths, compression_ratios)
    plt.xlabel('Text Length')
    plt.ylabel('Compression Ratio (%)')
    plt.title('Compression Ratio')

    plt.show()


def generate_tables(file_paths, text_lengths, symbols, occurrences, codes):
    for i, file_path in enumerate(file_paths):
        table_data = []
        for j in range(len(symbols[i])):
            table_data.append([symbols[i][j], occurrences[i][j], codes[i][j]])

        table = tabulate(table_data, headers=['Symbol', 'Occurrences', 'Huffman Code'], tablefmt='grid')
        with open(f"{file_path}_table.txt", 'w') as file:
            file.write(table)


if __name__ == '__main__':
    file_paths = ['1_wers.txt', '3_wersy.txt', '10_wersow.txt', '25_wersow.txt', '50_wersow.txt']
    text_lengths = []
    original_sizes = []
    compressed_sizes = []
    compression_ratios = []
    compression_times = []
    decompression_times = []
    symbols = []
    occurrences = []
    codes = []

    for file_path in file_paths:
        text_length, compressed_size, compression_ratio, compression_time = compress_file(file_path)
        decoded_text, decompression_time = decompress_file(f"{file_path}_compressed.txt")
        print(f"Original Text Length: {text_length}")
        print(f"Compressed Size: {compressed_size}")
        print(f"Compression Ratio: {compression_ratio}%")
        print(f"Compression Time: {compression_time} seconds")
        print(f"Decompression Time: {decompression_time} seconds")
        print("")

        text_lengths.append(text_length)
        original_sizes.append(text_length * 8)
        compressed_sizes.append(compressed_size)
        compression_ratios.append(compression_ratio)
        compression_times.append(compression_time)
        decompression_times.append(decompression_time)
        symbols.append(list(set(decoded_text)))
        occurrences.append([decoded_text.count(symbol) for symbol in symbols[-1]])
        codes.append([])

        symbol_codes = {}
        code = ""
        for bit in decoded_text:
            code += bit
            if code in symbol_codes.values():
                symbol = list(symbol_codes.keys())[list(symbol_codes.values()).index(code)]
                codes[-1].append(code)
                code = ""

    generate_plots(text_lengths,
                   original_sizes,
                   compressed_sizes,
                   compression_ratios,
                   compression_times,
                   decompression_times)
    generate_tables(file_paths,
                    text_lengths,
                    symbols,
                    occurrences,
                    codes)
