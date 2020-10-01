# Using pprint - pretty printing for printing
from pprint import pprint
sentence = input("Enter a sentence: ")
char_freq = {}
for char in sentence:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1
# pprint with width parameter
# pprint(char_freq, width=2)

# sorting- passing the dictionary(iterable) to return the key,
# value as tuples. Since sorted cant sort tuples, we using lambda
# function to sort based on kv[1] i.e value(freq)
char_freq_sorted = sorted(
    char_freq.items(),
    key=lambda kv: kv[1],
    reverse=True)
pprint(char_freq_sorted[0])
