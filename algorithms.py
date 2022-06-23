

def pascal_triangle(n):
    '''
    create pascal triangle with n rows
    '''
    result = [[1] * (i + 1) for i in range(n)]
    for i in range(n):
        for j in range(1, i):
            result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
    return result


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


def mayority_element(array):
    '''
    Given an array or size n, find the mayority element. The mayority element
    that appears more than floor(n/2) times. (The mayority always exists)
    time space: O(n)
    memory complexity: O(1)
    Moores Voting Algorithm
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


def longest_sub_string(string: str):
    char_set = set()
    l = 0
    res = 0
    for r in range(len(string)):
        while string[r] in char_set:
            char_set.remove(string[l])
            l += 1
            char_set.add(string[r])
            res = max(res, r - l + 1)
    return res


def character_replacement(s: str, k: int) -> int:
    '''
    You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

    Return the length of the longest substring containing the same letter you can get after performing the above operations.
    '''
    res = 0
    count = dict()
    l = 0
    max_f = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        max_f = max(max_f, count[s[r]])
        while (r - l + 1) - max_f > k:
            count[s[l]] -= 1
            l += 1

        res = max(res, r - l + 1)
    return res


if __name__ == '__main__':
    print("\nCharacter replacement")
    string = "AAABAABAABABBAA"
    print("String:", string)
    k = 2
    print("Number of replacements:", k)
    longest = character_replacement(string, k)
    print("Longest string:", longest)
