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
