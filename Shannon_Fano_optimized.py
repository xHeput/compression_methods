import random
import matplotlib.pyplot as plt
import time
import string


def shannon_fano(input_str):
    # Counting the frequency of characters
    freq = {}
    for char in input_str:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    # Sort characters based on frequency
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # Divide and conquer approach to assign 0's and 1's for characters
    left = 0
    right = len(sorted_freq) - 1
    threshold = 0
    result = {}
    for char in freq.keys():
        result[char] = ''

    for i, item in enumerate(sorted_freq):
        char, f = item
        threshold += f
        if i != right and threshold >= sum([freq[item[0]] for item in sorted_freq[left:i + 1]]) / 2:
            if i - left == 1:
                result[sorted_freq[left][0]] += '1'
            else:
                for j in range(left, i):
                    result[sorted_freq[j][0]] += '1'
            for j in range(i, right + 1):
                result[sorted_freq[j][0]] += '0'
            left = i + 1
            threshold = 0

    # Assign 0's and 1's to characters remaining in the list
    for i in range(left):
        result[sorted_freq[i][0]] += '1'

    return result


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
            root.append(shannon_fano(word))
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