
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


def search_sugestion(array: list[str], word: str):
    array.sort()
    left, right = 0, len(array) - 1
    res = []

    for i in range(len(word)):
        char = word[i]

        while left <= right and (len(array[left]) < i or array[left][i] != char):
            left += 1

        while left <= right and (len(array[right]) < i or array[right][i] != char):
            rught += 1

        res.append([])
        remander = right - left + 1
        for j in range(min(3, remander)):
            res[-1].append(array[left + j])

    return res


def topKFrequent(nums: list[int], k: int) -> list[int]:
    '''
    Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
    '''
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for num in nums:
        count[num] = 1 + count.get(num, 0)
    for num, c in count.items():
        freq[c].append(num)
    res = []
    for c in range(len(nums), -1, -1):
        if freq[c]:
            res.extend(freq[c])

        if len(res) == k:
            return res


if __name__ == '__main__':
    print("\nSearch sugestions")
    words = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    word = "mouse"
    print("List of words:", words)
    print("search word:", word)
    sugestions = search_sugestion(words, word)
    print("Sugestions:\n", sugestions)

    print("\nKth repeating")
    nums = [1, 1, 1, 2, 2, 3]
    print("My array is:", nums)
    k = 2
    print("Return the k:", k)
    res = topKFrequent(nums, k)
    print("The K repeating is:", res)
