from genericpath import exists
import unittest
import numpy as np
from pandas import array
from algorithms import *
from arrays import *
import time


class TestAlgorithms(unittest.TestCase):

    def test_array_value(self):
        print('\nIf str is value')
        my_array = "I am 5 years old"
        print(my_array, ":", is_value(my_array))
        my_array = "5124"
        print(my_array, ":", is_value(my_array))
        my_array = ""
        print(my_array, ":", is_value(my_array))
        my_array = "12.5"
        print(my_array, ":", is_value(my_array))
        my_array = "12..5"
        print(my_array, ":", is_value(my_array))

    def test_snake_sring(self):
        print('\nCreate a snake string')
        phrase = "Hello World!"
        print(phrase)
        snake = snake_sring(phrase)
        print(snake)
        phrase = [1, 2, 3, 4, 5]

    def test_roman(self):
        print('\nConvert from roman to integer')
        roman_val = "XCVII"
        decimal_val = roman_to_integer(roman_val)
        print("Roman Number: ", roman_val)
        print("Decimal Number: ", decimal_val)

    def test_reverse_int(self):
        print('\nReverse an integer')
        val = 1019
        print(val)
        rev = reverse_int(val)
        print(rev)

    def test_pascal(self):
        print('\nPascal triangle')
        n = 5
        print(pascal_triangle(n))

    def test_palindrome(self):
        print('\nCheck if string is palindrome')
        my_array = "anita lava la tina"
        print(my_array)
        print(is_palindrome(my_array))

    def test_bit_swap(self):
        print('\nCheck bit parity')
        val = 11
        print(val)
        value_swap = swap_bits(val, 1, 2)
        print(value_swap)

    def test_missing_val(self):
        print('\nFind missing value')
        array = [2, 3, 1, 6, 5, 4, 8]
        print(array)
        x = find_missing_value(array)
        print('Missing Value:', x)

    def test_sum_exist(self):
        print(
            '\nDetermine if the sum of two values in an array is equal to the given value')
        value = 15
        array = [1, 4, 6, 8, 2, 5]
        print('Array:', array)
        print('Value:', value)
        print('The sum exists:', sum_exists(array, value))
        value = 11
        print('Value:', value)
        print('The sum exists:', sum_exists(array, value))

    def test_reverse_order(self):
        print(
            '\nReverse the order of words in a given sentence')
        string = 'The big brown fox'
        print('Sentence:', string)
        rev_string = reverse_word_order(string)
        print('Reversed string:', rev_string)

    def test_mayority_element(self):
        print('\nThe mayority element that appears more than floor(n/2) times')

        array = [1, 3, 3, 1, 2, 3, 3]
        print('Array:', array)
        cand = mayority_element(array)
        print('Mayority Element:', cand)

    def test_max_product(self):
        print('\nMaximum subarray product')
        array = [2, 3, -2, 4]
        subarray, product = subarray_max_product(array)
        print('Array:', array)
        print('Product:', product)
        print('Subarray:', subarray)

    def test_num_bits_1(self):
        print("\nNumber of bits equal to 1 in integer")
        value = 12
        count = count_num_bits_to_1(value)
        print("Value:", format(value, 'b'))
        print("The number of bits equal to 1 is:", count)

    def test_parity_bit(self):
        print("\nParity bits")
        value = 55500
        t = time.time()
        result = parity_bit_v1(value)
        print("Bit value:", format(value, 'b'))
        print("Parity bit:", result)
        print("Time for parity bit v1:", time.time() - t)
        t = time.time()
        result = parity_bit_v2(value)
        print("Bit value:", format(value, 'b'))
        print("Parity bit:", result)
        print("Time for parity bit v1:", time.time() - t)

    def test_array_swap(self):
        print("\nSwap array")
        array = [1, 2, 3, 5, 6]
        print("Array:", array)
        array_value_swap(array, 2, 3)
        print("Array value swap:", array)

    def test_array_merging(self):
        print("\nMerge two sorted arrays")
        array_1 = [1, 2, 3, 5, 26]
        array_2 = [5, 10, 11, 20]
        print("Array 1:", array_1)
        print("Array 2:", array_2)
        array = merge_arrays(array_1, array_2)
        print("Merged array:", array)

    def test_binary_search(self):
        print("\nBinary search in a sorted list")
        array = [1, 3, 5, 7, 8, 10, 25]
        value = 8
        print("Array:", array)
        print("Search for value:", value)
        exists = binary_search(array, value)
        print("Value exists:", exists)

    def test_quicksort(self):
        print("\nTesting a quicksorting in a list")
        array = [2, 1, 6, 8, 4, 3, 6, -1]
        print("Original array:", array)
        quicksort(array, 0, len(array)-1)
        print("Sorted array:", array)

    def test_first_non_repeating(self):
        print("\nGet non repeating letters from string")
        string = 'aabaacfgfh'
        unique = first_non_repeating(string)
        print("Unique letters:", unique)


if __name__ == '__main__':
    algorithms = TestAlgorithms()
    algorithms.test_array_value()
    algorithms.test_snake_sring()
    algorithms.test_roman()
    algorithms.test_reverse_int()
    algorithms.test_pascal()
    algorithms.test_palindrome()
    algorithms.test_bit_swap()
    algorithms.test_missing_val()
    algorithms.test_sum_exist()
    algorithms.test_reverse_order()
    algorithms.test_mayority_element()
    algorithms.test_max_product()
    algorithms.test_num_bits_1()
    algorithms.test_parity_bit()
    algorithms.test_first_non_repeating()
    # list algorithms
    # algorithms.test_array_swap()
    # algorithms.test_array_merging()
    # algorithms.test_binary_search()
    # algorithms.test_quicksort()
