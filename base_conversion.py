# Program for converting numbers to other bases
# Written by Marten Voorberg

import string
import math

def get_index_of_char(string, char):
    for index in range(0, len(string)):
        if string[index] == char:
            return index
    print("ERROR: Character not found in the string")
    return None

def convert_number_to_dec(number, chars):
    res = 0
    base = len(chars)
    length = len(number)
    value_index = length - 1

    for index in range(0, length):
        current_char = number[index]
        value_of_current_char = get_index_of_char(chars, current_char)
        res += base**value_index * value_of_current_char
        value_index -= 1

    return res

def convert_dec_to_base(number, chars):
    base = len(chars)
    result_string = ""

    while number != 0:
        result_string += chars[number % base]
        number = math.floor(number / base)

    result_string = result_string[::-1]
    return result_string

def convert_base_to_base(number, chars1, chars2):
    # First we convert the number to decimal from base1
    # Then we convert to decimal number to base2
    dec = convert_number_to_dec(number, chars1)
    return convert_dec_to_base(dec, chars2)

# Example:
# We want to convert the octal(base 8) number '7245' to binary(base 2)
chars_base8  = "01234567"
chars_base2 = "01"
number_base8 = "7245"
answer = convert_base_to_base(number_base8, chars_base8, chars_base2)
print(answer)
