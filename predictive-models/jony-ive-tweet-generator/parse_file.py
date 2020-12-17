from string import printable


letters = {*printable[:36], *"-'%"}


def clean(word):
    word = word.lower()
    clean_word = ''
    for letter in word:
        if letter in letters:
            clean_word += letter
    if clean_word == 'i':
        return 'I'
    return clean_word


def parse(file_name):
    with open(file_name, 'r') as f:
        content = f.read()

    words = [clean(word) for line in content.splitlines()
             for word in line.split(' ')]

    return words
