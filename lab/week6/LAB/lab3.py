#각 문자 횟수 세기 (p. 472)

import os
current_dir = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(current_dir, "words.txt")
f = open(filepath, "r", encoding="utf-8")

word_dict = {}

for line in f:
    word = line.strip("\n")
    for letter in word:
        if letter in word_dict:
            word_dict[letter] += 1
        else:
            word_dict.update({letter:1})

print(word_dict)
