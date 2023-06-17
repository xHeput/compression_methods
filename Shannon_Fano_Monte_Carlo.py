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
                result[sorted_freq[left][0]] += '0'
            else:
                for j in range(left, i):
                    result[sorted_freq[j][0]] += '0'
            for j in range(i, right + 1):
                result[sorted_freq[j][0]] += '1'
            left = i + 1
            threshold = 0

    # Assign 0's and 1's to characters remaining in the list
    for i in range(left):
        result[sorted_freq[i][0]] += '0'

    return result


# input_str = input("Enter a string to encode: ")
# result = shannon_fano(input_str)
#
# print(input_str)

# Print the code for encoding each character
# for char in sorted(result.keys()):
#     print(char + ': ' + result[char])

def calculate_compression_ratio(original, compressed):
    compression_ratio = []
    for i in range(len(original)):
        original_size = len(original[i])
        compressed_size = len(compressed[i])
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
            table_compression.append(shannon_fano(values))
            end_time = time.perf_counter_ns()
            compressed_time.append(end_time - start_time)
        time_10.append(compressed_time[0])
        time_50.append(compressed_time[1])
        time_100.append(compressed_time[2])
        time_500.append(compressed_time[3])
        time_1000.append(compressed_time[4])
        # complex_area
        plt.plot(xplotvalues, compressed_time, color="k", marker='o')
        # calculate_compression_ratio
        compression_ratio = calculate_compression_ratio(table_word, table_compression)
        compression_ratios.append(compression_ratio)

    # calc mean
    plot_mean_values = [sum(time_10) / 1000, sum(time_50) / 1000, sum(time_100) / 1000, sum(time_500) / 1000,
                        sum(time_1000) / 1000]
    # plotting chart
    plt.plot(xplotvalues, plot_mean_values, color="r", marker="o")
    plt.xlabel("Word Length")
    plt.ylabel("Time")
    plt.title("complex area for Random Words")
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






