
def valid_parenthesis(string: str) -> bool:
    close_open = {')': '(', '}': '{', ']': '['}
    stack = []
    for char in string:
        if char in close_open:
            if stack and stack[-1] == close_open[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    if not stack:
        return True
    else:
        return False


def generate_parenthensis(n: int) -> list:
    '''
    Given n pairs of parentheses, write a function to generate all combinations of well-formed
    parentheses
    '''
    stack = []
    res = []

    def back_track(open_n, closed_n):
        if open_n == closed_n == n:
            res.append("".join(stack))
            return

        if open_n < n:
            stack.append("(")
            back_track(open_n + 1, closed_n)
            stack.pop()

        if closed_n < open_n:
            stack.append(")")
            back_track(open_n, closed_n + 1)
            stack.pop()
    back_track(0, 0)
    return res


def simplify_path(path: str) -> str:
    stack = []
    cur = ""
    for char in path + "/":
        if char == "/":
            if cur == "..":
                if stack:
                    stack.pop()
            elif cur != "" and cur != ".":
                stack.append(cur)
            cur = ""
        else:
            cur += char

    return "/" + "/".join(stack)


def largest_rectangle_of_histogram(histogram: list) -> int:
    '''
    Given n nonnegative integers representing the histogram's bar height
    where the width of each bar is 1. find the area of largest rectangle in the
    histogram
    '''
    stack = []
    max_area = 0
    for i, h in enumerate(histogram):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            max_area = max(max_area, height * (i - index))
            start = index
        stack.append((start, h))

    for i, h in stack:
        max_area = max(max_area, h * (len(histogram) - i))
    return max_area


def daily_temperatures(temperatures: list[int]) -> list[int]:
    '''
    Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
    '''
    res = [0] * len(temperatures)
    stack = []
    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            temp, ind = stack.pop()
            res[ind] = i - ind
        stack.append([t, i])
    return res


def evalRPN(tokens: list[str]) -> int:
    '''
    Polish notation
    '''
    my_stack = []
    for val in tokens:
        if val == '+':
            my_stack.append(my_stack.pop() + my_stack.pop())
        elif val == '-':
            first = my_stack.pop()
            second = my_stack.pop()
            my_stack.append(second - first)
        elif val == '*':
            my_stack.append(my_stack.pop() * my_stack.pop())
        elif val == '/':
            first = my_stack.pop()
            second = my_stack.pop()
            my_stack.append(int(second / first))
        else:
            my_stack.append(int(val))
    return my_stack[0]


def car_fleet(target: int, position: list[int], speed: list[int]) -> int:
    '''
    There are n cars going to the same destination along a one-lane road. The destination is target miles away.

    You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

    A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).

    A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

    If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

    Return the number of car fleets that will arrive at the destination.
    '''
    pairs = [[p, s] for p, s in zip(position, speed)]
    stack = []
    for p, s in sorted(pairs)[::-1]:
        stack.append((target - p) / s)
        if len(stack) > 1 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)


def asteroidCollision(asteroids: list[int]) -> list[int]:

    stack = []
    for asteroid in asteroids:

        while stack and asteroid < 0 < stack[-1]:

            if stack[-1] < -asteroid:
                stack.pop()
                continue
            elif stack[-1] == -asteroid:
                stack.pop()
            break
        else:
            stack.append(asteroid)
    return stack


def maxSumMinProduct(nums: list[int]) -> int:
    sum_array = [0]
    for n in nums:
        sum_array.append(sum_array[-1] + n)
    res = 0
    stack = []  # [idx, val]
    for i, n in enumerate(nums):
        new_start = i
        while stack and stack[-1][1] > n:
            start, val = stack.pop()
            total = sum_array[i] - sum_array[start]
            res = max(res, val*total)
            new_start = start
        stack.append((new_start, n))

    for start, val in stack:
        total = sum_array[len(nums)] - sum_array[start]
        res = max(res, val * total)
    return res % (10**9 + 7)


def removeKAdjecent(string: str, k: int):
    stack = []
    for c in string:
        if stack and stack[-1][0] == c:
            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append([c, 1])

    res = ""
    for c, i in stack:
        res += (c * i)
    return res


if __name__ == '__main__':
    print('\nVerify valid parenthesis')
    string = "()((()))[][[]]"
    print("For the string:", string)
    is_valid = valid_parenthesis(string)
    print("The string is valid, ", is_valid)

    print('\nGenerate valid parenthesis')
    n = 3
    print("For n ==", n)
    parenthesis = generate_parenthensis(n)
    print("The paretnthesis are:", parenthesis)

    print('\nSimplify path')
    string = "/alonso/villa/../cano/./tests"
    print("For the path:", string)
    path = simplify_path(string)
    print("The simplified path is:", path)

    print('\nLargest rectangle in histogram')
    array = [2, 1, 5, 6, 2, 3]
    print("For the histogram:", array)
    max_area = largest_rectangle_of_histogram(array)
    print("The max area is:", max_area)

    print('\nNumber of days you have to wait after to for the temperature to rise')
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print('Daily temeratures:', temperatures)
    waiting_time = daily_temperatures(temperatures)
    print("Waiting time:", waiting_time)

    print("\nEvaluate polish notation")
    notation = ["10", "6", "9", "3", "+", "-11",
                "*", "/", "*", "17", "+", "5", "+"]
    print("Notation:", notation)
    result = evalRPN(notation)
    print("Result:", result)

    print("\nCar fleet")
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    print("Destination target:", target)
    print("Position of each fleet:", position)
    print("Velocity of each fleet:", speed)
    num_fleets = car_fleet(target, position, speed)
    print("Number of fleets:", num_fleets)

    print("\n Asteroid collision")
    asteroids = [10, -5, 2]
    print("Initial Asteroids:", asteroids)
    asteroids = asteroidCollision(asteroids)
    print("Resulting asteroids:", asteroids)

    print("\nMaximum minimum priduct")
    array = [1, 2, 3, 2]
    print("The array is:", array)
    max_product = maxSumMinProduct(array)
    print("The maximum min product is:", max_product)

    print("Remove K adjecent")
    s = "aaabbcccccbdgghhhg"
    res = removeKAdjecent(s, 3)
    print(res)
