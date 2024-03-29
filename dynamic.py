def coin_change(coins: list[int], amount: int) -> int:
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])

    return dp[amount] if dp[amount] != amount + 1 else -1


def num_decodings(s: str) -> int:
    dp = {len(s): 1}

    def dfs(i):
        if i in dp:
            return dp[i]
        if s[i] == "O":
            return 0
        res = dfs(i + 1)
        if (i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456")):
            res += dfs(i + 2)
        dp[i] = res
        return res
    return dfs(0)


def minStepsToMinimize(n: int) -> int:
    if not n:
        return 0

    dp = [n+1] * (n + 1)
    dp[1] = 0
    for i in range(1, n):
        dp[i + 1] = min(dp[i + 1], dp[i] + 1)
        if i * 2 <= n:
            dp[i * 2] = min(dp[i] + 1, dp[i * 2])
        if i * 3 <= n:
            dp[i * 3] = min(dp[i] + 1, dp[i * 3])
    return dp[n]


if __name__ == '__main__':
    print("\nCoin change")
    coins = [1, 2, 3]
    target = 11
    print("Available coins:", coins)
    print("Target:", coins)
    print("Minimum number of coins:", coin_change(coins, target))

    print("\nNumber of decodings for a string")
    string = "123"
    print("The string is:", string)
    num_dec = num_decodings(string)
    print("The number of decodings is:", num_dec)

    print("\nMinimum steps to minimize n")
    val = 10
    print("The value is:", val)
    min_steps = minStepsToMinimize(val)
    print("The minimun number of steps are:", min_steps)
