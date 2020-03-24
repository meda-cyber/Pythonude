import random
word_file = "word_text.txt"
word_list = []

with open(word_file) as words:
    for line in words:
        # removing white space in btn
        word = line.strip().lower()
        # it will not include word too long or short
        if 3 < len(word) < 8:
            word_list.append(word)

# generating password by creating a function


def generating_password():
    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)


print(generating_password())
