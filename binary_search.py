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
