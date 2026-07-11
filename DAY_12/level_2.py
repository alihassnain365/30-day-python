# Write a function list_of_hexa_colors which returns any number
# of hexadecimal colors in an array (six hexadecimal numbers written after #. 
# Hexadecimal numeral system is made out of 16 symbols,
#  0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
import random
import string

def list_of_hex(number_of_colors: int):
    list_of_hex_colors = list()
    for i in range(0,number_of_colors):
        list_of_hex_colors.append('#' + ''.join(random.choices(string.ascii_lowercase[:6] + string.digits, k=6)))

    return list_of_hex_colors
print(f"Hex colors are {list_of_hex(4)}")  