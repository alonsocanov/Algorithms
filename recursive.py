def all_possible_sum(array, target):
    result = []

    def dfs(i, curr, total):
        if total == target:
            result.append(curr.copy())
            return
        if total > target or i >= len(array):
            return
        curr.append(array[i])
        dfs(i, curr, total + array[i])
        curr.pop()
        dfs(i + 1, curr, total)
    dfs(0, [], 0)
    return result


if __name__ == '__main__':
    print("\nFind all possible sums to target")
    candidates = [2, 3, 6, 7]
    print("The candidates are:", candidates)
    target = 7
    print("The target is:", target)
    res = all_possible_sum(candidates, target)
    print("All posible sums:", res)
