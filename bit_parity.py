def swapBits(x, i, j):
    res = x
    if (x >> i) & 1 != (x >> j) & 1:
        mask = (1 << i) | (1 << j)
        res ^= mask
    return res


def main():
    val = 11
    print(val)
    value_swap = swapBits(val, 1, 2)
    print(value_swap)


if __name__ == '__main__':
    main()
