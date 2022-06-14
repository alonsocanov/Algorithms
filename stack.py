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
