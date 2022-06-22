import time


def parity_bit_v1(value: int):
    '''
    The parity of a word bit is 1 if the number of 1s in a word is odd, o is the number of 1s in a word is even
    '''
    result = 0
    while value:
        result ^= value & 1
        value >>= 1
    return result


def parity_bit_v2(value: int):
    '''
    The parity of a word bit is 1 if the number of 1s in a word is odd, o is the number of 1s in a word is even
    '''
    pow_2 = [32, 16, 8, 4, 2, 1]
    for i in pow_2:
        value ^= value >> i
    return value & 0x1


def single_number(array: list[int]):
    res = 0
    for val in array:
        res ^= val
    return res


def count_num_bits_to_1(value: int):
    '''
     Counting number of bits equal to 1 aims to learn bit shifting algorithms
    '''
    count = 0
    while value:
        count += value & 1
        value >>= 1
    return count


def swap_bits(x, i, j):
    '''
    check bit parity
    '''
    res = x
    if (x >> i) & 1 != (x >> j) & 1:
        mask = (1 << i) | (1 << j)
        res ^= mask
    return res


def reverse_int(x):
    '''
    reverse an integer
    '''
    res = 0
    remain = abs(x)
    while remain:
        res = res * 10 + remain % 10
        remain //= 10
    return res if x > 0 else -res


if __name__ == '__main__':
    print('\nCheck bit parity')
    val = 11
    print(val)
    value_swap = swap_bits(val, 1, 2)
    print(value_swap)

    print('\nReverse an integer')
    val = 1019
    print(val)
    rev = reverse_int(val)
    print(rev)

    print("\nNumber of bits equal to 1 in integer")
    value = 12
    count = count_num_bits_to_1(value)
    print("Value:", format(value, 'b'))
    print("The number of bits equal to 1 is:", count)

    print("\nParity bits")
    value = 55500
    t = time.time()
    result = parity_bit_v1(value)
    print("Bit value:", format(value, 'b'))
    print("Parity bit:", result)
    print("Time for parity bit v1:", time.time() - t)
    t = time.time()
    result = parity_bit_v2(value)
    print("Bit value:", format(value, 'b'))
    print("Parity bit:", result)
    print("Time for parity bit v1:", time.time() - t)
