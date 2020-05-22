def equalToTarget(target, s):
    my_set = set()
    for i in s:
        my_set.add(target - i)
        if i in my_set:
            return True
    return False


def main():
    my_list = [1, 2, 3]
    target = 5
    print(equalToTarget(target, my_list))


if __name__ == '__main__':
    main()
