def isValue(array):
    '''
    find if a str in numeric or a decimal
    '''
    if array == "":
        return False
    decimal_flag = 0
    for i in array:
        if i == ".":
            decimal_flag += 1
        if ((i <= "0" or i >= "9") and i != ".") or decimal_flag == 2:
            return False
    return True


def snakeSring(string):
    result = []
    # height of the snake 3
    for i in range(1, len(string), 4):
        result.append(string[i])
    for i in range(0, len(string), 2):
        result.append(string[i])
    for i in range(3, len(string), 4):
        result.append(string[i])
    return ''.join(result)


def romanToInteger(s):
    '''
    convert from roman to integers
    '''
    T = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    s_copy = s[::-1]
    val = 0
    i = 0
    while i < len(s_copy):
        if i < len(s) - 1 and T[s_copy[i]] > T[s_copy[i + 1]]:
            val += T[s_copy[i]] - T[s_copy[i + 1]]
            i += 1
        else:
            val += T[s_copy[i]]
        i += 1
    return val


def reverseInt(x):
    '''
    reverse an integer
    '''
    res = 0
    remain = abs(x)
    while remain:
        res = res * 10 + remain % 10
        remain //= 10
    return res if x > 0 else -res


def pascalTriangle(n):
    '''
    create pascal triangle with n rows
    '''
    result = [[1] * (i + 1) for i in range(n)]
    for i in range(n):
        for j in range(1, i):
            result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
    return result


def isPalindrome(array):
    '''
    check if string is palindrome
    '''
    head = 0
    tail = len(array) - 1
    while head <= int((len(array) - 1) / 2):
        if array[head] == " ":
            head += 1
        if array[tail] == " ":
            tail -= 1
        if array[head] != array[tail]:
            return False
        head += 1
        tail -= 1
    return True


def swapBits(x, i, j):
    '''
    check bit parity
    '''
    res = x
    if (x >> i) & 1 != (x >> j) & 1:
        mask = (1 << i) | (1 << j)
        res ^= mask
    return res


def countBits(x):
    '''
    counting bits
    '''
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits


def findMissingValue(array):
    '''
    Given an array of positive numbers from 1 to n, such that all numbers
    from one to n are present except one number x, find x
    time complexity: O(n)
    '''
    sum_of_elements = sum(array)

    n = len(array) + 1
    actual_sum = (n * (n + 1)) / 2
    return int(actual_sum - sum_of_elements)


def sumExists(array, value):
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


def reverseWordOrder(string):
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

    return string.strip()
