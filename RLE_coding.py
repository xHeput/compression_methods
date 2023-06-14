import random
import matplotlib.pyplot as plt
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


# Function to generate a random word of given length
def generate_word(length):
    word = ""
    for _ in range(length):
        # Generate a random lowercase letter
        letter = random.choice("abcdefghijklmnopqrstuvwxyz")
        word += letter
    return word

# Function to calculate the compression ratio
def calculate_compression_ratio(original, compressed):
    original_size = len(original)
    compressed_size = len(compressed)
    compression_ratio = compressed_size / original_size
    return compression_ratio

# Generate and compress 1000 random words
word_lengths = []
compression_ratios = []

for _ in range(1000):
    # Generate a random word of length between 5 and 10
    word_length = random.randint(5, 10)
    word = generate_word(word_length)

    # Compress the word using RLE algorithm
    compressed_word = compress(word)

    # Calculate the compression ratio
    compression_ratio = calculate_compression_ratio(word, compressed_word)

    word_lengths.append(word_length)
    compression_ratios.append(compression_ratio)

print(word_lengths)
print(compression_ratios)
# Plot the compression ratios
plt.scatter(word_lengths, compression_ratios)
plt.xlabel("Word Length")
plt.ylabel("Compression Ratio")
plt.title("Compression Ratio for Random Words")
plt.show()

# Main program
def main():
    # Get the word from the user
    word = input("Enter a word: ")

    # Compress the word using RLE algorithm
    compressed_word = compress(word)

    # Print the compressed word
    print("Compressed word:", compressed_word)


# Run the main program
main()
