def duchFlag(a, pivot_index):
    pivot = a[pivot_index]
    smaller, equal, larger = 0, 0, len(a)
    while equal < larger:
        if a[equal] < pivot:
            a[smaller], a[equal] = a[equal], a[smaller]
            smaller += 1
            equal += 1
        elif a[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            a[equal], a[larger] = a[larger], a[equal]


def main():
    li = [0, 1, 2, 0, 2, 1, 1]
    print(li)
    duchFlag(li, 2)
    print(li)


if __name__ == '__main__':
    main()
