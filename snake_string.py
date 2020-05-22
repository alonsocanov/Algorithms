def snakeSring(s):
    result = []
    # height of the snake 3
    for i in range(1, len(s), 4):
        result.append(s[i])
    for i in range(0, len(s), 2):
        result.append(s[i])
    for i in range(3, len(s), 4):
        result.append(s[i])
    return ''.join(result)


def main():
    phrase = "Hello World!"
    print(phrase)
    snake = snakeSring(phrase)
    print(snake)
    phrase = [1, 2, 3, 4, 5]
    print(phrase[1::3])


if __name__ == '__main__':
    main()
