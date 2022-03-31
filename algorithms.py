from unittest import result


def reverse_int(x):
    '''
    reverse an integer
    '''
    res = 0
    remain = abs(x)
    while remain:
        res = res * 10 + remain % 10
        remain //= 10
    return res if x > 0 else -res


def pascal_triangle(n):
    '''
    create pascal triangle with n rows
    '''
    result = [[1] * (i + 1) for i in range(n)]
    for i in range(n):
        for j in range(1, i):
            result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
    return result


def swap_bits(x, i, j):
    '''
    check bit parity
    '''
    res = x
    if (x >> i) & 1 != (x >> j) & 1:
        mask = (1 << i) | (1 << j)
        res ^= mask
    return res


def sum_exists(array, value):
    '''
    given an array of integers and a value, determine if there are any two
    integers in an array whose sum is equal to the given value.
    Return true if the sum exists else return false
    time complexity: O(n)
    memory complexity: O(n)
    '''
    array.sort()
    lower = 0
    upper = len(array) - 1

    while lower < upper:
        if array[lower] + array[upper] == value:
            return True, [array[lower], array[upper]]
        elif array[lower] + array[upper] < value:
            lower += 1
        elif array[lower] + array[upper] > value:
            upper -= 1
        else:
            break
    return False


def reverse_word_order(string: str):
    '''
    Reverse the order of words in a given sentence
    time complexity: O(n)
    memory complexity: O(1)
    '''
    idx_end = 0
    counter = 0
    lenght = len(string)
    while counter < lenght:
        if string[idx_end] == ' ' or idx_end == lenght - 1:
            word = string[:idx_end]
            middle_sentence = string[idx_end + 1: lenght - counter + idx_end]
            end_sentence = string[lenght - counter + idx_end:]
            string = middle_sentence + ' ' + word + ' ' + end_sentence
            idx_end = 0
            counter += 1

        idx_end += 1
        counter += 1

    return string


def mayority_element(array):
    '''
    Given an array or size n, find the mayority element. The mayority element
    that appears more than floor(n/2) times. (The mayority always exists)
    time space: O(n)
    memory complexity: O(1)
    Moore’s Voting Algorithm
    '''
    def find_candidate(array: list):
        maj_index = 0
        count = 1
        for i in range(len(array)):
            if array[maj_index] == array[i]:
                count += 1
            else:
                count -= 1
            if count == 0:
                maj_index = i
                count = 1
        return array[maj_index]

    def is_majority(array: list, cand: int):
        count = 0
        for i in range(len(array)):
            if array[i] == cand:
                count += 1
        if count > len(array)/2:
            return True
        else:
            return False

    # Find the candidate for Majority
    cand = find_candidate(array)

    # Print the candidate if it is Majority
    if is_majority(array, cand) == True:
        return cand
    else:
        return "No Majority Element"


def subarray_max_product(array: list):
    '''
    Find the continious subarray within an array which has the largest product.
    Return an integer corresponding to the maximum product possible
    '''
    subarray = list()
    product = array[0]
    subarray.append(array[0])
    for idx in range(1, len(array)):
        if product * array[idx] > product:
            product *= array[idx]
            subarray.append(array[idx])
        elif product < array[idx]:
            product = array[idx]
            subarray = list()
            subarray.append(array[idx])

    return subarray, product


def count_num_bits_to_1(value: int):
    '''
     Counting number of bits equal to 1 aims to learn bit shifting algorithms
    '''
    count = 0
    while value:
        count += value & 1
        value >>= 1
    return count


def parity_bit_v1(value: int):
    '''
    The parity of a word bit is 1 if the number of 1s in a word is odd, o is the number of 1s in a word is even
    '''
    result = 0
    while value:
        result ^= value & 1
        value >>= 1
    return result


def parity_bit_v2(value: int):
    '''
    The parity of a word bit is 1 if the number of 1s in a word is odd, o is the number of 1s in a word is even
    '''
    pow_2 = [32, 16, 8, 4, 2, 1]
    for i in pow_2:
        value ^= value >> i
    return value & 0x1


def first_non_repeating(string: str):
    '''
        get unique letters in string
    '''
    dic = {}
    unique = []
    for c in string:
        if c not in dic:
            dic[c] = 1
            unique.append(c)
        else:
            dic[c] += 1
    return unique
