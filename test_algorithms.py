import unittest
import numpy as np
from algorithms import *


class TestAlgorithms(unittest.TestCase):

    # def test_array_value(self):
    #     print('\nIf str is value')
    #     my_array = "I am 5 years old"
    #     print(my_array, ":", isValue(my_array))
    #     my_array = "5124"
    #     print(my_array, ":", isValue(my_array))
    #     my_array = ""
    #     print(my_array, ":", isValue(my_array))
    #     my_array = "12.5"
    #     print(my_array, ":", isValue(my_array))
    #     my_array = "12..5"
    #     print(my_array, ":", isValue(my_array))

    # def test_snake_sring(self):
    #     print('\nCreate a snake string')
    #     phrase = "Hello World!"
    #     print(phrase)
    #     snake = snakeSring(phrase)
    #     print(snake)
    #     phrase = [1, 2, 3, 4, 5]

    # def test_roman(self):
    #     print('\nConvert from roman to integer')
    #     roman_val = "XCVII"
    #     decimal_val = romanToInteger(roman_val)
    #     print("Roman Number: ", roman_val)
    #     print("Decimal Number: ", decimal_val)

    # def test_reverse_int(self):
    #     print('\nReverse an integer')
    #     val = 1019
    #     print(val)
    #     rev = reverseInt(val)
    #     print(rev)

    # def test_pascal(self):
    #     print('\nPascal triangle')
    #     n = 5
    #     print(pascalTriangle(n))

    # def test_palindrome(self):
    #     print('\nCheck if string is palindrome')
    #     my_array = "anita lava la tina"
    #     print(my_array)
    #     print(isPalindrome(my_array))

    # def test_bit_swap(self):
    #     print('\nCheck bit parity')
    #     val = 11
    #     print(val)
    #     value_swap = swapBits(val, 1, 2)
    #     print(value_swap)

    # def test_counting_bits(self):
    #     print('\nBit counting')
    #     val = 100
    #     print(val)
    #     nb_bits = countBits(val)
    #     print(nb_bits)

    def test_missing_val(self):
        print('Find missing value')
        array = [2, 3, 1, 6, 5, 4, 8]
        print(array)
        x = findMissingValue(array)
        print('Missing Value:', x)


if __name__ == '__main__':
    unittest.main()
