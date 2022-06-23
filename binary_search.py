import math


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


def split_array_largest_sum(array: list, split: int):
    '''
    Given an array which consists of non-negative integers and an integer split you can split the array into split non-empty continious subarrays.
    Minimize the larges sum among these split subarrays
    '''
    def can_split(larges, array, split):
        subarray = 0
        current_sum = 0
        for n in array:
            current_sum += n
            if current_sum > larges:
                subarray += 1
                current_sum = n

        return subarray + 1 <= split

    left, right = min(array), sum(array)
    res = right
    while left <= right:
        mid = (left + right) // 2
        if can_split(mid, array, split):
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    return res


def binary_search_v2(array: list, target: int):
    '''
    Given an array of integers which is sorted in ascending order, and an integer target, write a finction to search target in the array. If the target exists then return its index, otherwhise -1
    '''
    left, right = 0, len(array) - 1
    while left <= right:
        mid = left + ((right - left) // 2)
        if array[mid] > target:
            right = mid - 1
        elif array[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1


def kogo_eating_bananas(piles: list[int], h: int):
    '''
    Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

    Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

    Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

    Return the minimum integer k such that she can eat all the bananas within h hours.
    '''

    l, r = 0, max(piles)
    res = r

    while l <= r:
        k = (l + r) // 2
        hours = 0
        for p in piles:
            hours += math.ceil(p/k)

        if hours <= h:
            res = min(res, k)
            r = k - 1
        else:
            l = k + 1

    return res


def search_rotated(nums: list[int], target: int):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid
        # left portion
        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
    return -1


if __name__ == '__main__':
    print("\nKogo eating bananas")
    piles = [30, 11, 23, 4, 20]
    print("The pile is:", piles)
    h = 5
    print("The guards will return in", h, "hours")
    rate = kogo_eating_bananas(piles, h)
    print("Kogo needs to eat the banaas at a rate of", rate, "bananas per hour")

    print('\nSplit array into largest sum')
    array = [7, 2, 5, 10, 8]
    split = 3
    result = split_array_largest_sum(array, split)
    print('For the array:', array)
    print('The largest sum is:', result)

    print("\nBinary search in a sorted list")
    array = [1, 3, 5, 7, 8, 10, 25]
    value = 8
    print("Array:", array)
    print("Search for value:", value)
    exists = binary_search_v2(array, value)
    print("The index is:", exists)

    print("\nBinary search in a sorted list")
    array = [1, 3, 5, 7, 8, 10, 25]
    value = 8
    print("Array:", array)
    print("Search for value:", value)
    exists = binary_search(array, value)
    print("Value exists:", exists)

    print("\nSearch rotated array")
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print("Array:", nums)
    print("Search for value:", target)
    exists = search_rotated(nums, target)
    print("Value exists:", exists)
