# Unpacking lists
# numbers = [1, 2, 3, 4, 4, 4, 4]
# first, *others, last = numbers
# print(first, last)
# print(others)

# Looping over list
# letters = ["a", "b", "c"]
# print(letters)

# enumerate returns a tuple(read-only)
# for letter in enumerate(letters):
#     print(letter)
# for index, letter in enumerate(letters):
#     print(index, letter)

# ADD
# letters.append("d")
# letters.insert(0, "&")
# print(letters)

# # Remove
# letters.pop()
# letters.pop(0)
# letters.append("d")
# del letters[0:2]
# letters.clear()
# print(letters)

# print(letters.index("b"))
# if "d" in letters:
#     print(letters.index("d"))

# # Sorting
# numbers = [3, 4, 1, 8, 2, 11]
# print(numbers)
# # numbers.sort()
# # print(numbers)
# # numbers.sort(reverse=True)
# # print(numbers)

# print(sorted(numbers))
# print(sorted(numbers, reverse=True))
# print(numbers)

# Lambda functions- Anonymous functions
# items = [
#     ("Product1", 10),
#     ("Product2", 6),
#     ("Product3", 12),
# ]
# items.sort(key=lambda item: item[1])
# print(items)

# prices = list(map(lambda item: item[1], items))
# list comprehensions
# prices = [item[1] for item in items]
# print(prices)

#filtered = list(filter(lambda item: item[1] >= 10, items))
# list comprehension
# filtered = [item for item in items if item[1] >= 10]
# print(filtered)

# Zip functions
l1 = [1, 2, 4]
l2 = [10, 20, 30]
print(list(zip("abc", l1, l2)))
