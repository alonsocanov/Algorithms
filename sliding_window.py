def lengthOfLongestSubstring(s: str) -> int:
    slow = 0
    max_len = 0
    for i in range(len(s)):
        if s[i] in s[slow:i]:
            max_len = max(max_len, len(s[slow:i]))
            slow += s[slow:i].find(s[i]) + 1
    max_len = max(max_len, len(s[slow:]))
    return max_len


if __name__ == '__main__':
    print("\nLenght of longest substring")
    string = "pwwkew"
    print("String:", string)
    length = lengthOfLongestSubstring(string)
    print("Longest substring:", length)
