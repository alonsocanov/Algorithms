from operator import inv
import unittest

from pandas import array
from algorithms import *
from arrays import *
from matrix import *
from strings import *
from binary_search import *
from linked_lists import Node, LinkedList
from trees import TreeNode
from hash import *
from stack import *
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

    def test_split_array_largest_sum(self):
        print('\nSplit array into largest sum')
        array = [7, 2, 5, 10, 8]
        split = 3
        result = split_array_largest_sum(array, split)
        print('For the array:', array)
        print('The largest sum is:', result)

    def test_binary_search_v2(self):
        print("\nBinary search in a sorted list")
        array = [1, 3, 5, 7, 8, 10, 25]
        value = 8
        print("Array:", array)
        print("Search for value:", value)
        exists = binary_search_v2(array, value)
        print("The index is:", exists)

    def test_linked_list(self):
        print("\nLinked list tests")
        nodes = []
        for i in range(6):
            nodes += [i]
        linked_list = LinkedList()
        for node in nodes:
            linked_list.append(node)
        print("Linked List:", linked_list)
        linked_list.reorder_list()
        print("Reordered linked List:", linked_list)

    def test_linked_list_intersection(self):
        print("\nLinked list Intersection")
        nodes = []
        for i in range(6):
            nodes += [i]
        linked_list_1 = LinkedList()
        for node in nodes:
            linked_list_1.append(node)
        print("Linked List 1:", linked_list_1)
        nodes = []
        for i in range(3, 6):
            nodes += [i]
        linked_list_2 = LinkedList()
        linked_list_2.append(9)
        for node in nodes:
            linked_list_2.append(node)
        print("Linked List 2:", linked_list_2)
        inter = linked_list_1.intersection(linked_list_2)
        print("Intersection Node:", inter)

    def test_tree(self):
        print("\nTest Tree")
        tree = TreeNode()
        tree.insert(10)
        tree.insert(40)
        tree.insert(5)
        tree.insert(20)
        tree.insert(4)
        print('The tree is:', tree)
        inv_tree = tree.invert(tree)
        print('The tree inverted is:', inv_tree)

    def test_two_sum(self):
        print("\nTest Two sum of a target in a array")
        array = [2, 3, 4, 5, 6, 7]
        print('The array is:', array)
        target = 11
        print('The target:', target)
        idx_1, idx_2 = two_sum(array, target)
        print('The two indexes for the target is:', idx_1, ',', idx_2)

    def test_valid_parenthesis(self):
        print('\nVerify valid parenthesis')
        string = "()((()))[][[]]"
        print("For the string:", string)
        print("The string is valid, ", valid_parenthesis(string))


if __name__ == '__main__':
    algorithms = TestAlgorithms()
    algorithms.test_array_value()
    algorithms.test_reverse_int()
    algorithms.test_bit_swap()
    algorithms.test_sum_exist()
    algorithms.test_reverse_order()
    algorithms.test_mayority_element()
    algorithms.test_max_product()
    algorithms.test_num_bits_1()
    algorithms.test_parity_bit()
    algorithms.test_first_non_repeating()
    # Arrays
    algorithms.test_array_swap()
    algorithms.test_array_merging()
    algorithms.test_binary_search()
    algorithms.test_quicksort()
    algorithms.test_find_duplicates()
    algorithms.test_remove_duplicates()
    algorithms.test_list_intersection()
    algorithms.test_missing_val()
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
    # Binary search
    algorithms.test_split_array_largest_sum()
    algorithms.test_binary_search_v2()
    # Linked List
    algorithms.test_linked_list()
    algorithms.test_linked_list_intersection()
    # Trees
    algorithms.test_tree()
    # Hash
    algorithms.test_two_sum()
    # stacks
    algorithms.test_valid_parenthesis()
