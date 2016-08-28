import base_conversion as bc

# Example 1:
# If we want to convert a number in any base to decimal we use convert_base_to_dec
# In this case we want to convert the hexadecimal number 'F4A' to decimal
chars_base16 = "0123456789ABCDEF"
answer1 = bc.convert_base_to_dec("F4A", chars_base16)
print("F4A in hexadecimal is " + str(answer1) + " in decimal")

# Example 2:
# If we want to convert a decimal number to another base we use convert_dec_to_base
# In this case we want to convert the number 180 to base 5
chars_base5 = "01234"
answer2 = bc.convert_dec_to_base(180, chars_base5)
print("180 in decimal is " + str(answer2) + " in base 5")

# Example 3:
# We want to convert the octal(base 8) number '7245' to binary(base 2)
chars_base8  = "01234567"
chars_base2 = "01"
number_base8 = "7245"
answer3 = bc.convert_base_to_base(number_base8, chars_base8, chars_base2)
print("7245 in base8 is " + str(answer3) + " in binary")
