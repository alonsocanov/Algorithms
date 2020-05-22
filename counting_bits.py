def countBits(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits


def main():
    val = 10
    print(val)
    nb_bits = countBits(val)
    print(nb_bits)


if __name__ == '__main__':
    main()
