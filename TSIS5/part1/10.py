from collections import Counter

def word_frequency(file_name):
        with open(file_name) as f:
                return Counter(f.read().split())

print("Number of words in the file: " + str(word_frequency("test.txt")))