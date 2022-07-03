
import heapq

from numpy import char


def string_decode_col(strning: str):
    pass


def reverse_words_in_sentence(string: str):
    '''
    Reverse the sentence Order
    '''
    def reverse_range(string: str, start: int, end: int):
        string = list(string)
        while start < end:
            string[start], string[end] = string[end], string[start]
            start, end = start + 1, end - 1
        return ''.join(string)

    string = string[::-1]
    start = 0
    while True:
        end = string.find(' ', start)
        if end < 0:
            break
        string = reverse_range(string, start, end - 1)
        start = end + 1
    string = reverse_range(string, start, len(string) - 1)
    return string


def phone_mnemonics(string: str):
    mapping = {'0': ' ', '1': '', '2': 'ABC', '3': 'DEF', '4': 'GHI',
               '5': 'JKL', '6': 'MNO', '7': 'PQRS', '8': 'TUV', '9': 'XYZ'}
    prev_digit = string[0]
    message = ''
    num_reps = 0
    str_len = len(string)
    for idx in range(1, str_len):
        digit = string[idx]
        if digit == prev_digit:
            if len(mapping[digit]) - 1 > num_reps:
                num_reps += 1
                if idx == str_len - 1:
                    message += mapping[digit][num_reps]
            else:
                message += mapping[digit][num_reps]
                num_reps = 0
        else:
            if len(mapping[prev_digit]) == 0:
                message += ''
            else:
                message += mapping[prev_digit][num_reps]
            prev_digit = digit
            num_reps = 0

    return message


def is_palindrome(array):
    '''
    check if string is palindrome
    '''
    head = 0
    tail = len(array) - 1
    while head <= int((len(array) - 1) / 2):
        if array[head] == " ":
            head += 1
        if array[tail] == " ":
            tail -= 1
        if array[head] != array[tail]:
            return False
        head += 1
        tail -= 1
    return True


def is_value(array):
    '''
    find if a str in numeric or a decimal
    '''
    if array == "":
        return False
    decimal_flag = 0
    for i in array:
        if i == ".":
            decimal_flag += 1
        if ((i <= "0" or i >= "9") and i != ".") or decimal_flag == 2:
            return False
    return True


def roman_to_integer(s):
    '''
    convert from roman to integers
    '''
    T = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    s_copy = s[::-1]
    val = 0
    i = 0
    while i < len(s_copy):
        if i < len(s) - 1 and T[s_copy[i]] > T[s_copy[i + 1]]:
            val += T[s_copy[i]] - T[s_copy[i + 1]]
            i += 1
        else:
            val += T[s_copy[i]]
        i += 1
    return val


def valid_ip(string):
    '''
    A valid ip addres contains numbers bettween 0 - 255 and must have 4 integers
    00 and 000 is not valid
    '''
    def is_valid(string):
        return len(string) == 1 or (string[0] != '0' and int(string) <= 255)

    result, parts = [], [None] * 4
    for idx in range(1, min(4, len(string))):
        parts[0] = string[:idx]
        if is_valid(parts[0]):
            for jdx in range(1, min(len(string) - idx, 4)):
                parts[1] = string[idx:idx + jdx]
                if is_valid(parts[1]):
                    for kdx in range(1, min(len(string) - idx - jdx, 4)):
                        parts[2], parts[3] = string[idx + jdx:idx +
                                                    jdx + kdx], string[idx + jdx + kdx:]
                        if is_valid(parts[2]) and is_valid(parts[3]):
                            result.append('.'.join(parts))
    return result


def snake_sring(string):
    result = []
    # height of the snake 3
    for i in range(1, len(string), 4):
        result.append(string[i])
    for i in range(0, len(string), 2):
        result.append(string[i])
    for i in range(3, len(string), 4):
        result.append(string[i])
    return ''.join(result)


def run_encoding(string):
    count, result = 1, []
    for idx in range(1, len(string) + 1):
        if idx == len(string) or string[idx] != string[idx - 1]:
            result.append(str(count) + string[idx - 1])


def reverse_word_order(string: str):
    '''
    Reverse the order of words in a given sentence
    time complexity: O(n)
    memory complexity: O(1)
    '''
    idx_end = 0
    counter = 0
    lenght = len(string)
    while counter < lenght:
        if string[idx_end] == ' ' or idx_end == lenght - 1:
            word = string[:idx_end]
            middle_sentence = string[idx_end + 1: lenght - counter + idx_end]
            end_sentence = string[lenght - counter + idx_end:]
            string = middle_sentence + ' ' + word + ' ' + end_sentence
            idx_end = 0
            counter += 1

        idx_end += 1
        counter += 1

    return string


def reorganize_string(s):
    '''
    No adjecent characters repeating
    '''
    char_frequency = dict()
    # O(n)
    for c in s:
        char_frequency[c] = 1 + char_frequency.get(c, 0)

    max_heap = [[-cnt, char] for char, cnt in char_frequency.items()]
    heapq.heapify(max_heap)  # O(n)

    prev = ""
    res = ""
    while max_heap or prev:
        if prev and not max_heap:
            return ""
        cnt, char = heapq.heappop(max_heap)
        res += char
        cnt += 1

        if prev:
            heapq.heappush(max_heap, prev)
            prev = ""

        if cnt != 0:
            prev = [cnt, char]
    return res


if __name__ == '__main__':
    print(
        '\nReverse the order of words in a given sentence')
    string = 'The big brown fox'
    print('Sentence:', string)
    rev_string = reverse_word_order(string)
    print('Reversed string:', rev_string)

    print("\nReorganize string")
    string = "aabbcgdvvbb"
    string = reorganize_string(string)
    print("Reorganized string:", string)
