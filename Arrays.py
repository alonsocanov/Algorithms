
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
def quicksort(array: list, left: int, right: int):
    '''
    Quisort using recursive method
    '''
    if left >= right:
        left, right = right, left
    pivot = array[int((left + right) / 2)]
    index = partition(array, left, right, pivot)
    quicksort(array, left, index - 1)
    quicksort(array, index, right)


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


def main():
    my_array_1 = [2, 4, 1, 5, 9, 45, 7]
    print(my_array_1)
    my_array_2 = [3, 8, 10, 20, 15]
    print(my_array_2)
    quicksort(my_array_1, 0, len(my_array_1) - 1)
    quicksort(my_array_2, 0, len(my_array_2) - 1)


if __name__ == '__main__':
    main()
