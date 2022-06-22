def lastStoneWeight(stones: list[int]) -> int:
    '''
    We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
    '''
    stones.sort()
    print(stones)
    while len(stones) > 1:
        heavyer, heavyest = stones[-2:]
        reminder = heavyest - heavyer
        stones.pop()
        stones[-1] = reminder
        print(stones)


if __name__ == '__main__':
    print('\nLast stone weight')
    stones = [2, 7, 4, 1, 8, 1]
    print("My stones:", stones)
    last_stone = lastStoneWeight(stones)
    print("My reminder stone is:", last_stone)
