def two_sum(list, target):
    hash = {}
    for idx in range(len(list)):
        complement = target - list[idx]
        if complement in hash:
            return hash[complement], idx
        else:
            hash[list[idx]] = idx
    return -1, -1
