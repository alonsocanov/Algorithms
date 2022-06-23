
import unittest
from algorithms import *
from arrays import *
from matrix import *
from strings import *
from binary_search import *
from hash import *
from stack import *


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

    def test_pascal(self):
        print('\nPascal triangle')
        n = 5
        print(pascal_triangle(n))

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

    def test_first_non_repeating(self):
        print("\nGet non repeating letters from string")
        string = 'aabaacfgfh'
        unique = first_non_repeating(string)
        print("Unique letters:", unique)

    # Arrays
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

    def test_quicksort(self):
        print("\nTesting a quicksorting in a list")
        array = [2, 1, 6, 8, 4, 3, 6]
        print("Original array:", array)
        quicksort(array)
        print("Sorted array:", array)

    def test_find_duplicates(self):
        print("\nFind duplicates in a list")
        array = [2, 4, 5, 6, 2, 3, 9, 7, 6, 1]
        print("The array is:", array)
        duplicates = find_duplicates(array)
        print("The duplicates in the list are:", duplicates)

    def test_remove_duplicates(self):
        print("\nRemove duplicates from list")
        array = [2, 4, 5, 6, 2, 3, 9, 7, 6, 1]
        print("The array is:", array)
        duplicates = remove_duplicates(array)
        print("The new list is:", duplicates)

    def test_list_intersection(self):
        print("\nCheck intersection of two lists")
        array_1 = [2, 4, 5, 6, 2, 3, 9, 7, 6, 1]
        array_2 = [2, 5, 6, 10, 3, 39, 6, 1]
        print("The array_1 is:", array_1)
        print("The array_2 is:", array_2)
        intersections = list_intersection(array_1, array_2)
        print("The intersection are:", intersections)

    def test_best_time_to_buy_stock(self):
        print("\nBest time to sell stock")
        array = [2, 4, 5, 6, 2, 3, 9, 7, 6, 1]
        print("The array is:", array)
        max_profit = best_time_to_buy_stock(array)
        print("The maximum profit is:", max_profit)

    # Matrix

    def test_matrix_transpose(self):
        print("\nTest matrix transpose")
        array = [[1, 2], [3, 4]]
        print("Matrix:", array)
        trans = transpose(array)
        print("Transposed matrix:", trans)

    def test_matrix_flip(self):
        print("\nTest matrix flip")
        array = [[1, 2], [3, 4]]
        print("Matrix:", array)
        flipped = flip(array)
        print("Flipped matrix:", flipped)

    def test_matrix_rotate(self):
        print("\nTest matrix rotate")
        array = [[1, 2], [3, 4]]
        print("Matrix:", array)
        rot = rotate(array)
        print("Flipped matrix:", rot)

    def test_reverse_sentence(self):
        print("\nTest Reverse a sentence")
        string = "Ana likes Bob and Alice"
        print("Original sentence:", string)
        string = reverse_words_in_sentence(string)
        print("Reversed sentence:", string)

    def test_phone_mnemonics(self):
        print("\nTest phone mnemonics")
        string = "2266622026630255544422233"
        print("Phone Mnemonics:", string)
        message = phone_mnemonics(string)
        print("Message:", message)

    def test_palindrome(self):
        print('\nCheck if string is palindrome')
        my_array = "anita lava la tina"
        print(my_array)
        print(is_palindrome(my_array))

    def test_roman(self):
        print('\nConvert from roman to integer')
        roman_val = "LIX"
        decimal_val = roman_to_integer(roman_val)
        print("Roman Number: ", roman_val)
        print("Decimal Number: ", decimal_val)

    def test_ip(self):
        print('\nConvert from roman to integer')
        num = "19216811"
        ip = valid_ip(num)
        print("Number: ", num)
        print("ip address: ", ip)

    def test_snake_sring(self):
        print('\nCreate a snake string')
        phrase = "Hello World!"
        print(phrase)
        snake = snake_sring(phrase)
        print(snake)
        phrase = [1, 2, 3, 4, 5]


if __name__ == '__main__':
    algorithms = TestAlgorithms()
    algorithms.test_array_value()
    algorithms.test_sum_exist()
    algorithms.test_mayority_element()
    algorithms.test_max_product()
    algorithms.test_first_non_repeating()
    # Arrays
    algorithms.test_array_swap()
    algorithms.test_array_merging()
    algorithms.test_quicksort()
    algorithms.test_find_duplicates()
    algorithms.test_remove_duplicates()
    algorithms.test_list_intersection()
    algorithms.test_best_time_to_buy_stock()
    # Matrix
    algorithms.test_matrix_transpose()
    algorithms.test_matrix_flip()
    algorithms.test_matrix_rotate()
    # Strings
    algorithms.test_reverse_sentence()
    algorithms.test_phone_mnemonics()
    algorithms.test_pascal()
    algorithms.test_palindrome()
    algorithms.test_roman()
    algorithms.test_ip()
    algorithms.test_snake_sring()
