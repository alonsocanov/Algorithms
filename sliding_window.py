def lengthOfLongestSubstring(s: str) -> int:
    slow = 0
    max_len = 0
    for i in range(len(s)):
        if s[i] in s[slow:i]:
            max_len = max(max_len, len(s[slow:i]))
            slow += s[slow:i].find(s[i]) + 1
    max_len = max(max_len, len(s[slow:]))
    return max_len


def max_value_in_window(array: list[int], k: int):
    queue = []
    output = []
    l, r = 0, 0
    while r < len(array):
        while queue and array[queue[-1]] < array[r]:
            queue.pop()
        queue.append(r)
        if l > queue[0]:
            queue.pop(0)
        if (r + 1) >= k:
            output.append(array[queue[0]])
            l += 1
        r += 1
    return output


if __name__ == '__main__':
    print("\nLenght of longest substring")
    string = "pwwkew"
    print("String:", string)
    length = lengthOfLongestSubstring(string)
    print("Longest substring:", length)

    print("\nSliding window get MAximum of the Window")
    nums = [1, 2, 3, 5, 6, 1, 3, 6, 4, 7, 4]
    k = 3
    print("The array is:", nums)
    print("The size of the window is:", k)
    output = max_value_in_window(nums, k)
    print("The max value of each window is:", output)
