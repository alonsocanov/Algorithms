from email import message


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
    for idx in range(1, len(string)):
        digit = string[idx]
        if digit == prev_digit:
            if len(mapping[digit]) - 1 > num_reps:
                num_reps += 1
                if idx == len(string) - 1:
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
