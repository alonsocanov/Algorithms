def isInt(array):
    for i in array:
        if i <= "0" or i >= "9":
            return False
    return True



def main():
    my_array = "I am 5 years old"
    my_array = "5124"
    print(isInt(my_array))

if __name__ == '__main__':
    main()