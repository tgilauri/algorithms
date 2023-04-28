from collections import defaultdict


def dict_from_string(s):
    d = defaultdict(int)
    for c in s:
        d[c] += 1
    return d


def are_anagrams(a, b):
    return dict_from_string(a) == dict_from_string(b)


input_file = open('./input.txt', 'r')
word_a, word_b = [line.strip() for line in input_file]
input_file.close()

result = "1" if are_anagrams(word_a, word_b) else "0"

output_file = open('./output.txt', 'w')
output_file.write(result)
output_file.close()

