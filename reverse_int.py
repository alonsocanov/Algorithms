def reverse(x):
    res = 0
    remain = abs(x)
    while remain:
        res = res * 10 + remain % 10
        remain //= 10
    return res if x > 0 else -res


def main():
    val = 1019
    print(val)
    rev = reverse(val)
    print(rev)


if __name__ == '__main__':
    main()
