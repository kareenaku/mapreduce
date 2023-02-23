import re
from collections import defaultdict

def map_func(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            words = re.findall('\w+', line.lower())
            for word in words:
                yield (word, 1)

def reduce_func(word, counts):
    return word, sum(counts)

def word_count(files):
    word_counts = defaultdict(list)
    for file_path in files:
        for word, count in map_func(file_path):
            word_counts[word].append(count)

    return [reduce_func(word, counts) for word, counts in word_counts.items()]

# # Test the function with example files
# files = ['example1.txt']
# result = word_count(files)
# print(result)