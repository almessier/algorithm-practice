# prompt user for string
# iterate through the string
# add the letters to a new string in reverse order
# split the strings into lists and then join them back to strings to remove spaces
# compare the strings
# if string are equal it is a palindrome, if not it is not a palindrome

string = input('Enter a string: ')


def reverse_string(string):
    reversed_string = ''
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string


reversed_string = reverse_string(string)


def compare_strings(string, reversed_string):
    split_string = string.lower().split(' ')
    compressed_string = ''.join(split_string)
    split_reversed_string = reversed_string.lower().split(' ')
    compressed_reversed_string = ''.join(split_reversed_string)
    if compressed_string == compressed_reversed_string:
        print(f'{string} is a palindrome')
    else:
        print(f'{string} is not a palindrome')


compare_strings(string, reversed_string)
