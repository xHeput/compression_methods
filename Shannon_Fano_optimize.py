import random
import matplotlib.pyplot as plt
import time
import string


def shannon_fano(input_str):
    # Liczenie częstości występowania znaków
    freq = {}
    for char in input_str:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    # Sortowanie znaków według częstości
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # Funkcja rekurencyjna do przypisywania 0 i 1 do znaków
    def assign_code(nodes, start, end):
        if start == end:
            return
        for i in range(start, end + 1):
            nodes[i] += '0' if i <= (start + end) / 2 else '1'
        assign_code(nodes, start, (start + end) // 2)
        assign_code(nodes, (start + end) // 2 + 1, end)

    # Inicjalizacja listy kodów
    codes = [''] * len(sorted_freq)

    # Przypisanie kodów do znaków
    assign_code(codes, 0, len(sorted_freq) - 1)

    # Tworzenie słownika z wynikowymi kodami
    result = {}
    for i, item in enumerate(sorted_freq):
        char, _ = item
        result[char] = codes[i]

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
    xplotvalues = [100, 500, 1000]
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