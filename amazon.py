import math
from collections import defaultdict, deque


def coin_flip(string: str):
    one = 0
    flip = 0

    for c in string:
        if c == 'T':
            one += 1
        else:
            flip += 1
        flip = min(flip, one)
    print(flip)
    return flip


coin_flip("HHTHHTT")


def max_nums_teams(skill: list[int], team_size: int, max_diff: int):
    teams = 0
    if team_size > len(skill):
        return False

    skill.sort()
    for i in range(0, len(skill), team_size):
        if i + team_size - 1 < len(skill):
            diff = skill[i + team_size - 1] - skill[i]
            if diff <= max_diff:
                teams += 1
    print(teams)
    return teams


max_nums_teams([3, 4, 3, 1, 6, 5], 3, 2)


def valid_cupon(string):
    stack = []
    for char in string:
        if (stack and stack[-1] != char) or not stack:
            stack.append(char)
        else:
            stack.pop()

    if stack:
        return False
    return True


print(valid_cupon("xyffyxdd"))


def decode(string):
    stack = []

    for i in range(len(string)):
        if string[i] != "]":
            stack.append(string[i])
        else:
            sub_string = ""
            while stack[-1] != "[":
                sub_string = stack.pop() + sub_string
            stack.pop()

            k = ""
            while stack and stack[-1].isnumeric():
                k = stack.pop() + k
            stack.append(int(k) * sub_string)
    return "".join(stack)


print(decode("2[ab3[fg]2[a]]"))


def simple_cipher(string: str, key: int):
    res = ""
    string.upper()
    key = key % 26
    for char in string:
        diff = ord(char) - key
        if diff < ord('A'):
            diff = ord('Z') - (key - (ord(char) - ord('A') + 1))

        res += chr(diff)
    return res


print(simple_cipher("VTAOG", 2))


def lowes_price(price_jeans, price_shoes, price_skirts, price_tops, budeget):
    hash_map = {}
    count = 0

    for j in price_jeans:
        for s in price_shoes:
            curr_sum = j + s
            hash_map[curr_sum] = 1 + hash_map.get(curr_sum, 0)

    for s in price_skirts:
        for t in price_tops:
            curr_val = budeget - (s + t)
            li_keys = [k for k in hash_map if k <= curr_val]
            values = [hash_map[k] for k in li_keys]
            count += sum(values)
    return count


print(lowes_price([2, 3], [4], [2, 3], [1, 2], 10))


def max_profit():
    pass


def shipment_inbalance(parcels):
    imbalance = 0
    for i in range(1, len(parcels)):
        for j in range(i + 1):
            imbalance += abs(max(parcels[j:i+1])-min(parcels[j:i+1]))
    return imbalance


print(shipment_inbalance([1, 2, 3, 4]))


def grid_connections():
    pass


def binary_substring(string: str):
    count = 0
    prev, curr = 0, 1

    for i in range(1, len(string)):
        if string[i] != string[i - 1]:
            count += min(prev, curr)
            prev = curr
            curr = 1
        else:
            curr += 1
    count += min(prev, curr)
    return count


print(binary_substring("010100100001"))


def top_k_frequent_elements(nums: list(int), k: int):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]
    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


def reorder_log_files(logs):
    res1, res2 = [], []

    for log in logs:
        if (log.split()[1].isnumeric()):
            res2.append(log)
        else:
            res1.append(log.split())

        res1.sort(key=lambda x: x[0])
        res2.sort(key=lambda x: x[1:])

        for i in range(len(res1)):
            res1[i] = (" ".join(res1[i]))
        res1.extend(res2)
        return res1


def shopping_patterns(n: int, edges: list[list[int]]):
    g = defaultdict(set)
    for a, b in edges:
        g[a].add(b)
        g[b].add(a)

    d = {n: len(g[n]) for n in g}

    res = int('inf')
    for n in g:
        for m in g[n]:
            for o in g[n] & g[m]:
                res = min(res, d[n] + d[m] + d[o] - 6)
                g[o].remove(n)
            g[m].discard(n)

    return res if res < int('inf') else -1


# print(shopping_patterns(6, [[1, 2], [1, 3], [3, 2], [4, 1], [5, 2], [3, 6]]))

def uniqueTwoSum(nums, target):
    ans, comp = set(), set()
    for n in nums:
        c = target-n
        if c in comp:
            res = (n, c) if n > c else (c, n)
            if res not in ans:
                ans.add(res)
        comp.add(n)
    return len(ans)


def merge_arrays(array_1: list, array_2: list):
    '''
    Merge two number sorted arrays
    '''
    res = []
    i = 0
    j = 0
    while i < len(array_1) and j < len(array_2):
        if array_1[i] < array_2[j]:
            res.append(array_1[i])
            i += 1
        else:
            res.append(array_2[j])
            j += 1
    while i < len(array_1):
        res.append(array_1[i])
        i += 1
    while j < len(array_2):
        res.append(array_2[j])
        j += 1
    return res


def findPairs(a, b, target):
    a.sort(key=lambda x: x[1])
    b.sort(key=lambda x: x[1])
    l, r = 0, len(b) - 1
    ans = []
    curDiff = float('inf')
    while l < len(a) and r >= 0:
        id1, i = a[l]
        id2, j = b[r]
        if (target - i - j == curDiff):
            ans.append([id1, id2])
        elif (i + j <= target and target - i - j < curDiff):
            ans.clear()
            ans.append([id1, id2])
            curDiff = target - i - j
        if (target > i + j):
            l += 1
        else:
            r -= 1
    return ans


def auto_scale(array: list[int], instances: int):
    i = 0
    max_val = 2 * 108
    while i < len(array):
        if array[i] < 25 and instances > 1:
            instances = (instances / 2) + (instances % 2)
            i += 9
        elif array[i] > 60 and max_val > instances * 2:
            instances *= 2
            i += 9
        i += 1
    return instances


def min_difficulty(jobs: list[int], d: int):

    n = len(jobs)
    if n < d:
        return -1

    dp = [[] for _ in range(n)]

    return dp(0, d)


def storage_optim(connections):
    def dfs(node, adj, visited) -> int:
        k = 0

        stack = [node]
        visited.add(node)
        u = None
        while stack:
            u = stack.pop()
            k += 1
            # for every node u can reach
            for v in adj[u]:
                if v not in visited:
                    visited.add(v)
                    stack.append(v)
        return k
    visited = set()
    # create adjacency list for edges
    adj = [[] for _ in range(n)]
    for edge in connections:
        u = edge[0]
        v = edge[1]

        adj[u].append(v)
        adj[v].append(u)

    ans = 0

    for node in range(n):
        # only start when this the node in unvisited
        if node not in visited:
            k = dfs(node, adj, visited)
            ans += math.ceil((k) ** (1/2))

    return ans


def word_lader(start, end, words):
    if end not in words:
        return 0

    nei = defaultdict(list)
    words.append(start)
    for word in words:
        for j in range(len(word)):
            pattern = word[:j] + "*" + word[j + 1]
            nei[pattern].append(word)

    visit = set([start])
    q = deque([start])
    res = 1
    while q:
        for _ in range(len(q)):
            word = q.popleft()
            if word == end:
                return res
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                for nei_word in nei[pattern]:
                    if nei_word not in visit:
                        visit.add(nei_word)
                        q.append(nei_word)


def countPrimeStrings(number, l):
    MOD = 1000000007

    def isPrime(number):

        num = int(number)
        i = 2

        while i * i <= num:
            if ((num % i) == 0):
                return False
            i += 1

        if num > 1:
            return True
        else:
            return False

    # 1 based indexing
    if (l == 0):
        return 1
    cnt = 0

    # Consider every suffix
    # up to 6 digits
    for j in range(1, 7):

        # Number should not have
        # a leading zero and
        # it should be a prime number
        if (l - j >= 0 and
            number[l - j] != '0' and
                isPrime(number[l - j: l])):
            cnt += countPrimeStrings(number,
                                     l - j)
            cnt %= MOD

    # Return the final result
    return cnt
