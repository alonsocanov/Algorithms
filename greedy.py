def jump_game(array: list[int]) -> bool:
    '''
    Given an array of non-negative integers nums, you are initially positioned at the
    first index of the array.
    Each element in the array represents your maximum jump length at that
    position.
    Determine if you are able to reach the last index.
    '''
    # geady method
    goal = len(array) - 1
    for i in range(goal, -1, -1):
        if i + array[i] >= goal:
            goal = i

    if goal == 0:
        return True
    else:
        return False


def maximum_sum_of_subarray(array: list[int]):
    # sliding window
    max_sub = array[0]
    curr_sum = 0
    for n in array:
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += n
        max_sub = max(max_sub, curr_sum)
    return max_sub


def can_complete_circuit(gas: list(int), cost: list(int)) -> int:
    if sum(gas) < sum(cost):
        return -1

    total = 0
    start = 0
    for i in range(len(gas)):
        total += (gas[i] - cost[i])
        if total < 0:
            total = 0
            start = 1 + i
    return start


if __name__ == '__main__':
    print("\nJumping Game")
    array = [1, 2, 0, 5, 6]
    print("Array:", array)
    print("Can get to the end:", jump_game(array))
