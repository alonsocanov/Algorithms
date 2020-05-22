def isPalindrome(array):
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


def main():
    my_array = "anita lava la tina"
    print(isPalindrome(my_array))


if __name__ == '__main__':
    main()
