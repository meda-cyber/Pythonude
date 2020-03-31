from pprint import pprint
sentence = "This is a common interview question"
freq_char = {}
for char in sentence:
    if char not in freq_char:
        freq_char[char] = 1
    else:
        freq_char[char] += 1
# pprint(freq_char, width=1)
# to make easy and nicer we need to use anothe way
print(sorted(freq_char.items(), key=lambda kv: kv[1], reverse=True))
