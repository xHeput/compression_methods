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



# Function to calculate the compression ratio
# def calculate_compression_ratio(original, compressed):
#     compression_ratio = []
#     for values in enumerate(original):
#         original_size = len(values[1])
#         compressed_size = len(compressed[0])
#         compression_ratio.append(compressed_size / original_size)

#     return compression_ratio
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
            table_compression.append(compress(values))
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



