def isValue(array):
    if array == "":
        return False
    decimal_flag = 0
    for i in array:
        if i == ".":
            decimal_flag += 1
        if ((i <= "0" or i >= "9") and i != ".") or decimal_flag == 2:
            return False
    return True


def main():
    my_array = "I am 5 years old"
    print(my_array, ":", isValue(my_array))
    my_array = "5124"
    print(my_array, ":", isValue(my_array))
    my_array = ""
    print(my_array, ":", isValue(my_array))
    my_array = "12.5"
    print(my_array, ":", isValue(my_array))
    my_array = "12..5"
    print(my_array, ":", isValue(my_array))


if __name__ == '__main__':
    main()
