import random
import matplotlib.pyplot as plt
import time
import string


# Function to perform Run-Length Encoding (RLE) compression
def compress(word):
    compressed = ""
    count = 1

    # Iterate through each character in the word
    for i in range(1, len(word)):
        # If the current character is the same as the previous one, increment the count
        if word[i] == word[i - 1]:
            count += 1
        else:
            # Append the character and its count to the compressed string
            compressed += word[i - 1] + str(count)
            count = 1
    # Append the last character and its count to the compressed string
    compressed += word[-1] + str(count)

    return compressed


def calculate_compression_ratio(original, root):
    compression_ratio = []
    # print(len(original))
    # print(len(root))
    for i in range(len(original)):
        original_size = len(original[i])
        compressed_size = len(root[i])
        ratio = compressed_size / original_size
        compression_ratio.append(ratio)
    return compression_ratio


def calculate_complex_area():
    xplotvalues = [10, 50, 100, 500, 1000]
    time_values = [[] for _ in range(len(xplotvalues))]
    compression_ratios = []

    for _ in range(1000):
        root = []
        words = [''.join(random.choices(string.ascii_letters, k=length)) for length in xplotvalues]
        compressed_times = []

        for word in words:
            start_time = time.perf_counter_ns()
            root.append(compress(word))
            compressed_times.append(time.perf_counter_ns() - start_time)

        for i in range(len(xplotvalues)):
            time_values[i].append(compressed_times[i])
        plt.plot(xplotvalues, compressed_times, color="k", marker='o', label='Complex Area')

        compression_ratios.append(calculate_compression_ratio(words, root))


    plot_mean_values = [sum(times) / 1000 for times in time_values]
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