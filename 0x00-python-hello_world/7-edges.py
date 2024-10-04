#!/usr/bin/python3
word = "Holberton"
word_first_3 = word[:3]  # Slices the first 3 letters
word_last_2 = word[-2:]  # Slices the last 2 letters
middle_word = word[1:-1]  # Slices the word, excluding the first and last letters
print("First 3 letters: {}".format(word_first_3))  # Prints the first 3 letters
print("Last 2 letters: {}".format(word_last_2))  # Prints the last 2 letters
print("Middle word: {}".format(middle_word))  # Prints the middle part of the word
