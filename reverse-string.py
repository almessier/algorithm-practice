# prompt user for string
# iterate through characters
# add the characters to a new string in reverse order
# print reversed word


word = input('Enter word')


def reverse_word(word):
    reversed_word = ''
    for letter in word:
        reversed_word = letter + reversed_word
    return reversed_word


reversed_word = reverse_word(word)
print(reversed_word)
