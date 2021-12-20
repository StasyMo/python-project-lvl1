def capitalize(text):
    first_char, *rest_chars = text
    rest_substring = ''.join(rest_chars)
    return f'{first_char.upper()}{rest_substring}'
#
# import sys
# print(sys.path)