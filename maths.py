import re
from unicodedata import digit


def is_happy(n: int):
    visit = set()

    def sum_of_squares(n):
        output = 0
        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n //= 10
        return output

    while n not in visit:
        visit.add(n)
        n = sum_of_squares(n)

        if n == 1:
            return True
    return False


def plus_one(array: list[int]):
    array = array[::-1]
    one, i = 1, 0

    while one:
        if i < len(array):
            if array[i] == 9:
                array[i] = 0
            else:
                array[i] += 1
                one = 0
        else:
            array.append(1)
            one = 0
        i += 1
    return array[::-1]


if __name__ == '__main__':
    print("\nIs Happy number")
    n = 19
    print("The number is:", n)
    print("Is happy number:", is_happy(n))

    print("\nPlus One")
    array = [1, 2, 3, 9]
    print("My  array is:", array)
    add_one = plus_one(array)
    print("When adding 1 we get:", add_one)
