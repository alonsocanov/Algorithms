
def array_value_swap(array: list, left: int, right: int):
    '''
    Arrat value swap
    '''
    array[left], array[right] = array[right], array[left]


def partition(array, left, right, pivot):
    while left <= right:
        while(array[left] < pivot):
            left += 1
        while array[right] > pivot:
            right -= 1
        if left <= right:
            array_value_swap(array, left, right)
            left += 1
            right -= 1
    return left


# quicksort
def quicksort(array: list):
    '''
    Quisort using recursive method
    '''
    if not array:
        return []
    return quicksort([x for x in array[1:] if x < array[0]]) + array[0:1] + quicksort([x for x in array[1:] if x >= array[0]])


# merging two lists
def merge_arrays(array_1: list, array_2: list):
    '''
    Merge two number sorted arrays
    '''
    res = []
    i = 0
    j = 0
    while i < len(array_1) and j < len(array_2):
        if array_1[i] < array_2[j]:
            res.append(array_1[i])
            i += 1
        else:
            res.append(array_2[j])
            j += 1
    while i < len(array_1):
        res.append(array_1[i])
        i += 1
    while j < len(array_2):
        res.append(array_2[j])
        j += 1
    return res


# binary search
def binary_search(array: list, x):
    ''''
    Binary search in a sorted list
    '''
    left = 0
    right = len(array) - 1
    while (left <= right):
        mid = int((right + left) / 2)
        if array[mid] == x:
            return True
        elif x > array[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return False


def find_duplicates(array: list):
    duplicates, seen = set(), set()
    for element in array:
        if element in seen:
            duplicates.add(element)
        seen.add(element)
    return duplicates


def remove_duplicates(array: list):
    return list(set(array))


def list_intersection(array_1: list, array_2: list):
    res, list2_copy = [], array_2[:]
    for element in array_1:
        if element in list2_copy:
            res.append(element)
            list2_copy.remove(element)
    return res


def find_missing_value(array):
    '''
    Given an array of positive numbers from 1 to n, such that all numbers
    from one to n are present except one number x, find x
    time complexity: O(n)
    '''
    sum_of_elements = sum(array)

    n = len(array) + 1
    actual_sum = (n * (n + 1)) / 2
    return int(actual_sum - sum_of_elements)


def best_time_to_buy_stock(array):
    '''
    Sliding window problem, two poninters to array, geta max profit
    '''

    left_buy, right_sell = 0, 1
    max_profit = 0
    while right_sell < len(array):
        # profitable
        if array[left_buy] < array[right_sell]:
            profit = array[right_sell] - array[left_buy]
            max_profit = max(profit, max_profit)
        else:
            left_buy = right_sell

        right_sell += 1

    return max_profit
