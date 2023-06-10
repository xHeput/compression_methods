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


input_str = input("Enter a string to encode: ")
result = shannon_fano(input_str)

print(input_str)

# Print the code for encoding each character
for char in sorted(result.keys()):
    print(char + ': ' + result[char])







