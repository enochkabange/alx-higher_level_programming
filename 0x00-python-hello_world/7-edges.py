#!/usr/bin/python3
word = "Holberton"
word_first_3 = word[:3]  # First 3 letters (index 0 to 2)
word_last_2 = word[-2:]  # Last 2 letters (index -2 to the end)
middle_word = word[1:-1]  # Middle word (from index 1 to -1, excluding first and last letters)
print("First 3 letters: {}".format(word_first_3))
print("Last 2 letters: {}".format(word_last_2))
print("Middle word: {}".format(middle_word))
