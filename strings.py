def string_decode_col(strning: str):
    pass


def reverse_words_in_sentence(string: str):
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
    mapping = ('0', '1', 'ABC', 'DEF', 'GHI',
               'JKL', 'MNO', 'PQRS', 'TUV', 'XYZ')
