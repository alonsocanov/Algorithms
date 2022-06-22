def two_sum(list, target):
    hash = {}
    for idx in range(len(list)):
        complement = target - list[idx]
        if complement in hash:
            return hash[complement], idx
        else:
            hash[list[idx]] = idx
    return -1, -1


if __name__ == '__main__':
    print("\nTest Two sum of a target in a array")
    array = [2, 3, 4, 5, 6, 7]
    print('The array is:', array)
    target = 11
    print('The target:', target)
    idx_1, idx_2 = two_sum(array, target)
    print('The two indexes for the target is:', idx_1, ',', idx_2)
