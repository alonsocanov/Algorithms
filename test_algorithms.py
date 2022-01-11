import unittest
import numpy as np
from algorithms import *


class TestAlgorithms(unittest.TestCase):

    def test_array_value(self):
        print('\nIf str is value')
        my_array = "I am 5 years old"
        print(my_array, ":", isValue(my_array))
        my_array = "5124"
        print(my_array, ":", isValue(my_array))
        my_array = ""
        print(my_array, ":", isValue(my_array))
        my_array = "12.5"
        print(my_array, ":", isValue(my_array))
        my_array = "12..5"
        print(my_array, ":", isValue(my_array))

    def test_snake_sring(self):
        print('\nCreate a snake string')
        phrase = "Hello World!"
        print(phrase)
        snake = snakeSring(phrase)
        print(snake)
        phrase = [1, 2, 3, 4, 5]

    def test_roman(self):
        print('\nConvert from roman to integer')
        roman_val = "XCVII"
        decimal_val = romanToInteger(roman_val)
        print("Roman Number: ", roman_val)
        print("Decimal Number: ", decimal_val)

    def test_reverse_int(self):
        print('\nReverse an integer')
        val = 1019
        print(val)
        rev = reverseInt(val)
        print(rev)

    def test_pascal(self):
        print('\nPascal triangle')
        n = 5
        print(pascalTriangle(n))

    def test_palindrome(self):
        print('\nCheck if string is palindrome')
        my_array = "anita lava la tina"
        print(my_array)
        print(isPalindrome(my_array))

    def test_bit_swap(self):
        print('\nCheck bit parity')
        val = 11
        print(val)
        value_swap = swapBits(val, 1, 2)
        print(value_swap)

    def test_counting_bits(self):
        print('\nBit counting')
        val = 100
        print(val)
        nb_bits = countBits(val)
        print(nb_bits)

    def test_missing_val(self):
        print('\nFind missing value')
        array = [2, 3, 1, 6, 5, 4, 8]
        print(array)
        x = findMissingValue(array)
        print('Missing Value:', x)

    def test_sum_exist(self):
        print(
            '\nDetermine if the sum of two values in an array is equal to the given value')
        value = 15
        array = [1, 4, 6, 8, 2, 5]
        print('Array:', array)
        print('Value:', value)
        print('The sum exists:', sumExists(array, value))
        value = 11
        print('Value:', value)
        print('The sum exists:', sumExists(array, value))

    def test_reverse_order(self):
        print(
            '\nReverse the order of words in a given sentence')
        string = 'The big brown fox'
        print('Sentence:', string)
        rev_string = reverseWordOrder(string)
        print('Reversed string:', rev_string)

    def test_mayority_element(self):
        print('The mayority element that appears more than floor(n/2) times')

        array = [1, 3, 3, 1, 2, 3, 3]
        print('Array:', array)
        cand = mayorityElement(array)
        print('Mayority Element:', cand)

    def test_max_product(self):
        print('Maximum subarray product')
        array = [2, 3, -2, 4]
        print('Array:', array)
        subarray, product = subarrayMaxProduct(array)
        print('Product:', product)
        print('Subarray:', subarray)


if __name__ == '__main__':
    algorithms = TestAlgorithms()
    algorithms.test_array_value()
    algorithms.test_snake_sring()
    algorithms.test_roman()
    algorithms.test_reverse_int()
    algorithms.test_pascal()
    algorithms.test_palindrome()
    algorithms.test_bit_swap()
    algorithms.test_counting_bits()
    algorithms.test_missing_val()
    algorithms.test_sum_exist()
    algorithms.test_reverse_order()
    algorithms.test_mayority_element()
    algorithms.test_max_product()
