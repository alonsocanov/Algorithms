from numpy import histogram


def valid_parenthesis(string: str):
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


def generate_parenthensis(n: int):
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


def largest_rectangle_of_histogram(histogram: list):
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


if __name__ == '__main__':
    print('\nVerify valid parenthesis')
    string = "()((()))[][[]]"
    print("For the string:", string)
    print("The string is valid, ", valid_parenthesis(string))

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
